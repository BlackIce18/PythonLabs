"""
Напишите скрипт reorganize.py, который в директории --source создает
две директории: Archive и Small. В первую директорию помещаются
файлы с датой изменения, отличающейся от текущей даты на
количество дней более параметра --days (т.е. относительно старые
файлы). Во вторую – все файлы размером меньше параметра --size байт.
Каждая директория должна создаваться только в случае, если найден
хотя бы один файл, который должен быть в нее помещен. Пример
вызова:

Вводил: 6.py --source "6" --data 2 --size 100000
"""
import sys
import argparse
import os
import time
import shutil

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', default='')
    parser.add_argument('-d', '--data', default='')
    parser.add_argument('-sz', '--size', default='')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    source = namespace.source
    data = namespace.data
    size = namespace.size
    folder = [i for i in os.walk(source)]

    allfiles = [files for address, dirs, files in folder][0]
    seconds = time.time()
    for file in allfiles:
        (mode, ino, dev, nlink, uid, gid, fsize, atime, mtime, ctime) = os.stat(source+'\\'+file)


        _seconds = os.path.getctime(source+'\\'+file)
        seconds = time.time()

        if ((seconds-_seconds)/86400) > 2:
            if not (os.path.isdir(source + "\\Archive")):
                os.mkdir(source + "\\Archive")
            shutil.move(source+'\\'+file, source+'\\'+'Archive')
            #print("DA")
        elif (fsize < int(size)):
            if not (os.path.isdir(source + "\\Small")):
                os.mkdir(source + "\\Small")
            shutil.move(source+'\\'+file, source+'\\'+'Small')
