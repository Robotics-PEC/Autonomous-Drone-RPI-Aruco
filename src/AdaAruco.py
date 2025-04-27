import cv2

from cv2 import aruco

from AdaVideoStream import AdaVideoStream
from AdaDebug import AdaDebug


class AdaAruco:

    def __init__(self, arucoDictionary=aruco.DICT_4X4_250):
        # Starting Module
        Debug = AdaDebug("AdaAruco")

        # Load the specified ArUco dictionary (default is 4x4 with 250 markers)
        aruco_dict = aruco.getPredefinedDictionary(arucoDictionary)

        # Create a set of parameters for the ArUco marker detector
        parameters = aruco.DetectorParameters()

        # Initialize the ArUco detector with the selected dictionary and parameters
        self.detector = aruco.ArucoDetector(aruco_dict, parameters)

    def PutImage(self, image):
        self.image = image
        height, width = image.shape[:2]
        self.FrameCenterX = width // 2
        self.FrameCenterY = height // 2

    def DetectAruco(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.corners, self.ids, rejected = self.detector.detectMarkers(gray)
        if self.ids is not None:
            aruco.drawDetectedMarkers(self.image, self.corners, self.ids)

    def GetCenter(self):
        if self.ids is not None:
            for idx, id in enumerate(self.ids):

                corners = self.corners[idx][0]

                # Compute center (average top-left and bottom-right)
                centerX = int((corners[0][0] + corners[2][0]) / 2)
                centerY = int((corners[0][1] + corners[2][1]) / 2)

                error_x = (self.FrameCenterX - centerX) / self.FrameCenterX
                error_y = (self.FrameCenterY - centerY) / self.FrameCenterY

                # Draw the center
                cv2.circle(self.image, (centerX, centerY), 1, (0, 255, 0), -1)
                cv2.line(
                    self.image,
                    (centerX, centerY),
                    (self.FrameCenterX, self.FrameCenterY),
                    (0, 255, 0),
                    1,
                )

                return (error_x, error_y)


if __name__ == "__main__":
    CameraStreamer = AdaVideoStream()
    AdaArucoDetector = AdaAruco()

    while True:
        frame = CameraStreamer.read_frame()
        AdaArucoDetector.PutImage(frame)
        AdaArucoDetector.DetectAruco()
        AdaArucoDetector.GetCenter()

        # Display the frame
        cv2.imshow("Received Stream", frame)

        # Exit condition (press 'q' to quit)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    del CameraStreamer
    del AdaArucoDetector
    cv2.destroyAllWindows()
