<<<<<<< HEAD
import os, glob
import numpy as np
import cv2
import matplotlib.pyplot as plt  
from skimage.color import rgb2hsv



def run_histogram_equalization(image):
    """
    Process enhanceg image by image equlizehist, by convert to Color domain that has an intensity and enhance then convert back
    
    """
    rgb_img = image
    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    return equalized_img

def hsvfilter(image):
    """
    hsvfilter: Roughly remove filter base on HSV domain range (. . . - 0.45)

    input :
    image = input as color BGR image (cv2 default)
    
    output :
    segim = image with roughly segmentation
    
    """
    image = cv2.GaussianBlur(image, (5, 5), 0)
    enhimage = run_histogram_equalization(image)
    rgbim = cv2.cvtColor(enhimage, cv2.COLOR_BGR2RGB)
    hsvim = rgb2hsv(rgbim)

    #fig, ax = plt.subplots(1, 3, figsize=(15,5))
    #ax[0].imshow(hsvim[:,:,0], cmap='hsv')
    #ax[0].set_title('Hue',fontsize=15)

    #plt.show()


    #create mask by select range that color can pass

    lower_hmask = hsvim[:, :, 0] > 0.03
    upper_hmask = hsvim[:, :, 0] < 0.45
    mask = upper_hmask*lower_hmask

    #Segmented:
    red = rgbim[:,:,0]*mask
    green = rgbim[:,:,1]*mask
    blue = rgbim[:,:,2]*mask
    hsvsegim = np.dstack((red,green,blue))

    grayim = cv2.cvtColor(hsvsegim, cv2.COLOR_RGB2GRAY)

    for x in range(hsvsegim.shape[0]):
        for y in range(hsvsegim.shape[1]):
            grayim[x, y] = 255 if grayim[x, y] != 0 else 0

    segim = grayim


    return segim

def clearborder(orgim,imgBW):

    """
    Receive input as BW image and clear border with morphological reconstruction:
    
    """

    #kernel = np.ones((7,7),np.uint8)
    kernel2 = np.ones((3,3),np.uint8)
    marker = imgBW.copy()
    marker[1:-1,1:-1]=0
    while True:
        tmp=marker.copy()
        marker=cv2.dilate(marker, kernel2)
        marker=cv2.min(imgBW, marker)
        difference = cv2.subtract(marker, tmp)
        if cv2.countNonZero(difference) == 0:
            break

    mask=cv2.bitwise_not(marker)
    mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    out=cv2.bitwise_and(orgim, mask_color)

    grayim = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)

    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            grayim[x, y] = 255 if grayim[x, y] != 0 else 0

    segim = grayim
    return segim


def flood_fill(orgim, hsvim):

    """
    What floodFill() does is connects a pixel to it's neighbors if the neighbors are within some
    threshold difference of the pixel. Four-way connectivity checks the neighbors above and below, and
    to the left and right. Eight-way connectivity checks the diagonal pixels in addition. This means that
    at border pixels, you either need a bunch of if statements to not check the pixels outside the
    border, OR, you can simply pad the image with one pixel on each side so that you don't need
    special cases, which both reads better in code and is faster. (Ref : stack overflow)

    input : hsvim(BW image) = An image that was roughly by hsv color domain filter

    output : hsvfillhole = Fill the hole where hsvim leave

    """
    
    im_flood_fill = hsvim.copy()
    height, width = hsvim.shape[:2]
   
    # Create mask to specify where region need to focus : 
    mask = np.zeros((height+2, width + 2), np.uint8)
    im_flood_fill = im_flood_fill.astype("uint8")

    #Fill the hole in the image
    cv2.floodFill(im_flood_fill, mask, (0, 0), 255)
    im_fllod_fill_inv = cv2.bitwise_not(im_flood_fill)

    imclearborder = clearborder(orgim, im_fllod_fill_inv)

    testim = im_fllod_fill_inv & imclearborder
    fillholeim = hsvim | testim


    #cv2.imshow("Windows_floodfill", fillholeim)
    #cv2.waitKey(0)


    return fillholeim

