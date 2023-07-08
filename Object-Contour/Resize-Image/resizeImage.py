import cv2 as cv

image=cv.imread("Watermark.jpg")

x=image.shape[1]
y=image.shape[0]

xkali=x*2
ykali=y*2
dimensi=(xkali,ykali)
resize=cv.resize(image,dimensi)

cv.imshow("Original",image)
print("Ukuran asli",image.shape)
cv.waitKey(0)
cv.imshow("Resize",resize)
print("Ukuran ubah",resize.shape)

cv.waitKey(0)
cv.destroyAllWindows()
