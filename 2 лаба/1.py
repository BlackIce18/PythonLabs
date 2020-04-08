"""
Напишите скрипт, который читает текстовый файл и выводит символы
в порядке убывания частоты встречаемости в тексте. Регистр символа
не имеет значения. Программа должна учитывать только буквенные
символы (символы пунктуации, цифры и служебные символы слудет
игнорировать). Проверьте работу скрипта на нескольких файлах с
текстом на английском и русском языках, сравните результаты с
таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
"""
import collections

fileText = open('file.txt').read()
filtered = map(lambda x: x.lower(), filter(lambda x: x.isalpha(), fileText))
res = list(map(lambda x: (x[0], x[1]/len(fileText)), collections.Counter(filtered).items()))
print(res)