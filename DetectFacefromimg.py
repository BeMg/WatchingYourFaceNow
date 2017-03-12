import cv2
import numpy as np


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


img = cv2.imread('./data/media/0.jpg', 0)

cascade_xml = []

cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt2.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_default.xml')
cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt_tree.xml')
cascade_xml.append('./data/haarcascades/haarcascade_fullbody.xml')

cascades = []

for i, xml in enumerate(cascade_xml):
    cascades.append(cv2.CascadeClassifier(xml))

for i, cascade in enumerate(cascades):
    rects = detect(img, cascade)
    print("{}: {}".format(i, rects))
