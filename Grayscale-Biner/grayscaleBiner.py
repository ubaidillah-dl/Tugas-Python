import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    _,camera=cap.read()
    gray=cv.cvtColor(camera,cv.COLOR_BGR2GRAY)
    _,biner=cv.threshold(gray,160,255,cv.THRESH_BINARY)
    
    cv.imshow('Camera',camera)
    cv.imshow('Grayscale',gray)
    cv.imshow('B&W',biner)
    
    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()