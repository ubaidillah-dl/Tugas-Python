import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv.imread("Watermark.jpg")
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
_,biner=cv.threshold(gray, 70, 255, cv.THRESH_BINARY)
plt.hist(gray.ravel(),256,[0,256])
plt.show()

cv.imshow("Binary", biner)

cv.waitKey(0)
cv.destroyAllWindows()