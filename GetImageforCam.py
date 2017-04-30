import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    flag, img = cap.read()
    cv2.imshow('GGGG', img)

    if cv2.waitKey(5) == 27:
        cap.release()
