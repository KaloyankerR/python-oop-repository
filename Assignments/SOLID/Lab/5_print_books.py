from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class TitleFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.title


class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_info(self, book: Book, formatter: Formatter):
        return formatter.format(book)
