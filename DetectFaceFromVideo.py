import cv2
import numpy as np
from detectanddraw import detect, draw, face_cascade


cap = cv2.VideoCapture(0)
cascades = face_cascade()


while True:
    flag, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detect(gray, cascades[0])
    print(rects)
    if len(rects) > 0:
        draw(img, rects, (255, 0, 0))
    cv2.imshow('GGGG', img)

    if cv2.waitKey(5) == 27:
        cap.release()
