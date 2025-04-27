import asyncio
import threading
import cv2

from enum import Enum

from AdaDebug import AdaDebug
from AdaImageControl import GetVideo
from AdaDroneControl import AdaDroneController
from AdaController import AdaPIDController
from AdaQueue import get_result


class FSM_STATES(Enum):
    IDEAL = 1
    INIT = 2
    TAKEOFF = 3
    SERVO = 4
    FINISH = 5


FSM_STATE = FSM_STATES.INIT

PIDControllerX = AdaPIDController(1.5, 0, 0)
PIDControllerY = AdaPIDController(1.5, 0, 0)

# Create a debugger object
Debug = AdaDebug("Main")

# Create a Drone Controller Object
DroneController = AdaDroneController()


async def Mission(self: AdaDroneController):
    global FSM_STATE

    while True:
        match FSM_STATE:
            case FSM_STATES.INIT:
                Debug.Log("Initializing drone...")
                await self.connect()
                await self.start_offboard_mode()
                await self.arm()
                FSM_STATE = FSM_STATES.TAKEOFF

            case FSM_STATES.TAKEOFF:
                Debug.Log("Arming and taking off...")
                await self.takeoff()
                FSM_STATE = FSM_STATES.SERVO

            case FSM_STATES.SERVO:
                result = get_result()
                if result is not None:
                    errorX, errorY = result
                    xVal = PIDControllerX.compute(errorX,0.1)
                    yVal = PIDControllerX.compute(errorY,0.1)
                    Debug.Log((f"{xVal}," f"{yVal}"))
                    # await self.move(yVal,xVal,0,0,0.1)

            case FSM_STATES.IDEAL:
                Debug.Log("Drone in ideal state...")
                await asyncio.sleep(0.3)

            case FSM_STATES.FINISH:
                Debug.Log("Mission complete. Finishing...")
                break

    await self.stop_movement()
    await self.stop_offboard_mode()
    await self.return_to_launch_and_land()
    Debug.Log("Mission complete")


if __name__ == "__main__":

    # Create a thread for the video stream to avoid blocking the main event loop
    video_thread = threading.Thread(target=GetVideo, daemon=True)
    video_thread.start()

    # Run the drone control async function
    asyncio.run(Mission(DroneController))
