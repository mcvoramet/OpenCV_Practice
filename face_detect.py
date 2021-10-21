# haarcasscade is very sensitive to noise (not use widely in advance project)
# improve by trying adjust minNeighbors parameter

import cv2 as cv

img = cv.imread('Mc_Com.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

friends_img = cv.imread('friends.jpg')
friends_gray = cv.cvtColor(friends_img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
friends_faces_rect = haar_cascade.detectMultiScale(friends_gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found in Mc.JPG = {len(faces_rect)}')
print(f'Number of faces found in friends.jpg = {len(friends_faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

for (x,y,w,h) in friends_faces_rect:
    cv.rectangle(friends_img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.imshow('Detected Face of Friends', friends_img)

cv.waitKey(0)