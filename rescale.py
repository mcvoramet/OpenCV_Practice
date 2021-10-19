import cv2 as cv

# Work with all Images, Videos, Live Videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# change resolution of Live video (not work on normal video and images)
def changeRes(width, height):
   # Live Video
    # 3 reference the width
    capture.set(3, width)
    # 4 reference the height
    capture.set(4, height)

capture = cv.VideoCapture('วิธีปรุงน้ำผัดหมี่.mp4')

while True:
    # Read frame by frame (Return frame and boolean to tell whether the reading success or not)
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    # If the letter 'd' is press then break out of the loop and stop display
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capture devices and destroy all windows cause we don't need them anymore
capture.release() 
cv.destroyAllWindows()