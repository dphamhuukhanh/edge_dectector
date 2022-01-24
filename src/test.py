import cv2
import numpy as np
import processing as processing


img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
print("anh goc", img)

# Chuyển ảnh sang gray image
img1 = processing.smoothing_processing.image_CannyDectectEdge1(img)
img2 = processing.smoothing_processing.image_CannyDectectEdge2(img, 100, 200)
print("image 1", img1)
print("image 2", img2)

cv2.imshow('Gray', img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()

