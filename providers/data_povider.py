from abc import ABC, abstractmethod


class DataProvider(ABC):
    @classmethod
    @abstractmethod
    def connect():
        pass

    @staticmethod
    @abstractmethod
    def create_tables():
        pass

    @staticmethod
    @abstractmethod
    def add_autor(name):
        pass

    @staticmethod
    @abstractmethod
    def add_book(*args):
        pass

    @staticmethod
    @abstractmethod
    def create_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def get_books_by_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def get_books_by_autor_and_year(author_name, year):
        pass


