import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

IN_FILE = '/home/etri/mAP/scripts/extra/result.txt' #input 파일 (result.txt)

DR_PATH = os.path.join('/home/etri/YOLO_dataset/', 'bounding-box') # outputfile 디렉토리
os.chdir(DR_PATH)

SEPARATOR_KEY = 'Enter Image Path:'
IMG_FORMAT = '.jpg'

outfile = None
with open(IN_FILE) as infile:
    for line in infile:
        if SEPARATOR_KEY in line: # jpg 경로만 얻기 위해 조건문 실행
            if IMG_FORMAT not in line:
                break

            image_path = re.search(SEPARATOR_KEY + '(.*)' + IMG_FORMAT, line)

            image_name = os.path.basename(image_path.group(1))

            if outfile is not None:
                outfile.close()

            outfile = open(os.path.join(DR_PATH, image_name + '.txt'), 'w') # 해당 jpg의 txt 파일을 열기

        elif outfile is not None:
            class_name, info = line.split(':', 1)
            confidence, bbox = info.split('%', 1)

            bbox = bbox.replace(')','')

            # 바운딩 박스의 left, top, width, height을 최종적으로 작성
            left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
            outfile.write("left: {}, top: {}, width: {}, height: {}\n".format(left, top, width, height))
