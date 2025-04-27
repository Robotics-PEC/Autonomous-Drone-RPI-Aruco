import cv2

from AdaVideoStream import AdaVideoStream
from AdaAruco import AdaAruco
from AdaDebug import AdaDebug


# Function to handle the video stream in a separate thread
def GetVideo():
    Debug = AdaDebug("AdaImageControl")
    # Create the objects each time we loop (if needed)
    CameraStreamer = AdaVideoStream()
    ArucoDetector = AdaAruco()

    while True:
        # Check if the stop event is triggered before continuing

        frame = CameraStreamer.read_frame()
        ArucoDetector.PutImage(frame)
        ArucoDetector.DetectAruco()
        ArucoDetector.GetCenter()

        # Display the frame
        cv2.imshow("GStreamer Video", frame)

        # Wait for a key press and check if the stop event is set
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources after the inner loop ends
    del CameraStreamer
    cv2.destroyAllWindows()

    # Final cleanup when the stop event is triggered
    Debug.Log("Stopped")
