from pathlib import Path
import os
import sys

target = sys.argv[1]
replacement = sys.argv[2]
path = sys.argv[3]
extension = sys.argv[4]

def replace_var(target, replacement, path, extension):
    result = list(Path(path).rglob("*." + extension))
    for i in result:
        read_file = open(i, 'r')
        lines = read_file.readlines()
        for x in range(len(lines)):
            if target in lines[x]:
                lines[x] = lines[x].replace(target, replacement)
        read_file.close()
        os.remove(i)
        write_file = open(i, 'w')
        write_file.seek(0)
        write_file.write(''.join(lines))
        write_file.truncate()
        write_file.close()

replace_var(target, replacement, path, extension)
