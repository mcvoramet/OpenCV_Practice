import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

early_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___Early_blight'
late_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___Late_blight'
healthy_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___healthy'

early_blight = []
late_blight = []
healthy = []

for file in os.listdir(early_DIR):
    early_blight.append(file)

for file in os.listdir(late_DIR):
    late_blight.append(file)

for file in os.listdir(healthy_DIR):
    healthy.append(file)

img = cv.imread(early_DIR + '/' + early_blight[1])
cv.imshow('test', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)



cv.waitKey(0)

