import cv2 as cv

I = cv.imread('Mc_Com.JPG')
gray = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

eq_img = cv.equalizeHist(gray)
cv.imshow('Gray Image', gray)
cv.imshow('Equalize Image',eq_img)

cv.waitKey(0)