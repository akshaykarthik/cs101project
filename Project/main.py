import utils

import numpy as np
import cv2
import math
import time
import operator

vc = cv2.VideoCapture(0)


def round_to(x, base=5):
    return int(base * round(float(x) / base))


def openCVFunction():
    rval, frame = vc.read()  # frame is color image

    ### Line Detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # make into gray-scale
    canny = cv2.Canny(gray, 100, 300, 3)  # perform canny edge detection
    canny_color = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    hough = cv2.HoughLines(canny, 1, math.pi / 180, 125)  # convert edges into lines

    if hough is not None:  # while we have lines
        angle_data = []
        for rho, theta in hough[0]:
            angle_data.append((abs(theta - math.pi / 2) - math.pi / 2, theta, rho))  # set the angle data

            # project lines that go out 1000 pixels in each direction
            pt1, pt2 = utils.rtToPts(rho, theta)
            # draw the line on the color image
            cv2.line(frame, pt1, pt2, (255, 32, 32), 5)

        angle_data.sort()  # sort by angles
        angle_data = map(lambda (x, y, z): (int(x * 180 / math.pi), int(y * 180 / math.pi), z),
                         angle_data)  # map deg to rads
        average_angles = [sum(x) / len(angle_data) for x in zip(*angle_data)]  # find average angles

    else:
        average_angles = [0, 0]

    width, height = int(vc.get(3)), int(vc.get(4))  # width/height of webcam image
    cv2.line(frame, (width / 2, 0), (width / 2, height), (32, 32, 255), 5)  # draw red line

    ### Circle Detection

    img = cv2.medianBlur(gray, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 100,
                               param1=60, param2=30, minRadius=15, maxRadius=100)

    if circles is not None:
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow("frame", frame)  # draw frame with line drawn    cv2.imshow("edge", canny_color)

    return average_angles


while True:  #each turn
    average_angles = openCVFunction()
    print [round_to(x) for x in average_angles]
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break;
