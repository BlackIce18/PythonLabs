'''
Напишите параметризированный декоратор pre_process, который
осуществляет предварительную обработку (цифровую фильтрацию)
списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
коде (по умолчанию равен 0.97). Пример кода:
@pre_process(a=0.93)
def plot_signal(s):
 for sample in s:
print(sample)
'''


def pre_process(a):
    def decoration(foo):
        print(s)
        for i in range(len(s)):
            s[i] = s[i] - a * s[i - 1]
            print(s[-1])
        print(s)
        return foo
    return decoration


s = [1, 5, 3, 9, 6, 5, 7, 4, 3]


@pre_process(0.93)
def plot_signal(s):
    for sample in s:
        print(sample)