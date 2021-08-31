from PIL import Image, ImageFilter
import os, glob, sys

path = '/home/etri/YOLO_dataset/add_dataset_all/'
save_path = '/home/etri/YOLO_dataset/add_dataset/'

fileNames = os.listdir(path)

image_index = 683

for fileName in fileNames:
    image = Image.open(os.path.join(path, fileName)).convert('RGB')
    print("path : " + os.path.join(path, fileName))

    new_path = os.path.join(save_path, str(image_index) + '.jpg')
    print("new_path : " + new_path)
    image.save(new_path)
    image_index += 1
