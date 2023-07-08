import cv2
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/90)
    height=int(frame.shape[0]* percent/90)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    image=rescale_frame(frame,percent=50)
    
    cv2.imshow('Original Size',frame)
    cv2.imshow('Resize',image)
    
    if cv2.waitKey(1)==ord('p'):
        break

cap.release()
cv2.destroyAllWindows()

