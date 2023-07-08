import cv2 as cv
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]*percent/100)
    height=int(frame.shape[0]*percent/100)
    dim=(width, height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cap=cv.VideoCapture(0)

while True:
    _,frame=cap.read()
    image=rescale_frame(frame,percent=50)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edge=cv.Canny(gray,50,300)
    _,biner=cv.threshold(gray,60,255,cv.THRESH_BINARY)
    contours,hierarchy=cv.findContours(edge,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    
    jumlah=str(len(contours))
    print("jumlah objek : ",jumlah)
    result_contour=cv.drawContours(image,contours,-1,(0,255,0),2)

    cv.imshow("Grayscale",gray)
    cv.imshow("Canny",edge)
    cv.imshow("Biner",biner)
    cv.imshow("Result Contour",result_contour)
    
    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()
