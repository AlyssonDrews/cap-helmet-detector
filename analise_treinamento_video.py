import cv2
import glob
import os, codecs, glob
from datetime import datetime
import logging as log
import face_recognition
import numpy as np


faces_encodings = []
faces_names = []
currentDir = os.getcwd()
path = os.path.join(currentDir, "faces/")
lista = [f for f in glob.glob(path+"*.JPG")]
list_length = len(lista)
names = lista.copy()

for i in range(list_length):
    presets = face_recognition.load_image_file(lista[i])
    encoding = face_recognition.face_encodings(presets)[0]
    faces_encodings.append(encoding)
    names[i] = names[i].replace(currentDir, "")
    names[i] = names[i].replace(".JPG", "")
    names[i] = names[i].replace("faces", "")
    faces_names.append(names[i])

face_locations = []
face_encodings = []
face_names = []


car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
cap = cv2.VideoCapture(0)
date =  datetime.now().strftime("%d/%m/%Y %H:%M:%S")


while True:
    _, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edge_image=cv2.Canny(gray,30,200)
    objetos = car_cascade.detectMultiScale(gray, 1.6, 9)
        
    smallFrame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgbSmallFrame = smallFrame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgbSmallFrame)
    face_encodings = face_recognition.face_encodings(
        rgbSmallFrame, face_locations)
    face_names = []

    for face in face_encodings:
        matches = face_recognition.compare_faces(faces_encodings, face)
        name = "Suspeito"
        face_distances = face_recognition.face_distance(faces_encodings, face)
        best_match = np.argmin(face_distances)
        if matches[best_match]:
            name = faces_names[best_match]
        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top = top * 4
        right = right * 4
        bottom = bottom * 4
        left = left * 4
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 1)
        cv2.rectangle(img, (left, bottom-35), (right, bottom), (0,0,255), cv2.FILLED)
        cv2.putText(img, name, (left+4, bottom-4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 1)


    for (x,y,w,h) in objetos:
        if name not in face_names:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            if objetos.all():
                cv2.imwrite("logs/last_image.png", img)
                logs = codecs.open("logs/logs.txt", 'w+', 'UTF-8')
                logs.write("Suspeito detectado "+date+"\n")
        logs = codecs.open("logs/logs_pessoa_conhecida.txt", 'w+', 'UTF-8')
        logs.write(name+" foi o ultimo funcionario a ser detectado " +date+"\n")

    cv2.imshow('Detector', img)
    cv2.imshow('Edge', edge_image)
    k = cv2.waitKey(60)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()