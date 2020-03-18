'''
Напишите скрипт, генерирующий случайным образом число n в
диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
чисел, также сгенерированных случайным образом, и дополнить
массив нулями до размера, равного ближайшей сверху степени двойки.
Например, если в массиве было n=100 элементов, то массив нужно
дополнить 28 нулями, чтобы в итоге был массив из 28
=128 элементов
(ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).
'''

import random
import math

n = random.randint(1, 100)
result = []
print(n)
zeroes = 2**math.ceil(math.log2(n))

for i in range(0, n):
    result.append(random.randint(1, 100))
addZero = zeroes - n

for i in range(0, addZero):
    result.append(0)
print(result)

'''count = random.randint(1, 20)
print('Количество элементов в списке {}'.format(count))


def numbers_range(a):
    for i in range(a):
        yield random.randint(1, 100)


arr = list(numbers_range(count))
cz = 2
while cz < count:
    for j in range(10000):
        if cz >= count:
            print('2 в степени {0} = {1}'.format(j - 1, cz))
            print(math.ceil(math.log2(j - 1)))
            break
        else:
            cz = 2 ** j
difference = cz - count

print('Необходимо добавить {} нулей'.format(difference))
for k in range(difference):
    arr.append(0)
print(arr)'''