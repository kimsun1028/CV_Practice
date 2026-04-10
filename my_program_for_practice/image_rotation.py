import numpy as np
import cv2 as cv

img = cv.imread('data/baboon.tif')

if img is None:
    raise FileNotFoundError('data/baboon.tif not found')

height = img.shape[0]
width = img.shape[1]

fmoveH = np.array([
    [1,0,-width/2],
    [0,1,-height/2],
    [0,0,1]
    ])

lmoveH = np.array([
    [1,0,width/2],
    [0,1,height/2],
    [0,0,1]])

theta = np.deg2rad(90)
H = np.array([
    [np.cos(theta),-np.sin(theta),0],
    [np.sin(theta),np.cos(theta),0],
    [0,0,1]
])

totalH  = lmoveH @ H @ fmoveH

img2 = np.zeros_like(img)

for y in range(height):
    for x in range(width):
        src = np.array([x, y, 1.0])
        dst = totalH @ src
        dst /= dst[2]
        
        # 새 좌표 계산
        x2 = int(round(dst[0]))
        y2 = int(round(dst[1]))

        if 0 <= x2 < width and 0 <= y2 < height:
            img2[y2, x2] = img[y, x]

cv.imshow('original', img)
cv.imshow('rotated', img2)
cv.waitKey(0)
cv.destroyAllWindows()

