"""
Написать скрипт trackmix.py, который формирует обзорный трек-микс
альбома (попурри из коротких фрагментов mp3-файлов в
пользовательской директории). Для манипуляций со звуковыми
файлами можно использовать сторонние утилиты, например, FFmpeg.
Пример вызова и работы скрипта:
 trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e
--- processing file 1: 01 - Intro.mp3
--- processing file 2: 02 - Outro.mp3
--- done!
13
Параметры скрипта:
--source (-s) – имя рабочей директории с треками, обязателен;
--destination (-d) – имя выходного файла, необязателен (если не указан,
то имя выходного файла – mix.mp3 в директории source);
--count (-c) – количество файлов в "нарезке", необязателен (если он не
указан, то перебираются все mp3-файлы в директории source);
--frame (-f) – количество секунд на каждый файл, необязателен (если не
указан, скрипт вырезает по 10 секунд из произвольного участка каждого
файла);
--log (-l) – необязательный ключ (если этот ключ указывается, то скрипт
должен выводить на консоль лог процесса обработки файлов, как в
примере);
--extended (-e) – необязательный ключ (если этот ключ указывается, то
каждый фрагмент попурри начинается и завершается небольшим
fade in/fade out).

Для теста вводил: 7.py -s"7" -d"123" -f 4 -c 3 -l -e
"""
from pydub import AudioSegment
import sys
import os
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', default='', required=True)
    parser.add_argument('-d', '--destination', default='')
    parser.add_argument('-c', '--count', default='')
    parser.add_argument('-f', '--frame', default='')
    parser.add_argument('-l', '--log', action='store_true', default=False)
    parser.add_argument('-e', '--extended', action='store_true', default=False)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    source = namespace.source
    destination = namespace.destination
    count = namespace.count
    frame = namespace.frame
    log = namespace.log
    extended = namespace.extended

    folder = [i for i in os.walk(source)]
    allfiles = [files for address, dirs, files in folder][0]

    songs = []
# Нет проверки на тип файла
if frame == '':
    frame = 10

for file in allfiles:
    (mode, ino, dev, nlink, uid, gid, fsize, atime, mtime, ctime) = os.stat(source + '\\' + file)
    if extended:
        songs.append(AudioSegment.from_mp3(source+'\\'+file)[:int(frame)*1000].fade_in(3000).fade_out(3000))


if count == '':
    count = len(songs)-1
else:
    count = int(count)-1
playlist = songs.pop(0)
if log:
    print("--- processing file "+str(1)+": "+allfiles[0])
for i in range(0, count):
    playlist = playlist.append(songs[i])
    if log:
        print("--- processing file "+str(i+2)+": "+allfiles[i+1])

if destination == '':
    destination = source + '\\' + 'mix.mp3'
else:
    destination = destination+".mp3"
if playlist.export(destination, format='mp3'):
    if log:
        print("done!")

