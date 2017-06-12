import cv2
import numpy as np


def PolygonArea(corners):
    #n = len(corners) # of corners
    #print(corners)
    #print(corners.shape)
    l, m, n = corners.shape
    area = 0.0
    for i in range(l):
        j = (i + 1) % l
        area += corners[i][0][0] * corners[j][0][1]
        area -= corners[j][0][0] * corners[i][0][1]
    area = abs(area) / 2.0
    return area

def selectScreen(contours):
    x = np.array([[1, 2]])
    toReturn = contours[0]
    left = np.array([[]])
    right = np.array([[]])
    maxArea = -1.0
    for c in contours:
        area = PolygonArea(c)
        if(area > maxArea):
            maxArea = area
            toReturn = c
    #print(np.array_repr(toReturn).replace('\n', ''))
    l, m, n = toReturn.shape
    toReturn = toReturn.reshape(l, n)
    #print(np.array_repr(toReturn).replace('\n', ''))
    lx = 640
    ly = 480
    rx = -1
    ry = -1
    for i in toReturn:
        if(i[0] < lx): lx = i[0]
        if(i[1] < ly): ly = i[1]
        if(i[0] > rx): rx = i[0]
        if(i[1] > ry): ry = i[1]

    return c, [lx, ly], [rx, ry]



cap = cv2.VideoCapture('./data/media/3.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=20, detectShadows = False)


while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    print(fgmask)
    im2,contours,hierarchy = cv2.findContours(fgmask, 1, 2)
    screen, coordLeft, coordRight = selectScreen(contours)
    cv2.rectangle(frame, (coordLeft[0], coordLeft[1]), (coordRight[0], coordRight[1]), (0, 0, 255), 2)

    cv2.imshow('GGGG', frame)

    if cv2.waitKey(5) == 27:
        cap.release()