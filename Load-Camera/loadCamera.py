import cv2 as cv 

cap=cv.VideoCapture(0)

while True:
    _,camera=cap.read()
    
    cv.imshow('Camera',camera)
    
    if cv.waitKey(1)==ord('p'):
        break

camera.release()
cv.destroyAllWindows()
