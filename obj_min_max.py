import re

remove_pattern = re.compile('v[a-zA-z]{1,}.') # 무시해야할 패턴

def objPoseZMaxMin(filepath, line_index=0): # object z좌표의 최대, 최소 반환

    with open(filepath) as file:
        for line in file:
            if remove_pattern.match(line) is None and '#' not in line: # vertex positions만 가져오기 위해
                if 'v' in line:
                    line_index += 1

                    split_line = line.split(' ')
                    z_pose = split_line[4].split('\n')[0]

                    if line_index is 1:
                        min_z, max_z = float(z_pose), float(z_pose)
                    else:
                        max_z = float(z_pose) if float(z_pose) >= max_z else max_z
                        min_z = float(z_pose) if min_z > float(z_pose) else min_z

    z_pose = {max: max_z, min: min_z}
    print("file : {0} z_pose : {1}" .format(filepath, z_pose))
    return z_pose