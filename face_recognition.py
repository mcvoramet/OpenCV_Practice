import numpy as np
import cv2 as cv
import os
import random

test_img = []
for img_file in os.listdir(r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/test_img_recognition'):
    test_img.append(img_file)

# randomly pick image for testing
random.shuffle(test_img)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Monica', 'Joey', 'Phoebe', 'Rachel', 'Ross', 'Chandler']
#features = np.load('features.npy', allow_pickle=True)
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(f'test_img_recognition/{test_img[0]}')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

person_name = test_img[0].split('_')[0]
cv.imshow(f'Expected Answer: {person_name.capitalize()}', img)

cv.waitKey(0)