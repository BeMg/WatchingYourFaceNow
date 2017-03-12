import cv2
import numpy as np
from detectanddraw import detect, draw, face_cascade


img = cv2.imread('./data/media/0.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascades = face_cascade()

rects = []

for cascade in cascades:
    rects.append(detect(gray, cascade))
    print(detect(gray, cascade))
draw(img, rects[0], (255, 0, 0))

cv2.imshow('aaa', img)
cv2.waitKey(0)
