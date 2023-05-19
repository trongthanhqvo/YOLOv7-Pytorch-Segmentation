import numpy as np
import cv2
import pandas as pd
# Tạo ma trận kích thước [142, 1700] ngẫu nhiên cho mục đích minh họa
# matrix_142_1700 = np.random.randint(0, 255, size=(142, 1700))
# print("ma:", matrix_142_1700.shape)
matrix_142_1700 = np.array(pd.read_csv("/home/k/thanhnt/YOLOv7-Pytorch-Segmentation/test1.csv"))
# print("ma:", matrix_142_1700.shape)
# exit()
# Chuyển đổi ma trận kích thước [142, 1700] thành ma trận [480, 640, 3]
matrix_480_640_3 = np.zeros((480, 640, 3), dtype=np.uint8)

# Tính toán tỷ lệ chia tỉ lệ chiều rộng và chiều cao
scale_width = 640 / 1700
scale_height = 480 / 141

# Lặp qua từng điểm ảnh trong ma trận kích thước [142, 1700]
for i in range(141):
    for j in range(1700):
        # Tính toán tọa độ tương ứng trong ma trận [480, 640, 3]
        x = int(j * scale_width)
        y = int(i * scale_height)
        
        # Gán giá trị điểm ảnh cho ma trận [480, 640, 3]
        matrix_480_640_3[y, x] = [matrix_142_1700[i, j]] * 3

# In ma trận kích thước [480, 640, 3] đã chuyển đổi
print(matrix_480_640_3.shape)
cv2.imwrite("aaaaaa.png", matrix_480_640_3)
# cv2.imshow("aaaa", matrix_480_640_3)
# cv2.waiKey(0)