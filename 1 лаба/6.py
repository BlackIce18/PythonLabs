'''
Напишите программу, позволяющую ввести с клавиатуры текст
предложения и вывести на консоль все символы, которые входят в этот
текст ровно по одному разу.
'''

'''
text = list(input('Введите текст: '))
for i in text:
    if text.count(i) == 1:
        print(i, end='\n')
'''

text = input("Введите текст: ")

result = []
for val in text:
    firstIndex = text.find(val)
    lastIndex = text.rfind(val)

    if firstIndex == lastIndex:
        if text[firstIndex].isalnum():
            result.append(text[firstIndex])

print(result)

