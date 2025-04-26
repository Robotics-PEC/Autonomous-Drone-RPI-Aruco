import cv2
from cv2 import aruco
from AdaVideoStream import AdaVideoStream


class AdaAruco:

    def __init__(self, arucoDictionary=aruco.DICT_4X4_250):
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

                _corners = self.corners[idx][0]

                # Compute center (average top-left and bottom-right)
                _centerX = int((_corners[0][0] + _corners[2][0]) / 2)
                _centerY = int((_corners[0][1] + _corners[2][1]) / 2)

                # Draw the center
                cv2.circle(self.image, (_centerX, _centerY), 1, (0, 255, 0), -1)
                cv2.line(
                    self.image,
                    (_centerX, _centerY),
                    (self.FrameCenterX, self.FrameCenterY),
                    (0, 255, 0),
                    1,
                )


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
