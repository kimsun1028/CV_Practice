import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('data/baboon.tif',cv.IMREAD_GRAYSCALE)

img_tran = cv.equalizeHist(img)

bin_width = 4
bin_num = int(256/bin_width)
hist = cv.calcHist([img],[0],None, [bin_num],[0,255])
hist_tran = cv.calcHist([img_tran],[0],None, [bin_num],[0,255])

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(2,2,2)
plt.plot(range(0,256,bin_width), hist / 1000)
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(2,2,3)
plt.imshow(img_tran, cmap='gray')
plt.axis('off')
plt.subplot(2,2,4)
plt.plot(range(0,256,bin_width), hist_tran / 1000)
plt.xlabel('x')
plt.ylabel('y')
plt.show()