import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    #capture frame by frame
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('rgb picture', frame)        # show rgb image
    cv2.imshow('gray_scale_video',gray)     #show a grayscale image

    if cv2.waitKey(20) and 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
