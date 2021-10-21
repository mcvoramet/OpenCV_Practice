import cv2 as cv
import numpy as np

img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)  # there are an negative value occur here (actually picture can't have negative)
lap = np.uint8(np.absolute(lap)) # that's why we transform it with absolute
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) 
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel =  cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)