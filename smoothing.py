import cv2 as cv

img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

# Averaging Blur (higer kernel size -> more blur)
# cv.blur(img, kernel size)
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur (more natural compare to averaging)
gauss = cv.GaussianBlur(img, (9,9), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (not use much with high kernel size like 5 or 7)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (Most effective)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)