def smoothimg(image):
    """
    Finally, in order to make the segmented object look natural, smooth the object by eroding the image for a sharpening edge and clear undesirable noise
    Use kernel as elipse shape depend on an average shape of noise

    - Erodes away the boundaries of the foreground object
    - Used to diminish the features of an image.

    input : image that passing through HSV filter and Fill the hole (BW image)

    output : image with denoise and sharpen the edge
    """

    mask_size = (5 ,5)

    #Elipse Kernel : 
    mask_shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,mask_size)

    imerosion = cv2.erode(image, mask_shape, iterations = 2)


    return imerosion


def leafsegmented(OriginalImage):
    """
    1.) Remove the image background by focusing on a Hue Color range (0.03 - 0.45)
    2.) Fill in the empty hole in ROI(Region of Interest)
    3.) Denoise and shapen the edge
    4.) Segmented by : Segmented image = OriginalImage * BWimage(from step 3)
    
    input : Original Image = image as RGB format
          : Bwimage = binary image that passing through a preprocessing

    output : SegmentedImage = image with remove background :
    """
    hsvsegim = hsvfilter(OriginalImage)

    imfillhole = flood_fill(OriginalImage, hsvsegim)
    bwimage = smoothimg(imfillhole)

    bwimage = bwimage.astype("uint8")
    #bwimage = ~bwimage
    

    #rgbim = cv2.cvtColor(OriginalImage, cv2.COLOR_BGR2RGB)
    red = OriginalImage[:,:,0] & bwimage
    green = OriginalImage[:,:,1] & bwimage
    blue = OriginalImage[:,:,2] & bwimage
    segim = np.dstack((red,green,blue))


    #cv2.imshow("Image Segmented",segim )
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return segim




=======
import os, glob
import numpy as np
import cv2
import matplotlib.pyplot as plt  
from skimage.color import rgb2hsv



def run_histogram_equalization(image):
    """
    Process enhanceg image by image equlizehist, by convert to Color domain that has an intensity and enhance then convert back
    
    """
    rgb_img = image
    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    return equalized_img

def hsvfilter(image):
    """
    hsvfilter: Roughly remove filter base on HSV domain range (. . . - 0.45)

    input :
    image = input as color BGR image (cv2 default)
    
    output :
    segim = image with roughly segmentation
    
    """
    image = cv2.GaussianBlur(image, (5, 5), 0)
    enhimage = run_histogram_equalization(image)
    rgbim = cv2.cvtColor(enhimage, cv2.COLOR_BGR2RGB)
    hsvim = rgb2hsv(rgbim)

    #fig, ax = plt.subplots(1, 3, figsize=(15,5))
    #ax[0].imshow(hsvim[:,:,0], cmap='hsv')
    #ax[0].set_title('Hue',fontsize=15)

    #plt.show()


    #create mask by select range that color can pass

    lower_hmask = hsvim[:, :, 0] > 0.03
    upper_hmask = hsvim[:, :, 0] < 0.45
    mask = upper_hmask*lower_hmask

    #Segmented:
    red = rgbim[:,:,0]*mask
    green = rgbim[:,:,1]*mask
    blue = rgbim[:,:,2]*mask
    hsvsegim = np.dstack((red,green,blue))

    grayim = cv2.cvtColor(hsvsegim, cv2.COLOR_RGB2GRAY)

    for x in range(hsvsegim.shape[0]):
        for y in range(hsvsegim.shape[1]):
            grayim[x, y] = 255 if grayim[x, y] != 0 else 0

    segim = grayim


    return segim

def clearborder(orgim,imgBW):

    """
    Receive input as BW image and clear border with morphological reconstruction:
    
    """

    #kernel = np.ones((7,7),np.uint8)
    kernel2 = np.ones((3,3),np.uint8)
    marker = imgBW.copy()
    marker[1:-1,1:-1]=0
    while True:
        tmp=marker.copy()
        marker=cv2.dilate(marker, kernel2)
        marker=cv2.min(imgBW, marker)
        difference = cv2.subtract(marker, tmp)
        if cv2.countNonZero(difference) == 0:
            break

    mask=cv2.bitwise_not(marker)
    mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    out=cv2.bitwise_and(orgim, mask_color)

    grayim = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)

    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            grayim[x, y] = 255 if grayim[x, y] != 0 else 0

    segim = grayim
    return segim


