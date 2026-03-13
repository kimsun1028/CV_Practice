import cv2 as cv
img_file = 'data/peppers.tif'

img = cv.imread(img_file)

if img is not None:
    cv.imshow('Image Viewer',img)
    cv.waitKey()
    cv.destroyAllWindows()