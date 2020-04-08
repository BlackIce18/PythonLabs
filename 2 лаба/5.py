'''
Введите с клавиатуры текст. Программно найдите в нем и выведите
отдельно все слова, которые начинаются с большого латинского
символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
«Petr93», «Johnny70», «Service2002». Используйте регулярные
выражения

Вводил:
Введите Petr93 с клавиатуры Petr93 текст eptr9311 Petr99
'''
import re
print("Введите текст:")
text = input()
results = re.findall(r'([A-Z][a-z]+\d{4})|([A-Z][a-z]+\d{2})', text)
for result in results:
    for i in range(0, len(result)):
        if result[i] != "":
            print(result[i])
