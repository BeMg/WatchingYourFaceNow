import cv2
import numpy as np


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


img = cv2.imread('./data/media/0.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade_xml = []

cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt2.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_default.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt_tree.xml')

cascades = []

for i, xml in enumerate(cascade_xml):
    cascades.append(cv2.CascadeClassifier(xml))

rects = []

for cascade in cascades:
    rects.append(detect(gray, cascade))
    print(detect(gray, cascade))
draw(img, rects[0], (255, 0, 0))

cv2.imshow('aaa', img)
cv2.waitKey(0)