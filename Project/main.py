import utils
import create
import cv2
import math
import time
import texttospeech

is_talking = True

vc = cv2.VideoCapture(1)
width = 0
height = 0
r = create.Create(3)  # create robot

def openCVFunction():
    vc.read()
    rval, frame = vc.read()  # frame is color image

    frame = cv2.medianBlur(frame, 21)
    cv2.imshow("blur", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # make into gray-scale

    threshst, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY);
    cv2.imshow("grey", gray)
    cv2.imshow("thresh", thresh)

    canny = cv2.Canny(thresh, 100, 300, 3)  # perform canny edge detection

    hough = cv2.HoughLines(canny, 1, math.pi / 180, 70)  # convert edges into lines

    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 50,
                               param1=50, param2=30, minRadius=55, maxRadius=100)
    ### Circle Detection



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


    if circles is not None:
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow("frame", frame)  # draw frame with line drawn    cv2.imshow("edge", canny_color)


    return average_angles, circles

start_moving = False
time = 0
last_turn = [0 for x in range(0)]
index = 0
while True:
    time += 1
    average_angles, circles = openCVFunction()
    left = 0;
    right = 0;
    if circles is not None:
        for circle in circles[0]:
            if circle[0] > int(vc.get(3)/2):
                right += 1
            else:
                left += 1

    #print time, start_moving, [x for x in average_angles], "-- ", len(circles[0]) if circles is not None else " - no circles ", left, right
    key = cv2.waitKey(20)
    #print key


    sensors = r.sensors()
    if key == 32:
        r.stop()
        start_moving = not start_moving

    turning = (average_angles[0] if (average_angles[1] < 90) else -average_angles[0])
    last_turn.append(turning)

    if start_moving:
        trn = 0.75*last_turn[0]
        fwd = abs(15 - 10 * (abs(trn)/90))
        print fwd, trn
        r.go(fwd, trn)
        print fwd, trn
        #r.turn(trn/2, 20)
    last_turn = last_turn[1:]

    #    print " ".join([str(x) for x in last_turn])

    if is_talking and circles is not None and len(circles) > 0:
        r.move(25, 0)
        texttospeech.say(index)
        index += 1
        if(index > 3):
            break
        r.stop()


    if key == 27: # exit on ESC
        break

r.stop()d
r.close()
