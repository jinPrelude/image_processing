import numpy as np
import cv2
import sys
import os

recordStart = False
recordEnd = False

def onMouse(event, x, y, flags, param) :
    global recordStart, recordEnd
    if event == cv2.EVENT_LBUTTONDOWN :
        print('record start')
        recordStart = True

    elif event == cv2.EVENT_LBUTTONUP :

        recordStart = False
        recordEnd = True

def writeVideo(i) :

    global recordStart, recordEnd
    try :
        print('camera start')
        cap = cv2.VideoCapture(0)
        cap.set(3, 100)
        cap.set(4, 100)

    except :
        print('camera setting failed')


    j = 0
    while True :
        ret, frame = cap.read()

        if not ret :
            print('video reading error')
            break

        cv2.imshow('video', frame)
        cv2.setMouseCallback('video', onMouse)
        if recordStart:
            cv2.imwrite('eyeTrack_dataset/' + '%d'%i + '/%d.jpg'%j, frame)
            j += 1
        if cv2.waitKey(1) & 0xFF == ord('q') :
            sys.exit()
        elif recordEnd == True :
            print('finish record')
            recordEnd = False
            break


    cap.release()


    cv2.destroyAllWindows()

if __name__ == "__main__" :
    for i in range(1000) :
        os.system("mkdir eyeTrack_dataset/%d"%i)
        writeVideo(i)