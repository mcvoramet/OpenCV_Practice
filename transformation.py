import cv2 as cv
import numpy as np


img = cv.imread('Mc_Com.JPG')
cv.imshow('Mc', img)

# Translation (translate along x and y axis)
def translate(img, x, y):
    transMat = np.float32(([1,0,x],[0,1,y]))
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x implied Left
# -y implied Up
# +x implied Rightg
# +y implied Down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing 
# Enlarging --> cv.INTER_LINEAR or cv.INTER_CUBIC(Slower but better) 
# Shrinking --> cv.INTER_AREA
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flipping
# 0 --> vertical flip
# 1 --> horizontal flip (Mirror)
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
