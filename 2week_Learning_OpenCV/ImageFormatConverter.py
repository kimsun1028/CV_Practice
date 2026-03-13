import cv2 as cv
img_file = 'data/peppers.tif'
target_format = 'png'

img = cv.imread(img_file)

if img is not None:
    target_file = img_file[:img_file.rfind('.')] + '.' + target_format
    cv.imwrite(target_file, img)