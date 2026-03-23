
import cv2 as cv
import numpy as np

kernel_table = [
    {'name': 'Box 3x3',         'kernel': np.ones((3, 3)) / 9},   # Alternative: cv.boxFilter(), cv.blur()
    {'name': 'Gaussian 3x3',    'kernel': np.array([[1, 2, 1],    # Alternative: cv.GaussianBlur()
                                                    [2, 4, 2],
                                                    [1, 2, 1]]) / 16},
    {'name': 'Box 5x5',         'kernel': np.ones((5, 5)) / 25},
    {'name': 'Gaussian 5x5',    'kernel': np.array([[1,  4,  6,  4, 1],
                                                    [4, 16, 24, 16, 4],
                                                    [6, 24, 36, 24, 6],
                                                    [4, 16, 24, 16, 4],
                                                    [1,  4,  6,  4, 1]]) / 256},
    {'name': 'Gradient X',      'kernel': np.array([[-1,  1]])},
    {'name': 'Robert DownRight','kernel': np.array([[-1,  0],
                                                    [ 0,  1]])},
    {'name': 'Prewitt X',       'kernel': np.array([[-1,  0,  1],
                                                    [-1,  0,  1],
                                                    [-1,  0,  1]])},
    {'name': 'Sobel X',         'kernel': np.array([[-1,  0,  1], # Alternative: Sobel()
                                                    [-2,  0,  2],
                                                    [-1,  0,  1]])},
    {'name': 'Scharr X',        'kernel': np.array([[-3,  0,  3], # Alternative: Scharr()
                                                    [-10, 0, 10],
                                                    [-3,  0,  3]])},
    {'name': 'Gradient Y',      'kernel': np.array([[-1], [1]])},
    {'name': 'Robert UpRight',  'kernel': np.array([[ 0,  1],
                                                    [-1,  0]])},
    {'name': 'Prewitt Y',       'kernel': np.array([[-1, -1, -1],
                                                    [ 0,  0,  0],
                                                    [ 1,  1,  1]])},
    {'name': 'Sobel Y',         'kernel': np.array([[-1, -2, -1],
                                                    [ 0,  0,  0],
                                                    [ 1,  2,  1]])},
    {'name': 'Scharr Y',        'kernel': np.array([[-3,-10, -3],
                                                    [ 0,  0,  0],
                                                    [ 3, 10,  3]])},
    {'name': 'Laplacian (4)',   'kernel': np.array([[ 0, -1,  0], # Alternative: Laplacian
                                                    [-1,  4, -1],
                                                    [ 0, -1,  0]])},
    {'name': 'Laplacian (8)',   'kernel': np.array([[-1, -1, -1],
                                                    [-1,  8, -1],
                                                    [-1, -1, -1]])},
    {'name': 'Sharpen (5)',     'kernel': np.array([[ 0, -1,  0],
                                                    [-1,  5, -1],
                                                    [ 0, -1,  0]])},
    {'name': 'Sharpen (9)',     'kernel': np.array([[-1, -1, -1],
                                                    [-1,  9, -1],
                                                    [-1, -1, -1]])},
    {'name': 'Emboss (0)',      'kernel': np.array([[-2, -1,  0],
                                                    [-1,  0,  1],
                                                    [ 0,  1,  2]])},
    {'name': 'Emboss (1)',      'kernel': np.array([[-2, -1,  0],
                                                    [-1,  1,  1],
                                                    [ 0,  1,  2]])},
]


img_list = ['data/lena.tif']
kernel_select = 0
img_select = 0

while True:
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)

    name, kernel = kernel_table[kernel_select].values()
    result = cv.filter2D(img, -1, kernel)

    merge = np.hstack((img,result))
    cv.imshow('Image Filtering',merge)

    cv.waitKey()