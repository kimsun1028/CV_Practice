import cv2 as cv
import numpy as np

video = cv.VideoCapture('data/PETS09-S2L1-raw.webm')

frame_count = 0
img_back = None
while True:
    valid, img = video.read()
    if not valid:
        break
    frame_count += 1

    if frame_count % 100 == 0:
        print(f'Frame: {frame_count}')

    if img_back is None:
        img_back = np.zeros_like(img, dtype=np.float64)
    img_back += img.astype(np.float64)
img_back = img_back / frame_count
img_back = img_back.astype(np.uint8)

cv.imwrite('data/PETS09-S2L1-raw_back.png', img_back)
cv.imshow('Background Extraction', img_back)
cv.waitKey()
cv.destroyAllWindows()