def flood_fill(orgim, hsvim):

    """
    What floodFill() does is connects a pixel to it's neighbors if the neighbors are within some
    threshold difference of the pixel. Four-way connectivity checks the neighbors above and below, and
    to the left and right. Eight-way connectivity checks the diagonal pixels in addition. This means that
    at border pixels, you either need a bunch of if statements to not check the pixels outside the
    border, OR, you can simply pad the image with one pixel on each side so that you don't need
    special cases, which both reads better in code and is faster. (Ref : stack overflow)

    input : hsvim(BW image) = An image that was roughly by hsv color domain filter

    output : hsvfillhole = Fill the hole where hsvim leave

    """
    
    im_flood_fill = hsvim.copy()
    height, width = hsvim.shape[:2]
   
    # Create mask to specify where region need to focus : 
    mask = np.zeros((height+2, width + 2), np.uint8)
    im_flood_fill = im_flood_fill.astype("uint8")

    #Fill the hole in the image
    cv2.floodFill(im_flood_fill, mask, (0, 0), 255)
    im_fllod_fill_inv = cv2.bitwise_not(im_flood_fill)

    imclearborder = clearborder(orgim, im_fllod_fill_inv)

    testim = im_fllod_fill_inv & imclearborder
    fillholeim = hsvim | testim


    #cv2.imshow("Windows_floodfill", fillholeim)
    #cv2.waitKey(0)


    return fillholeim

def smoothimg(image):
    """
    Finally, in order to make the segmented object look natural, smooth the object by eroding the image for a sharpening edge and clear undesirable noise
    Use kernel as elipse shape depend on an average shape of noise

    - Erodes away the boundaries of the foreground object
    - Used to diminish the features of an image.

    input : image that passing through HSV filter and Fill the hole (BW image)

    output : image with denoise and sharpen the edge
    """

    mask_size = (5 ,5)

    #Elipse Kernel : 
    mask_shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,mask_size)

    imerosion = cv2.erode(image, mask_shape, iterations = 2)


    return imerosion


def leafsegmented(OriginalImage):
    """
    1.) Remove the image background by focusing on a Hue Color range (0.03 - 0.45)
    2.) Fill in the empty hole in ROI(Region of Interest)
    3.) Denoise and shapen the edge
    4.) Segmented by : Segmented image = OriginalImage * BWimage(from step 3)
    
    input : Original Image = image as RGB format
          : Bwimage = binary image that passing through a preprocessing

    output : SegmentedImage = image with remove background :
    """
    hsvsegim = hsvfilter(OriginalImage)

    imfillhole = flood_fill(OriginalImage, hsvsegim)
    bwimage = smoothimg(imfillhole)

    #Prevent from do nothings  : 
    w, h = bwimage.shape[:2]
    if cv2.countNonZero(bwimage) < ((w*h)*0.1):
        bwimage = hsvfilter(OriginalImage)

    bwimage = bwimage.astype("uint8")
    #bwimage = ~bwimage
    

    #rgbim = cv2.cvtColor(OriginalImage, cv2.COLOR_BGR2RGB)
    red = OriginalImage[:,:,0] & bwimage
    green = OriginalImage[:,:,1] & bwimage
    blue = OriginalImage[:,:,2] & bwimage
    segim = np.dstack((red,green,blue))


    #cv2.imshow("Image Segmented",segim )
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return segim


if __name__ == "__main__":

    Datadir = "C:/Users/acer/Desktop/EIE461_IMG_proc/PlantVillage-Dataset/Potato/Train/Potato___Late_blight/*jpg"

    path = glob.glob(Datadir)
    cv_img = []
    for img in path:
        n = cv2.imread(img)
        cv_img.append(n)

    #for i in range(len(cv_img)):

    rmbgIm = leafsegmented(cv_img[138])
    cv2.imshow("Image Segmented",rmbgIm )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


>>>>>>> 8cd2c7af94268ebdd5f2f34eb3ad2a54d395376b
