import cv2
import numpy as np

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

camera=cv2.VideoCapture(0)

while True:
    _,frame=camera.read()
    image=rescale_frame(frame,percent=70)
    gray=cv2.cv2tColor(image,cv2.COLOR_BGR2GRAY)
    
    prex=np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])
    prey=np.array([[ 1, 1, 1],
                   [ 0, 0, 0],
                   [-1,-1,-1]])
    
    img_prex=cv2.filter2D(gray,-1,prex)
    img_prey=cv2.filter2D(gray,-1,prey)
    prewitt=cv2.add(img_prex,img_prey)
    prewitt=cv2.cv2tColor(prewitt,cv2.COLOR_GRAY2BGR)
    
    cv2.rectangle(image,(0,0),(150,30),(255,255,255),-1)
    cv2.rectangle(prewitt,(0,0),(150,30),(255,255,255),-1)
    image=cv2.putText(image,"Citra Asli",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    prewitt=cv2.putText(prewitt,"Metode Prewitt",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    
    stacked=np.vstack((image,prewitt))
    cv2.imshow('Deteksi Tepi',stacked)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()