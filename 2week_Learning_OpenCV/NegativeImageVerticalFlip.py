import numpy as np
import cv2 as cv

img = cv.imread('data/peppers.tif')

if img is not None:
    img_nega = 255-img
    img_flip = img[::-1,:,:]
    merge=np.hstack((img, img_nega, img_flip))
    cv.imshow("Image Editing: Original | Negative | Flip", merge)
    cv.waitKey()
    cv.destroyAllWindows()