import asyncio
import threading

from enum import Enum

from AdaImageControl import GetVideo
from AdaDroneControl import AdaDroneController


class FSM_STATES(Enum):
    IDEAL = 1
    INIT = 2
    TAKEOFF = 3
    SERVO = 4
    FINISH = 5


FSM_STATE = FSM_STATES.INIT


async def Mission(self: AdaDroneController):
    global FSM_STATE

    while True:
        match FSM_STATE:
            case FSM_STATES.INIT:
                self.debug.Log("Initializing drone...")
                await self.connect()
                await self.start_offboard_mode()
                FSM_STATE = FSM_STATES.TAKEOFF

            case FSM_STATES.TAKEOFF:
                self.debug.Log("Arming and taking off...")
                await self.arm_and_takeoff()
                FSM_STATE = FSM_STATES.SERVO

            case FSM_STATES.SERVO:
                self.debug.Log("Performing servo action...")
                await self.move()
                await asyncio.sleep(10)
                FSM_STATE = FSM_STATES.FINISH

            case FSM_STATES.IDEAL:
                self.debug.Log("Drone in ideal state...")
                await asyncio.sleep(0.1)

            case FSM_STATES.FINISH:
                self.debug.Log("Mission complete. Finishing...")
                break

    await self.stop_movement()
    await self.stop_offboard_mode()
    await self.return_to_launch_and_land()
    self.debug.Log("Mission complete")


if __name__ == "__main__":
    # Create a Drone Controller Object
    DroneController = AdaDroneController()

    # Create a thread for the video stream to avoid blocking the main event loop
    video_thread = threading.Thread(target=GetVideo, daemon=True)
    video_thread.start()

    # Run the drone control async function
    asyncio.run(Mission(DroneController))
