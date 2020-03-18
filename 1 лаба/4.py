'''
Напишите скрипт, который разделяет введенный с клавиатуры текст на
слова и выводит сначала те слова, длина которых превосходит 7
символов, затем слова размером от 4 до 7 символов, затем – все
остальные.
'''

text = input("Введите текс: ").split(" ")
text = filter(None, text)
result7 = []
result47 = []
resultother = []
for val in text:
    if len(val) > 7:
        result7.append(val);
    elif len(val) <= 7 & len(val) >= 4:
        result47.append(val);
    else:
        resultother.append(val);
print(result7)
print(result47)
print(resultother)

#Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent cursus tempor sapien quis ullamcorper. Morbi id dui risus. Suspendisse quis mollis magna, nec porttitor urna. Ut id porta orci. Ut tincidunt convallis mi, ut fermentum metus congue eget. Maecenas id eros non nisi efficitur tincidunt quis sed est. Phasellus convallis tellus nec risus vehicula, vel hendrerit arcu aliquam. Nulla accumsan justo et dolor fermentum, ac rhoncus lectus porttitor. Morbi vel enim luctus, congue eros sit amet, commodo magna. Curabitur quam odio, lobortis sit amet ultricies vel, imperdiet vel orci.
