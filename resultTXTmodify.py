import os

filePATH = "/home/etri/yolo_custum_test/result.txt"
outfilePATH = "/home/etri/mAP/scripts/extra/modify_result.txt"
rewritefilePATH = "/home/etri/mAP/scripts/extra/result.txt"

SEPARATOR_KEY = 'Enter Image Path:'
REMOVE_TEXT = 'Detection layer:'
HOME = "/home/etri/yolo_custum_test/img"

outfile = open(outfilePATH, 'w')
rewritefile = open(rewritefilePATH, 'w')

with open(filePATH) as file:
    for line in file:
        if SEPARATOR_KEY not in line:
            if REMOVE_TEXT in line:
                continue

        outfile.write(line)
outfile.close()

with open(outfilePATH) as file:
    for line in file:
        if SEPARATOR_KEY in line:
            if REMOVE_TEXT in line:
                continue

        if HOME in line:
            line = 'Enter Image Path: ' + line

        rewritefile.write(line)

rewritefile.close()