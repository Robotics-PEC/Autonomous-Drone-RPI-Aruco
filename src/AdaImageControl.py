import cv2

from AdaVideoStream import AdaVideoStream
from AdaAruco import AdaAruco

# Function to handle the video stream in a separate thread
def GetVideo():
    CameraStreamer = AdaVideoStream()
    ArucoDetector = AdaAruco()
    while True:
        frame = CameraStreamer.read_frame()
        ArucoDetector.PutImage(frame)
        ArucoDetector.DetectAruco()
        ArucoDetector.GetCenter()
        cv2.imshow("GStreamer Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    del CameraStreamer
    cv2.destroyAllWindows()