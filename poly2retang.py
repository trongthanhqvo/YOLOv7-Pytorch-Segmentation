import json 
import base64 
import shutil 
import numpy as np 
import os 
 
path="/home/mrc/thanhnt/YOLOv7-Pytorch-Segmentation/dataset/" 
list_path=os.listdir(path) 
data_point_new=[] 
for file in list_path: 
    if file.endswith(".json"): 
        file_json=path+file 
        with open(file_json) as f: 
            data = json.load(f) 
        data_shape=data["shapes"] 
        for i in range (len(data_shape)): 

            data_point=data_shape[i]['points']
            if len(data_point) == 2:
                point1=data_point[0] 
                point2=[*[data_point[1][0]],*[data_point[0][1]]] 
                point3=[*[data_point[1][0]],*[data_point[1][1]]] 
                point4=[*[data_point[0][0]],*[data_point[1][1]]] 
                data_point_new.append(point1) 
                data_point_new.append(point2) 
                data_point_new.append(point3) 
                data_point_new.append(point4) 
            
                data_shape[i]['points']=data_point_new 
                data_shape[i]["shape_type"]="polygon" 
                data_point_new=[] 
        with open(file_json,"w") as f: 
            json.dump(data, f) 
 
print("done!!")