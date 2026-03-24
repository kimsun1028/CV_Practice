import numpy as np
import cv2 as cv

img = cv.imread('data/salt_and_pepper.png')

kernel_size = 5
img_select = -1

while True:
    result = cv.medianBlur(img,kernel_size)

    merge = np.hstack((img,result))

    cv.imshow('image',merge)
    key = cv.waitKey()
    if key == 27:
        break
cv.destroyAllWindows()