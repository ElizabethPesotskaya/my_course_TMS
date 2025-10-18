from classes import Book, Library

library = Library()

book1 = Book(pages = 350, year = 1836, author = "Пушкин А.С.", price = 57)
book2 = Book(pages=260, year=1841, author="Лермонтов М.Ю.", price=65)
book3 = Book(pages=128, year=1867, author="Толстой Л.Н.", price=48)
book4 = Book(pages=199, year=1869, author="Достоевский Ф.М.", price=55)
book5 = Book(pages = 320, year = 1842, author = "Гоголь М.Ю.", price = 36)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)


print("Книга 1 дешевле 2", book1 < book2)
print(library)

print("Информация о книге с 3 id ", library.get_book_info(3))

print("Поиск книги от автора: Пушкин А.С.")
for book in library.find_by_author("Пушкин А.С."):
    print(book)
print("Поиск книг от авторов: Пушкин А.С.")
for book in library.find_by_author(["Пушкин А.С.", "Гоголь М.Ю."]):
    print(book)
# Добавлен комментарий для коммита
