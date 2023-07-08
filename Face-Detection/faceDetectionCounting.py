import cv2 as cv 

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

camera=cv.VideoCapture(0)

while True:
    _,frame=camera.read()
    image=rescale_frame(frame,percent=70)
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    
    face_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
    faces=face_cascade.detectMultiScale(gray)
    jumlah=str(len(faces))
    
    for (x,y,w,h) in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv.rectangle(image,(0,0),(175,30),(255,255,255),-1)
    cv.putText(image,"Face Detected : "+str(jumlah),(10,20),cv.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    cv.imshow('Face Detection & Counting',image)
    
    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()