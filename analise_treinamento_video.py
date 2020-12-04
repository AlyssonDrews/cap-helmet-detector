import cv2
import glob
import os
from datetime import datetime
import logging as log

car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
cap = cv2.VideoCapture(0)
date =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")
while True:
    _, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = car_cascade.detectMultiScale(gray, 1.6, 10)
        
    for (x,y,w,h) in objetos:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        if objetos.all():
            cv2.imwrite("logs/last_image.png", img)
            print("Suspeito detectado", date)
            

    cv2.imshow('Detector', img)
    k = cv2.waitKey(60)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()