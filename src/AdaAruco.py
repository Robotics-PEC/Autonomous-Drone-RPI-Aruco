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

    def DetectAruco(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = self.detector.detectMarkers(gray)
        if ids is not None:
            aruco.drawDetectedMarkers(image, corners, ids)


if __name__ == "__main__":
    CameraStreamer = AdaVideoStream()
    AdaArucoDetector = AdaAruco()

    while True:
        frame = CameraStreamer.read_frame()
        AdaArucoDetector.DetectAruco(frame)

        # Display the frame
        cv2.imshow("Received Stream", frame)

        # Exit condition (press 'q' to quit)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    del CameraStreamer
    del AdaArucoDetector
    cv2.destroyAllWindows()
