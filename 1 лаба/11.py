'''
Напишите генератор frange как аналог range() с дробным шагом.
Пример вызова:

for x in frange(1, 5, 0.1):
print(x)
# выводит 1 1.1 1.2 1.3 1.4 … 4.9
'''
def frange(start, end, step):
    for i in range(start, end):
        while i < end:
            i += step
            yield i


for x in frange(1, 5, 0.1):
    print(x)
