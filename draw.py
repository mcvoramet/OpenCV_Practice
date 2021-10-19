import cv2 as cv
import numpy as np

# [Height, Width, Color Channel]
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour 
#blank[:] = 0,255,0    # R, G, B
#cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.FILLED or -1 is use for filling the space with that color 
# or you can use number like 2 on thickness to specify it as a line
cv.rectangle(blank, (0,0), (250, 250), (0,255,0), thickness=cv.FILLED)   
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
# 40 is the radius
cv.circle(blank, (250, 250), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (100,150), (250, 250), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write Text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text', blank)

cv.waitKey(0)