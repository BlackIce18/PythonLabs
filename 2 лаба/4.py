'''
Напишите скрипт, который позволяет ввести с клавиатуры имя
текстового файла, найти в нем с помощью регулярных выражений все
подстроки определенного вида, в соответствии с вариантом.
Например,
для варианта № 1 скрипт должен вывести на экран следующее:
Строка 3, позиция 10 : найдено '11-05-2014'
Строка 12, позиция 2 : найдено '23-11-2014'
Строка 12, позиция 17 : найдено '23-11-2014'
---------------------------------------------------------------
Вариант 5: найдите все номера телефонов – подстроки вида
«(000)1112233» или «(000)111-22-33»
'''
import re
from itertools import groupby
print("Введите название файла:")
filename = input()+".txt" #phones

regexp = r'^\.'
with open(filename, 'r') as f:
    content = f.read()

results = re.findall(r'(\(\d{3}\)\d{3}-\d{2}-\d{2})|(\(\d{3}\)\d{7})', content)
res = []
for result in results:
    if result[0] != "":
        res.append(result[0])
    elif result[1] != "":
        res.append(result[1])

lines = content.split("\n")
resultsIndx = []
def f(ph):
    linenmb = 1
    for line in lines:
        char = line.find(ph)
        if char != -1:
            print("Строка "+str(linenmb)+", позиция "+str(char)+":"+"найдено"+ph)
        linenmb += 1

res = [el for el, _ in groupby(res)]
for phone in res:
    f(phone)

