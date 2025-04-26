import cv2
import cv2.aruco as aruco
from scipy.spatial import distance as dist
import imutils
from imutils import contours

def findArucoMarker(img,markerSize= 6, totalMarkers=250,
      draw=True):
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    #load the dictionary that was used to generate the markers
    arucoDict = aruco.getPredefinedDictionary(key)
    arucoParam = aruco.DetectorParameters()
            
    imgGray = imutils.resize(imgGray, width=500)
    imgGray=cv2.GaussianBlur(imgGray,(7,7),0)

    #perform edge detection, then perform 
    #dilation + erosion to close gaps in between edges

    imgGray=cv2.dilate(imgGray, None, iterations=1)
    imgGray = cv2.erode(imgGray , None, iterations=1)

    #find contours in edge map
    cnts = cv2.findContours(imgGray.copy(),
                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)

    #sort the contours from left-to-right and initialize 
    (cnts,_)= contours.sort_contours(cnts)
    #for pixel to inch calibration


    pixelsPerMetric=None
    arucofound= findArucoMarker(img , totalMarkers=100)
    if len(arucofound[0])!=0:
        aruco_perimeter = cv2.arcLength(arucofound[0][0][0], True)

        #Pixel to inch ratio
        #perimeter of the aruco marker is 8 inches

        pixelsPerMetric = aruco_perimeter /8
        print(" pixel to inch", pixelsPerMetric)

    else:
        pixelsPerMetric  = 38.0
        

    for c in cnts:

        #if the contour is not sufficiently large, 
        #ignore it
        if cv2.contourArea(c)<2000:
            continue

#bounding rectangle is drawn within the minimum area , 
#so it considers the rotation also
  # the function used is cv.minAreaRect(). it returns
  #a box2D structure which contains following details:
     

    # Detect aruco marker and use
    # it's dimension to calculate the pixel to inch ratio
    (tl, tr, br, bl) = box
    width_1 = (dist.euclidean(tr, tl))
    height_1 = (dist.euclidean(bl, tl))
    d_wd= width_1/pixelsPerMetric
    d_ht= height_1/pixelsPerMetric        


    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
        bboxs, ids, rejected= aruco.detectMarkers(imgGray,
             arucoDict, parameters=arucoParam)
        print(ids)
    return[ bboxs, ids, rejected]

def main():
    # Define the GStreamer pipeline to receive the H.264 video stream over UDP
    gst_pipeline = (
        "udpsrc port=5600 ! application/x-rtp,encoding-name=H264,payload=96 ! "
        "rtph264depay ! avdec_h264 ! videoconvert ! appsink"
    )

    # Create a VideoCapture object using the GStreamer pipeline
    cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Error: Could not open UDP stream.")
        exit()

    # Load the predefined dictionary for ArUco markers
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()

    detector = aruco.ArucoDetector(aruco_dict, parameters)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        findArucoMarker(frame)

        # Display the frame
        cv2.imshow("Received Stream with ArUco Detection", frame)

        # Exit condition (press 'q' to quit)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
