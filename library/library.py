from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for b in self.books:
            print(b.show_info())

    def search_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        return None

    def delete_book(self, book_id):
        book = self.search_book(book_id)
        if book:
            self.books.remove(book)
            print("Deleted successfully")
        else:
            print("Book not found")

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        for s in self.students:
            print(s.show_info())

    def search_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print("Deleted successfully")
        else:
            print("Student not found")

    def borrow_book(self, student_id, book_id):
        student = self.search_student(student_id)
        book = self.search_book(book_id)
        if not student:
            print("Student not found")
        elif not book:
            print("Book not found")
        elif book.borrow_book():
            print("Borrow successful")
        else:
            print("Book out of stock")

    def return_book(self, book_id):
        book = self.search_book(book_id)
        if book:
            book.return_book()
            print("Return successful")
        else:
            print("Book not found")
