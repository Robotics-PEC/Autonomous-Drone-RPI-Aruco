import asyncio

from mavsdk import System
from mavsdk.offboard import OffboardError, VelocityNedYaw
from AdaDebug import AdaDebug


class AdaDroneController:
    def __init__(self, connection_url="udp://:14540"):
        self.drone = System()
        self.debug = AdaDebug("AdaDroneController")
        self.connection_url = connection_url

    async def connect(self):
        await self.drone.connect(system_address=self.connection_url)

        self.debug.Log("Waiting for drone to connect...")
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                self.debug.Log("Drone discovered!")
                break

        self.debug.Log("Waiting for global position estimate...")
        async for health in self.drone.telemetry.health():
            if health.is_global_position_ok:
                self.debug.Log("Global position estimate OK")
                break

    async def arm_and_takeoff(self, altitude=5):
        self.debug.Log("Arming")
        await self.drone.action.arm()

        self.debug.Log(f"Taking off to {altitude} meters")
        await self.drone.action.set_takeoff_altitude(altitude)
        await self.drone.action.takeoff()
        await asyncio.sleep(30)  # Wait for stable takeoff

    async def start_offboard_mode(self):
        self.debug.Log("Starting Offboard mode")
        await self.drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 0.0, 0.0, 0.0))

        try:
            await self.drone.offboard.start()
        except OffboardError as error:
            self.debug.Log(f"Starting offboard failed: {error._result.result}")
            await self.drone.action.disarm()
            raise

    async def move(self, north=0.0, east=0.0, down=0.0, yaw=0.0, duration=5):
        self.debug.Log(
            f"Moving (N:{north}, E:{east}, D:{down}, Yaw:{yaw}) for {duration} seconds"
        )
        await self.drone.offboard.set_velocity_ned(
            VelocityNedYaw(north, east, down, yaw)
        )
        await asyncio.sleep(duration)

    async def stop_movement(self):
        self.debug.Log("Stopping movement")
        await self.drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 0.0, 0.0, 0.0))
        await asyncio.sleep(1)

    async def stop_offboard_mode(self):
        self.debug.Log("Stopping offboard mode")
        try:
            await self.drone.offboard.stop()
        except OffboardError as error:
            self.debug.Log(f"Stopping offboard failed: {error._result.result}")

    async def return_to_launch_and_land(self):
        self.debug.Log("Returning to Launch (RTL)")
        await self.drone.action.return_to_launch()

        self.debug.Log("Waiting to land...")
        async for in_air in self.drone.telemetry.in_air():
            if not in_air:
                self.debug.Log("Landed at home position")
                break
            await asyncio.sleep(1)


async def DemoMission(self):
    await self.connect()
    await self.arm_and_takeoff()

    await self.start_offboard_mode()

    await self.move(north=1.0, east=0.0, down=0.0, yaw=0.0, duration=5)
    await self.move(north=0.0, east=1.0, down=0.0, yaw=0.0, duration=5)
    await self.move(north=-1.0, east=0.0, down=0.0, yaw=0.0, duration=5)

    await self.stop_movement()
    await self.stop_offboard_mode()

    await self.return_to_launch_and_land()

    self.debug.Log("Mission complete")


if __name__ == "__main__":
    DroneController = AdaDroneController()
    asyncio.run(DemoMission(DroneController))
