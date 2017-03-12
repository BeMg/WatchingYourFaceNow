import cv2
import numpy as np
from detectanddraw import detect, draw


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
