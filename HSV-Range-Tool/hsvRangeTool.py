import cv2 as cv
import numpy as np

def kamera(x):
    pass

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cap=cv.VideoCapture(0)
cv.namedWindow('HSV Range Tool')
kernel=np.ones((5,5),np.uint8)

hl='Hue Low'
sl='Saturation Low'
vl='Value Low'
hh='Hue High'
sh='Saturation High'
vh='Value High'

cv.createTrackbar(hl,'HSV Range Tool',0,180,kamera)
cv.createTrackbar(sl,'HSV Range Tool',0,255,kamera)
cv.createTrackbar(vl,'HSV Range Tool',0,255,kamera)
cv.createTrackbar(hh,'HSV Range Tool',0,180,kamera)
cv.createTrackbar(sh,'HSV Range Tool',0,255,kamera)
cv.createTrackbar(vh,'HSV Range Tool',0,255,kamera)

while True:
    _,frame=cap.read()
    frame=rescale_frame(frame,percent=67.5)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    hul=cv.getTrackbarPos(hl,'HSV Range Tool')
    sal=cv.getTrackbarPos(sl,'HSV Range Tool')
    val=cv.getTrackbarPos(vl,'HSV Range Tool')
    huh=cv.getTrackbarPos(hh,'HSV Range Tool')
    sah=cv.getTrackbarPos(sh,'HSV Range Tool')
    vah=cv.getTrackbarPos(vh,'HSV Range Tool')

    hsv_low=np.array([hul,sal,val])
    hsv_high=np.array([huh,sah,vah])

    mask=cv.inRange(hsv,hsv_low,hsv_high)
    res=cv.bitwise_and(frame,frame,mask=mask)

    stacked=np.hstack((frame,res))
    cv.imshow('HSV Range Tool',stacked)

    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()