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
while True:
    flag, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detect(gray, cascades[1])
    #rects = [[75,0,565,100]]
    print(rects)
    if len(rects) > 0:
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
