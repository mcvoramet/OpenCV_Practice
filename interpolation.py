from img_extract_proj import read_file
import cv2 as cv
import numpy as np

healthy_DIR = 'Potato/Train/Potato___healthy'      # total 300 images

healthy_img = read_file(healthy_DIR)
img = cv.imread(healthy_img[0])
cv.imshow('Potato', img)

# Blur
# Number (7,7) the higher the number the more blur it get
blur = cv.GaussianBlur(img, (13,13), 0)
cv.imshow('Blur', blur)

gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold = 150
threshold, thresh = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)
cv.imshow('Binary', thresh)

mask = np.zeros((3,3), dtype='uint8')
print(mask)



cv.waitKey(0)