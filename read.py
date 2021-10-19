import cv2 as cv

'''
# Reading Images
img = cv.imread('Mc_Com.JPG')
cv.imshow("Mc", img)

# Press anykey to exit the code
cv.waitKey(0)
'''

# Reading Videos
capture = cv.VideoCapture('วิธีปรุงน้ำผัดหมี่.mp4')

while True:
    # Read frame by frame (Return frame and boolean to tell whether the reading success or not)
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # If the letter 'd' is press then break out of the loop and stop display (20 is in Milliseconds)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capture devices and destroy all windows cause we don't need them anymore
capture.release() 
cv.destroyAllWindows()
 