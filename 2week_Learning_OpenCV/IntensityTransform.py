import cv2 as cv
import numpy as np
img = cv.imread('data/baboon.tif',cv.IMREAD_GRAYSCALE)

if img is not None:
    contrast = 1.6
    contrast_step=0.1
    brightness = -40
    brightness_step = 1

    while True:
        img_tran = contrast * img + brightness
        img_tran[img_tran < 0] = 0
        img_tran[img_tran > 255] = 255
        img_tran = img_tran.astype(np.uint8)

        merge = np.hstack([img,img_tran])
        cv.imshow("image viewer",merge)

        key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('+') or key == ord('='):
            contrast += contrast_step
        elif key == ord('-'):
            contrast -= contrast_step
        elif key == ord(']'):
            brightness += brightness_step
        elif key == ord('['):
            brightness -= brightness_step
