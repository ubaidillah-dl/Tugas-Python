import cv2 as cv

image=cv.imread("Watermark.jpg")

cv.imshow("Image",image)

cv.waitKey(0)
cv.destroyAllWindows()
