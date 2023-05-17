import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.image as img

#get data
data = np.array(pd.read_csv("/home/k/thanhnt/YOLOv7-Pytorch-Segmentation/test.csv"))
# print(len(data[0]))

# data /= data.max()/255.0
print("data= ",data.shape)

fig = plt.figure()
ax = fig.add_axes((0, 0, 1, 1))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.imshow(data)

plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())

# plt.show()
# plt.savefig("test.png",bbox_inches='tight',pad_inches = 0)
plt.show()
# print(data)
