from PIL import Image, ImageFilter
import os, glob, sys

path = '/home/etri/YOLO_dataset/add_car_image/'

fileNames = os.listdir(path)

for fileName in fileNames:
    image = Image.open(os.path.join(path, fileName)).convert('RGB')

    if os.path.splitext(fileName)[1] != '.jpg':
        new_path = os.path.join(path, os.path.splitext(fileName)[0] + '.jpg') # jpg 파일로 변
        os.remove(os.path.join(path, fileName))정
    else:
        new_path = os.path.join(path, fileName)

    print("new_path : " + new_path)
    print("pre_img_size : " + str(image.size))
    image = image.resize((600, 400))  # 이미지 사이즈 조
    image.save(new_path)
    print("post_img_size : " + str(image.size))





환