import cv2
import numpy as np
import processing as processing


img = cv2.imread('./RGB-picker.png', cv2.IMREAD_UNCHANGED)
print("anh goc", img)

# Chuyển ảnh sang gray image
img_gray1 = processing.smoothing_processing.image_CannyDectectEdge1(img, 100, 200)
img_gray2 = processing.smoothing_processing.image_CannyDectectEdge2(img, 100, 200)


##Sobel filter
# compute gx, gy
#gx = cv2.Sobel(img_gray, cv2.CV_32F, dx=0, dy=1, ksize=3)
#gy = cv2.Sobel(img_gray, cv2.CV_32F, dx=1, dy=0, ksize=3)

# compute gradient magnitude and gradient direction
#g, theta = cv2.cartToPolar(gx, gy, angleInDegrees=True)

#img_fix1 = processing.smoothing_processing.image_CannyDectectEdge1(img, 100, 200)
#img_fix2 = processing.smoothing_processing.image_CannyDectectEdge2(img, 100, 200)


cv2.imshow('Gray', img_gray1)
#cv2.imshow('Gray', img_gray2)
cv2.waitKey(5000)
cv2.destroyAllWindows()

