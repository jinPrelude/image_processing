import numpy as np
import cv2

col, width, row, height = -1, -1, -1, -1
frame = None
frame2 = None
inputmode = False
rectangle = False
trackWindow = None
roi_hist = None

def onMouse(event, x, y, flags, param):
    global col, width, row, height, frame, frame2, inputmode
    global rectangle, roi_hist, trackWindow

    if inputmode :
        if event ==  cv2.EVENT_LBUTTONDOWN :
            rectangle = True
            col, row = x, y

        elif event == cv2.EVENT_MOUSEMOVE :
            if rectangle :
                frame = frame2.copy()
                cv2.rectangle(frame, (col, row), (x,y), (0, 255, 0), 2)
                cv2.imshow('frame', frame)

        elif event == cv2.EVENT_LBUTTONUP :
            inputmode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
            height, width = abs(row - y), abs(col - x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row+height, col:col+width]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            roi_hist = cv2.calcHist([roi], [0], None, [180], [0,180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return

def camShift() :
    global frame, frame2, inputmode, trackWindow, roi_hist

    try:
        cap = cv2.VideoCapture(0)
    except Exception as e :
        print(e)
        return

    ret, frame = cap.read()

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', onMouse, param=(frame, frame2))

    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    while True :
        ret, frame = cap.read()
        if not ret :
            break

        if trackWindow is not None :
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2. calcBackProject([hsv],[0], roi_hist, [0,180], 1)
            ret, trackWindow = cv2.meanShift(dst, trackWindow, termination)

            x, y, w, h = trackWindow
            cv2.rectangle(frame, (x, y), (x+h, y+w), (0,255,0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(60) & 0xFF == ord('q') :
            break

        if cv2.waitKey(60) & 0xFF == ord('i') :
            print("Select Area for camShift and Enter a key")
            inputmode = True
            frame2 = frame.copy()

            while inputmode :
                cv2.imshow('frame', frame)
                cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

camShift()