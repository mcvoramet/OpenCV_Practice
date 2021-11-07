import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

early_DIR = '/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/PROJECT/Potato/Train/Potato___Early_blight'   # total 300 images
late_DIR = '/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/PROJECT/Potato/Train/Potato___Late_blight'     # total 300 images
healthy_DIR = '/Users/vorametchunvattananon/Desktop/Dev/OpenCV_Project/PROJECT/Potato/Train/Potato___healthy'      # total 300 images

def read_file(path):
    img_file_path = []
    for img in os.listdir(path):
        img_file_path.append(path + '/' + img)
    
    return img_file_path

early_img = read_file(early_DIR)
late_img = read_file(late_DIR)
healthy_img = read_file(healthy_DIR)

img = cv.imread(healthy_img[0])
cv.imshow('Potato', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)