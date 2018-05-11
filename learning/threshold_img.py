import cv2
import numpy as np

img = cv2.imread('pictures/elon_musk.jpg', cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('original', img)
cv2.imshow('threshold', thr1)

cv2.waitKey(0)
cv2.destroyAllWindows()