import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

early_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___Early_blight'
late_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___Late_blight'
healthy_DIR = r'/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/Potato/Train/Potato___healthy'

img_file_path = []

def read_file(path):
    for img in os.listdir(path):
        img_file_path.append(path + '/' + img)
    
    return img_file_path

img = read_file(early_DIR)

img = cv.imread(img[0])
cv.imshow('Potato', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)



