# image analysis

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cole.jpg',cv2.IMREAD_GRAYSCALE)
#IMRAED_COLOR =1
#IMREAD_UNCHANGED =-1
#IMREAD_GRAYSCALE = 0

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img,cmap='gray', interpolation = 'bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

cv2.imwrite('colegray.png',img)