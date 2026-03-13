import numpy as np
import cv2 as cv

img1 = cv.imread('data/baboon.tif')
img2 = cv.imread('data/peppers.tif')

if img1 is not None and img2 is not None:
    alpha = 0.5

    while True:
        blend = (alpha * img1 + (1-alpha)*img2).astype(np.uint8)
        info = f'Alpha = {alpha:.1f}'
        merge = np.hstack((img1,img2,blend))
        cv.imshow('Image Blending',merge)

        key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('+'):
            alpha = min(alpha + 0.1,1)
        elif key == ord('-'):
            alpha = max(alpha - 0.1, 0)
    cv.destroyAllWindows()