import cv2 as cv

img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
# Number (7,7) the higher the number the more blur it get
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
# when try using more iterations the line get thicker
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

# Resize to 500x500 ignore the aspect ration
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# Resize to 500x500 with interpolation
resized_inter = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized with Interpolation', resized_inter)

# Cropping
cropped = img[20:400, 20:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

