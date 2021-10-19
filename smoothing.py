import cv2 as cv

img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

# Averaging Blur (higer kernel size -> more blur)
# cv.blur(img, kernel size)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur (more natural compare to averaging)
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur 
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

cv.waitKey(0)