from abc import ABC, abstractmethod

class PersonBase(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Book(PersonBase):
    def __init__(self, book_id, title, author, quantity):
        self.id = book_id
        self.title = title
        self.author = author
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def borrow_book(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def return_book(self):
        self.__quantity += 1

    def show_info(self):
        return f"{self.id} | {self.title} | {self.author} | {self.__quantity}"
