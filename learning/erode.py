import numpy as np
import cv2

def morph() :
    img = cv2.imread('pictures/openai.png', cv2.IMREAD_GRAYSCALE)
    thr = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
    cv2.imshow('threshold', thr)
    kernal = np.ones((3,3), np.uint8)
    erosion = cv2.erode(thr, kernal, iterations=1)

    cv2.imshow('erosion', erosion)

    dilation = cv2.dilate(thr, kernal, iterations=1)

    cv2.imshow('dilation', dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()