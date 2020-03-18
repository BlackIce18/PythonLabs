'''
Напишите собственную версию генератора enumerate под названием
extra_enumerate. Пример вызова:
for i, elem, cum, frac in extra_enumerate(x):
 print(elem, cum, frac)
5
В переменной cum хранится накопленная сумма на момент текущей
итерации, в переменной frac – доля накопленной суммы от общей
суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
вывод будет таким:
 (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)
'''
def extra_enumerate(x):
    fraction = 0
    cum = 0
    for step in x:
        fraction += step
    for i in range(len(x)):
        elem = x[i]
        cum += x[i]
        frac = cum / fraction
        yield i, elem, cum, frac


x = [1, 3, 4, 2]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
