import cv2 as cv

img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding ( cv.threshold(gray, thresh, if pixel>thresh set value to maxval) )
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# Inverse Thresholding ( cv.threshold(gray, thresh, if pixel<thresh set value to maxval) )
threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholded', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Adaptive Thresholding (Inverse)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh)

# Adaptive Thresholding (Gaussian)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh)

cv.waitKey(0)

