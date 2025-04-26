import cv2

from AdaDebug import AdaDebug


class AdaVideoStream:
    """
    Video Streamer class, used to create a wrapper around cv2 to get frames from
    gstreamer
    """

    def __init__(self, port: int = 5600):
        # Starting Debug
        Debug = AdaDebug("AdaVideoStream")

        # Create a GStreamer Pipeline
        pipeline = (
            f"udpsrc port={port} ! application/x-rtp,encoding-name=H264,payload=96 ! "
            "rtph264depay ! avdec_h264 ! videoconvert ! appsink"
        )

        # Create a capture object using the pipeline
        self.capture = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

        # Error checking for created object
        if not self.capture.isOpened():
            Debug.log("Error: Could not open UDP stream.")
            exit()

    def read_frame(self):
        # Read frame from the capture object
        ret, frame = self.capture.read()

        # Return the frame is ret is true otherwise return empty
        if ret:
            return frame
        return None

    def __del__(self):
        if hasattr(self, "capture") and self.capture.isOpened():
            self.capture.release()


if __name__ == "__main__":
    CameraStreamer = AdaVideoStream()

    while True:
        frame = CameraStreamer.read_frame()
        cv2.imshow("GStreamer Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    del CameraStreamer
    cv2.destroyAllWindows()
