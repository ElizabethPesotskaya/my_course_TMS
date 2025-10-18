from dataclasses import dataclass, field
from typing import Optional, List

class PageCountError(Exception):
    def __str__(self):
        return "Страницы не должны быть меньше 0!"
class CorrectYear(Exception):
    def __str__(self):
        return "Год должен быть не раньше 1600!"
class AuthorNotSpecified(Exception):
    def __str__(self):
        return "Автор не указан!"
class PriceError(Exception):
    def __str__(self):
        return "Цена не может быть меньше 0!"

@dataclass
class Book:
    book_id: Optional[int] = field(default=None, init=False)
    pages: int
    year: int
    author: str
    price: float

    def __post_init__(self):
        if self.pages < 0:
            raise PageCountError()
        if self.year < 1600:
            raise CorrectYear()
        if not self.author or not isinstance(self.author, str):
            raise AuthorNotSpecified()
        if self.price <= 0:
            raise PriceError()

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    def __str__(self):
        return f" Книга #{self.book_id or '—'}: '{self.author}', {self.year}, {self.pages} стр., {self.price} руб."

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.next_id: int = 1
    def add_book(self, book) :
        book.book_id = self.next_id
        self.next_id += 1
        self.books.append(book)

    def get_book_info(self, book_id: int):
        for book in self.books:
            if book.book_id == book_id:
                return str(book)
        return None

        return None
    def find_by_author(self, author) :
        if isinstance(author, str):
            return [book for book in self.books if book.author == author]
        elif isinstance(author, list):
            return [book for book in self.books if book.author in author]
    def __str__(self):
        if not self.books:
            return " Библиотека пуста."
        return f" Библиотека содержит {len(self.books)} книг:\n" + "\n".join(str(book) for book in self.books)