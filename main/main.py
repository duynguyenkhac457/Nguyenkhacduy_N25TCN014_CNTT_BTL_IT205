from library import Library
from book import Book
from student import Student


library = Library()


while True:
    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")

    choice = input("Choose: ")

   match choice:
        case "1":
            try:
                qty = int(input("Quantity: "))
                if qty < 0:
                    raise ValueError
                library.add_book(Book(input("Book ID: "), input("Title: "), input("Author: "), qty))
            except ValueError:
                print("Invalid quantity. Please enter a positive number.")

        case "2":
            library.view_books()

        case "3":
            book = library.search_book(input("Book ID: "))
            print(book.show_info() if book else "Book not found")

        case "4":
            library.delete_book(input("Book ID: "))

        case "5":
            library.add_student(Student(input("Student ID: "), input("Name: "), input("Class: ")))

        case "6":
            library.view_students()

        case "7":
            student = library.search_student(input("Student ID: "))
            print(student.show_info() if student else "Student not found")

        case "8":
            library.delete_student(input("Student ID: "))

        case "9":
            library.borrow_book(input("Student ID: "), input("Book ID: "))

        case "10":
            library.return_book(input("Book ID: "))

        case "0":
            print("Exiting library system...")
            break
            
        case _:
            # This acts as an 'else' catching any invalid inputs
            print("Invalid choice, please try again.")
