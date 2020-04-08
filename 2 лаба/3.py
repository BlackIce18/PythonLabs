'''
Задан путь к директории с музыкальными файлами (в названии
которых нет номеров, а только названия песен) и текстовый файл,
хранящий полный список песен с номерами и названиями в виде строк
формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
имена файлов в директории на основе текста списка песен
'''
import os

StartPath = "3"
folder = [i for i in os.walk(StartPath)]

allfiles = [files for address, dirs, files in folder][0]
mp3Files = [file for file in allfiles if file[-3:] != 'txt']

with open(StartPath + '\\' + "musics.txt", 'r') as f:
    content = f.read()

newMp3Names = content.split('\n')

for mp3file in mp3Files:
    for i in newMp3Names:
        nmb = i.split('. ')[1]
        name = nmb.split(" [")[0]
        filenmb = i.split('. ')[0]+"."
        #duration = " ["+nmb.split(" [")[1]
        if mp3file[:-4] == name:
            os.rename(StartPath+"\\"+mp3file, (StartPath+"\\"+filenmb+" "+name+mp3file[-4:]))




