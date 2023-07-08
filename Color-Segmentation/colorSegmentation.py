import cv2 as cv
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cap=cv.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=rescale_frame(frame,percent=47)
    cv.rectangle(frame,(0,0),(150,30),(255,255,255),-1)
    frame=cv.putText(frame,"Original Image",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    lower_blue=np.array([90,170,160])
    upper_blue=np.array([130,255,255])
    mask_blue=cv.inRange(hsv,lower_blue,upper_blue)
    res_blue=cv.bitwise_and(frame,frame,mask=mask_blue)
    cv.rectangle(res_blue,(0,0),(150,30),(255,255,255),-1)
    res_blue=cv.putText(res_blue,"Blue Color",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_green=np.array([60,170,160])
    upper_green=np.array([80,255,255])
    mask_green=cv.inRange(hsv,lower_green,upper_green)
    res_green=cv.bitwise_and(frame,frame,mask=mask_green)
    cv.rectangle(res_green,(0,0),(150,30),(255,255,255),-1)
    res_green=cv.putText(res_green,"Green Color",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_red=np.array([0,35,210])
    upper_red=np.array([10,255,255])
    mask_red=cv.inRange(hsv,lower_red,upper_red)
    res_red=cv.bitwise_and(frame,frame,mask=mask_red)
    cv.rectangle(res_red,(0,0),(150,30),(255,255,255),-1)
    res_red=cv.putText(res_red,"Red Color",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    lower_yellow=np.array([20,0,240])
    upper_yellow=np.array([80,255,255])
    mask_yellow=cv.inRange(hsv,lower_yellow,upper_yellow)
    res_yellow=cv.bitwise_and(frame,frame,mask=mask_yellow)
    cv.rectangle(res_yellow,(0,0),(150,30),(255,255,255),-1)
    res_yellow=cv.putText(res_yellow,"Yellow Color",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)

    lower_purple=np.array([140,20,160])
    upper_purple=np.array([160,255,255])
    mask_purple=cv.inRange(hsv,lower_purple,upper_purple)
    res_purple=cv.bitwise_and(frame,frame,mask=mask_purple)
    cv.rectangle(res_purple,(0,0),(150,30),(255,255,255),-1)
    res_purple=cv.putText(res_purple,"Purple Color",(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    hor1=cv.hconcat([frame,res_blue])
    hor2=cv.hconcat([res_green,res_red])
    hor3=cv.hconcat([res_yellow,res_purple])
    concat=cv.vconcat([hor1,hor2,hor3])
    
    cv.imshow('Color Segmentation',concat)
    
    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()
