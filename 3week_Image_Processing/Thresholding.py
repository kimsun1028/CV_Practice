import numpy as np
import cv2 as cv

def drawText(img, text, org=(10, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.6, color=(0, 0, 0), colorBoundary=(255, 255, 255)):
    cv.putText(img, text, org, fontFace, fontScale, colorBoundary, thickness=2)
    cv.putText(img, text, org, fontFace, fontScale, color)

img = cv.imread('data/sudoku.png',cv.IMREAD_GRAYSCALE)
img_threshold_type = cv.THRESH_BINARY_INV

threshold = 127
adaptive_type = cv.ADAPTIVE_THRESH_MEAN_C
adaptive_blocksize = 99
adaptive_C = 4

while True:
    _, binary_user = cv.threshold(img,threshold,255,img_threshold_type)
    threshold_otsu, binary_otsu = cv.threshold(img, threshold, 255, img_threshold_type | cv.THRESH_OTSU)
    binary_adaptive = cv.adaptiveThreshold(img,255, adaptive_type, img_threshold_type, adaptive_blocksize, adaptive_C)

   
    drawText(binary_user, f'Threshold: {threshold}')
    drawText(binary_otsu, f'Otsu Threshold: {threshold_otsu}')
    adaptive_type_text = 'M' if adaptive_type == cv.ADAPTIVE_THRESH_MEAN_C else 'G'
    drawText(binary_adaptive, f'Type: {adaptive_type_text}, BlockSize: {adaptive_blocksize}, C: {adaptive_C}')
    merge = np.vstack((np.hstack((img, binary_user)),
                       np.hstack((binary_otsu, binary_adaptive))))
    cv.imshow('Thresholding: Original | User | Otsu | Adaptive', merge)

    # Process the key event
    key = cv.waitKey()

    cv.destroyAllWindows()