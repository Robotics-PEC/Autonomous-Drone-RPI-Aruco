import asyncio
import threading
import time

from mavsdk import System
from mavsdk.offboard import OffboardError, VelocityNedYaw

from AdaImageControl import GetVideo
from AdaDebug import AdaDebug

# Define an Event to signal video thread to stop
stop_event = threading.Event()

# Define async function to run the drone control
async def run():
    drone = System()
    Debug = AdaDebug("Main")
    await drone.connect(system_address="udp://:14540")

    Debug.Log("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            Debug.Log("Drone discovered!")
            break

    Debug.Log("Waiting for global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            Debug.Log("Global position estimate OK")
            break

    Debug.Log("Arming")
    await drone.action.arm()

    Debug.Log("Taking off")
    await drone.action.set_takeoff_altitude(5)
    await drone.action.takeoff()
    await asyncio.sleep(30)

    Debug.Log("Starting Offboard mode")
    await drone.offboard.set_velocity_ned(
        VelocityNedYaw(0.0, 0.0, 0.0, 0.0)
    )  # Initial stable command
    try:
        await drone.offboard.start()
    except OffboardError as error:
        Debug.Log(f"Starting offboard failed: {error._result.result}")
        Debug.Log("Disarming")
        await drone.action.disarm()
        return

    Debug.Log("Moving forward for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(1.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(5)

    Debug.Log("Moving right for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 1.0, 0.0, 0.0))
    await asyncio.sleep(5)

    Debug.Log("Moving back for 5 seconds")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(-1.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(5)

    Debug.Log("Stopping movement")
    await drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(1)

    Debug.Log("Stopping offboard mode")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        Debug.Log(f"Stopping offboard failed: {error._result.result}")

    Debug.Log("Returning to Launch (RTL)")
    await drone.action.return_to_launch()

    # Wait until landed
    async for in_air in drone.telemetry.in_air():
        if not in_air:
            Debug.Log("Landed at home position")
            break
        await asyncio.sleep(1)

    Debug.Log("Mission complete")

    # Signal video thread to stop
    stop_event.set()


# Main function to run both video stream and drone control concurrently
async def main():
    # Create a thread for the video stream to avoid blocking the main event loop
    video_thread = threading.Thread(target=GetVideo, args=(stop_event,))
    video_thread.start()

    # Run the drone control async function
    await run()

    # Wait for the video thread to finish (if needed)
    video_thread.join()


if __name__ == "__main__":
    asyncio.run(main())
