import cv2 as cv
import numpy as np
def get_histogram(gray_img):
    hist = np.zeros((256), dtype=np.uint32)
    for val in range(0,256):
        hist[val] = sum(sum(gray_img == val))
    return hist

def conv_hist2img(hist):
    img = np.full((256,256),255,dtype=np.uint8)
    max_freq = max(hist)
    for val in range(len(hist)):
        normalized_freq = int(hist[val] / max_freq * 255)
        img[0:normalized_freq, val] = 0
    return img[::-1,:]

if __name__ == '__main__':
    img = cv.imread('data/baboon.tif', cv.IMREAD_GRAYSCALE)

    hist = get_histogram(img)

    img_hist = conv_hist2img(hist)
    img_hist = cv.resize(img_hist, (len(img[0]), len(img_hist)))
    newimg = np.vstack([img,img_hist])

    cv.imshow('Histogram',newimg)
    cv.waitKey()
    cv.destroyAllWindows()