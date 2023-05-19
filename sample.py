import json
import requests
import time
import numpy as np
import matplotlib.pyplot as plt
path_save = "/home/k/thanhnt/YOLOv7-Pytorch-Segmentation/images/"
number = 0
r = requests.get("http://192.168.0.102:54664/stream", stream=True)
def plot_data(data):
    fig = plt.figure(figsize=(5,5))
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
    # plt.savefig(path_save + "{time}.png".format(time=number),bbox_inches='tight',pad_inches = 0)
    # print(number)
    # plt.close()
    
    plt.show()
if r.encoding is None:
    r.encoding = 'utf-8'
data_colect = []
# print(type(r))
for line in r.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(len(data["samples"]))
        for arr in data["samples"]:
            data_colect.append(arr)
            if len(data_colect) == 500:
                plot_data(data_colect)
                
                print("number:" , number)
                number = number + 1
                # plot_data(data_colect)
                data_colect.clear()
                break
