import numpy as np
import cv2 as cv
from Image_Histogram import get_histogram, conv_hist2img
img = cv.imread('data/baboon.tif', cv.IMREAD_GRAYSCALE)


value_range = [20, 200]

while True:
    img_tran = 255 / (value_range[1] - value_range[0]) * (img.astype(np.int32) - value_range[0])
    img_tran = img_tran.astype(np.uint8)

    hist = conv_hist2img(get_histogram(img))
    hist_tran = conv_hist2img(get_histogram(img_tran))
    # cliping 안됨!!!!!
    if value_range[0] >= 0 and value_range[0] <= 255:
        mark = hist[:,value_range[0]] == 255
        hist[mark, value_range[0]] == 200

    if value_range[1] >= 0 and value_range[1] <= 255:
        mark = hist[:,value_range[1]] == 255
        hist[mark, value_range[1]] = 100

    hist = cv.resize(hist, (len(img[0]), len(hist)))
    hist_tran = cv.resize(hist_tran, (len(img_tran[0]), len(hist_tran)))
    img_0 = np.vstack((img,hist))
    img_1 = np.vstack((img_tran,hist_tran))
    
    full_img = np.hstack((img_0,img_1))

    cv.imshow('Constrast Stretching',full_img)
    key = cv.waitKey()