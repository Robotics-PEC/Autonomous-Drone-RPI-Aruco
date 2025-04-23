import asyncio
from mavsdk import System
from mavsdk.offboard import OffboardError, VelocityNedYaw

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    print("Waiting for global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate OK")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(7)  # Climb to ~10ft / ~3m

    print("-- Starting Offboard mode")
    await drone.offboard.set_velocity_ned(
        VelocityNedYaw(0.0, 0.0, 0.0, 0.0))  # Initial stable command
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard failed: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Moving forward for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(1.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(5)

    print("-- Moving right for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 1.0, 0.0, 0.0))
    await asyncio.sleep(5)

    print("-- Moving back for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(-1.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(5)

    print("-- Stopping movement")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(1)

    print("-- Stopping offboard mode")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard failed: {error._result.result}")

    print("-- Returning to Launch (RTL)")
    await drone.action.return_to_launch()

    # Wait until landed
    async for in_air in drone.telemetry.in_air():
        if not in_air:
            print("-- Landed at home position")
            break
        await asyncio.sleep(1)

    print("-- Mission complete")

def main():
    print("Starting mission...")
    asyncio.run(run())

if __name__ == "__main__":
    main()
