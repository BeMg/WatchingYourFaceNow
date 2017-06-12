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


def face_cascade():
    cascade_xml = []

    cascade_xml.append('./data/haarcascades/mycascade.xml')
    cascade_xml.append('./data/haarcascades/haarcascade_frontalface_alt2.xml')
    cascade_xml.append(
        './data/haarcascades/haarcascade_frontalface_default.xml')
    cascade_xml.append(
        './data/haarcascades/haarcascade_frontalface_alt_tree.xml')

    cascades = []

    for i, xml in enumerate(cascade_xml):
        cascades.append(cv2.CascadeClassifier(xml))

    return cascades
