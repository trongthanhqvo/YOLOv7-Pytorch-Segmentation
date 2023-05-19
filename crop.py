import numpy as np
import cv2

image = cv2.imread('/home/k/thanhnt/YOLOv7-Pytorch-Segmentation/runs/detect/exp56/mavic_0.png')
y=202
x=0
h=75
w=640
crop = image[y:y+h, x:x+w]
# print(crop.shape)
cv2.imwrite("abc1.png", crop)
# cv2.imshow('Image', image)
# cv2.waitKey(0) 