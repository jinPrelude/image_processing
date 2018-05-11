import cv2
import numpy as np

def video_threshold() :
    try :
        print('video initializing')
        cap = cv2.VideoCapture(0)
    except :
        print('video read error')

    cap.set(3, 100)
    cap.set(4, 100)


    while True :
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret2, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        thr2 = cv2.adaptiveThreshold(img, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)

        cv2.imshow('original', img)
        cv2.imshow('threshold', thr1)
        cv2.imshow('adaptive', thr2)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break


    cv2.destroyAllWindows()

video_threshold()