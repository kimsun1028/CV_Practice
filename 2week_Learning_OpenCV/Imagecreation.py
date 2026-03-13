import numpy as np
import cv2 as cv

img_gray = np.full((480,640), 255, dtype = np.uint8)
img_gray[140:240, 220:420] = 0
img_gray[240:340, 220:420] = 127

img_color = np.zeros((480,640,3), dtype = np.uint8)
img_color[:] = 255
img_color[140:240, 220:420, :] = (0,0,255)
img_color[240:340, 220:420, :] = (0,255,0)

cv.imshow('Gray Image', img_gray)
cv.imshow('Color Image', img_color)
cv.waitKey()
cv.destroyAllWindows()