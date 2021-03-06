# script for identifying the hsv values of a colour using OpenCV HSV (Hue, Saturation, Value)
# use the sliders to detect the colour being tested 
# credits https://www.youtube.com/watch?v=AMFhjir4WgQ

import cv2
import numpy as np

def nothing(x):
    #any function here
    pass

cap = cv2.VideoCapture(0) #captures video from the main camera,

# create a trackbar window to help tune the detection and find the HSV
cv2.namedWindow("Trackbars")

# create the trackbars for each HSV value
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = cap.read() # read each video frame
    #cv2.imshow('Trackbars', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converts BGR colour to HSV

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    # set upper and lower red values
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_red, upper_red) # identify red in frame

    #cv2.imshow("Frame", frame) # opens a window to show original video being captured


    resize = cv2.resize(mask, (960, 540))
    # draw on image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(resize, 'Colour Detection', (10, 500), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Mask", resize) # opens a window to show the mask

    key = cv2.waitKey(1)
    if key == 27:
        break

    #l_h = ("l_h", l_h)
    #l_s = ("l_s", l_s)
    #l_v = ("l_v", l_v)
    #u_h = ("u_h", u_h)
    #u_s = ("u_s", u_s)
    #u_v = ("u_v", u_v)

    # print HSV values to a text file called hsv
    hsv = str([l_h, l_s, l_v, u_h, u_s, u_v])
    f = open("hsv.txt", "w")
    f.write(hsv)
    f.close()


cap.release()
cv2.destroyAllWindows()
