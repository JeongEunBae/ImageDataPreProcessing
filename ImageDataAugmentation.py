import numpy as np

import os
from libarchive.ffi import errno

np.random.seed(3)

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

optInputPath = '/home/etri/YOLO_dataset/add_car_image/' # input 이미지 디렉토리

optOutputPath = '/home/etri/YOLO_dataset/add_car_image_Increase/' # output 디렉토리

optRescale = 1. / 255 #원본 영상은 0-255의 RGB 계수로 구성되는데, 모델을 학습시키기엔 너무 높아 스케일링하여 0-1범위로 변환

optRotationRange = 10 #이미지 회전 범위

optWidthShiftRange = 0.2 # 그림을 수평으로 랜덤하게 평행 이동 시키는 범위 (원본 가로에 대한 비율 값)

optHeightShiftRange = 0.2 # 그림을 수직으로 랜덤하게 평행 이동 시키는 범위 (원본 세로에 대한 비율 값)

optShearRange = 0.5 # 임의 전단 변환 범위

optZoomRange = [0.9, 2.2] # 임의 확대 / 축소 범위

optHorizontalFlip = True # True로 설정할 경우 50% 확률로 좌우반전

optVerticalFlip = True # True로 설정할 경우 50% 확률로 상하반전

optFillMode = 'nearest' # 이미지 회전, 이동, 축소할 때 생기는 공간을 채우는 방식

optNbrOfIncreasePerPic = 2 # 이미지 증가 개수

optNbrOfBatchPerPic = 2

# train_datagen = ImageDataGenerator(rescale=optRescale,
#
#                                    rotation_range=optRotationRange,
#
#                                    width_shift_range=optWidthShiftRange,
#
#                                    height_shift_range=optHeightShiftRange,
#
#                                    shear_range=optShearRange,
#
#                                    zoom_range=optZoomRange,
#
#                                    horizontal_flip=optHorizontalFlip,
#
#                                    vertical_flip=optVerticalFlip,
#
#                                    fill_mode=optFillMode)

train_datagen = ImageDataGenerator(horizontal_flip=optHorizontalFlip)

def checkFoler(path):
    try:

        if not (os.path.isdir(path)):
            os.makedirs(os.path.join(path))

    except OSError as e:

        if e.errno != errno.EEXIST:
            raise


def increaseImage(path, folder):
    for index in range(0, optNbrOfIncreasePerPic):

        img = load_img(path)

        x = img_to_array(img)

        x = x.reshape((1,) + x.shape)

        i = 0

        checkFoler(optOutputPath + folder)

        print('index : ' + str(index))

        for batch in train_datagen.flow(x, batch_size=1, save_to_dir=optOutputPath + folder, save_prefix='car',
                                        save_format='jpg'):

            i += 1

            print(folder + " " + str(i))

            if i >= optNbrOfBatchPerPic:
                break


def generator(dirName):
    checkFoler(optOutputPath)

    try:

        fileNames = os.listdir(dirName)

        for fileName in fileNames:

            fullFileName = os.path.join(dirName, fileName)

            if os.path.isdir(fullFileName):

                generator(fullFileName)

            else:

                ext = os.path.splitext(fullFileName)[-1]

                folderName = os.path.splitext(fullFileName)[0].split('/')[-2]

                if (ext == '.jpg'):
                    increaseImage(fullFileName, folderName)



    except PermissionError:

        pass


if __name__ == "__main__":
    generator(optInputPath)