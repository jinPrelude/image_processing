import cv2
import numpy as np

def bitOperation(hpos, vpos) :
    img1 = cv2.imread("pictures/elon_musk.jpg")
    img2 = cv2.imread("pictures/openai.png")
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    dst = cv2.add(img1_bg, img2_fg)

    img1[vpos:rows+vpos, hpos:cols+hpos] = dst
    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(hpos=10,vpos=10)