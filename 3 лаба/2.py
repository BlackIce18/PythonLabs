"""
Напишите классы
«Книга» (с обязательными полями: название, автор,код),
«Библиотека» (с обязательными полями: адрес, номер)
и корректно свяжите их.
Код книги должен назначаться автоматически при добавлении книги в библиотеку
(используйте для этого статический член класса).
Если в конструкторе книги указывается в параметре пустое название,
необходимо сгенерировать исключение (например, ValueError).

Книга должна реализовывать интерфейс
Taggable с методом tag(), который создает на основе строки набор тегов
(разбивает строку на слова и возвращает только те, которые
начинаются с большой буквы). Например, tag() для книги с названием
‘War and Peace’ вернет список тегов [‘War’, ‘Peace’].

Реализуйте классы таким образом, чтобы корректно выполнялся следующий код:
lib = Library(1, ’51 Some str., NY’)
lib += Book(‘Leo Tolstoi’, ‘War and Peace’)
lib += Book(‘Charles Dickens’, ‘David Copperfield’)
for book in lib:

# вывод в виде: [1] L.Tolstoi ‘War and Peace’
print(book)

# вывод в виде: [‘War’, ‘Peace’]
print(book.tag())
"""
import re
class ITaggable():
    def tag(self):
        """"""

class Book(ITaggable):
    codeBook = 1
    def __init__(self, author, title):
        if title == "":
            raise ValueError
        self.title = title
        self.author = author
        self.code = self.codeBook

    @staticmethod
    def BookSTR(book):
        return "[" + str(book.code) + "]" + " " + book.author + " " + "'"+book.title+"'"

    @staticmethod
    def autocodebook():
        Book.codeBook += 1
        return Book.codeBook

    def tag(self):
        tags = []
        reg = re.compile('[^a-zA-Z ]')
        self.title = reg.sub('', self.title)
        words = str(self.title).split(" ")
        for word in words:
            if word.istitle():
                tags.append(word)
        print(tags)
        return tags


class Library:
    lib = []
    cur = 0
    def __init__(self, number, address):
        self.address = address
        self.number = number

    def __iadd__(self, book):
        self.lib.append(book)
        book.autocodebook()
        return self

    def __iter__(self):
        res = []
        while(self.cur != len(self.lib)):
            b = Book.BookSTR(self.lib[self.cur])
            self.cur += 1
            res.append(b)
        return iter(res)

lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')

for book in lib:
    print(book)

for book in lib.lib:
    print(book.tag())

