import numpy as np
import cv2 as cv

img = cv.imread('data/baboon.tif')

if img is None:
    raise FileNotFoundError('data/baboon.tif not found')
height, width = img.shape[:2]


img2 = np.zeros((height, 2*width,3), dtype = img.dtype) 

for x in range(width):
    for y in range(height):
        img2[y,2*x] = img[y,x]
        img2[y,2*x+1] = img[y,x]
cv.imshow('original', img)
cv.imshow('rotated', img2)
cv.waitKey(0)
cv.destroyAllWindows()
