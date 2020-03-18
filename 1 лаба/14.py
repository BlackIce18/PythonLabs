'''
Напишите декоратор non_empty, который дополнительно проверяет
списковый результат любой функции: если в нем содержатся пустые
строки или значение None, то они удаляются. Пример кода:
@non_empty
def get_pages():
 return ['chapter1', '', 'contents', '', 'line1']
'''


def non_empty(foo):
    def wrapper():
        res = list(filter(None, foo()))
        return res
    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None, 'line2', None]


print(get_pages())
'''
def non_empty(foo):
    def wrapper():
        res = foo()
        iter = 0
        for i in res:
            if i == '' or i is None:
                res.pop(iter)
            iter += 1
        return res
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None, 'line1', None]

print(get_pages())
'''