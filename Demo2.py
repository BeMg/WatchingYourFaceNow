import RPi.GPIO as GPIO
import time
import sys
from array import *
import cv2
import numpy as np
from detectanddraw import detect, draw, face_cascade
from TurningWithDetect import Turn

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

clockwise = 1
steps = 180

ports = [29,31,33,35]
for p in ports:
    GPIO.setup(p,GPIO.OUT)

cap = cv2.VideoCapture(0)
cascades = face_cascade()

flag,img = cap.read()

roi = img 
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
rects = []
track = ()

while True:
    flag, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    if len(rects) == 0:
        rects = detect(gray, cascades[1])
    else:
        track = tuple(rects[0])
        ret, track = cv2.meanShift(dst, track, term_crit)
    print(list(track))
    if len(track) > 0:
        x,y,w,h = track
        img2 = cv2.rectangle(img, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)
    elif len(rects) > 0:
        draw(img, rects, (255, 0, 0))
    if(len(rects)>=1):
        if(rects[0][0]<75):
            Turn(2,1)
            print(11111)
        elif(rects[0][2]>565):
            Turn(2,0)
            print(22222)
    cv2.imshow('GGGG', img)

    if cv2.waitKey(5) == 27:
        cap.release()
