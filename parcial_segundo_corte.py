class Member:
    def __init__(self, name, id, borrowed_books=None):
        self.name = name
        self.__id = id 
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
#prestamos libros
    def borrow_book(self, book):
        if book.is_available():
            self.borrowed_books.append(book)
            book.set_availability(False)
            print(f"{self.name} ha tomado prestado el libro '{book.title}'.")
        else:
            print(f"El libro '{book.title}' no está disponible.")
#devolvemos libros
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_availability(True)
            print(f"{self.name} ha devuelto el libro '{book.title}'.")
        else:
            print(f"El libro '{book.title}' no fue tomado por {self.name}.")

    def __str__(self):
        return f"Miembro: {self.name}, ID: {self.__id}, Libros prestados: {[book.title for book in self.borrowed_books]}"

    def __repr__(self):
        return self.__str__()

class MemberVIP(Member):
    def __init__(self, name, id, borrowed_books=None, limit_books=10):
        super().__init__(name, id, borrowed_books)
        self.limit_books = limit_books
#prestamos libros sin exceder los 10 libros
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.limit_books:
            super().borrow_book(book)
        else:
            print(f"{self.name} ha alcanzado el límite de préstamos.")

    def __str__(self):
        return f"Miembro VIP: {self.name}, ID: {self.__id}, Libros prestados: {[book.title for book in self.borrowed_books]}, Límite de préstamos: {self.limit_books}"

    def __repr__(self):
        return self.__str__()

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn 
        self.available = available

    def is_available(self):
        return self.available

    def set_availability(self, status):
        self.available = status

    def __repr__(self):
        return f"Título del libro: {self.title}, Autor: {self.author}, ISBN: {self.__isbn}, Disponible: {self.available}"

class Library:
    def __init__(self, title, books=None):
        self.title = title
        self.books = books if books is not None else []

    def add_book(self, new_book):
        self.books.append(new_book)
        print(f"Libro '{new_book.title}' agregado a la biblioteca.")
        return new_book

    def show_book(self, index):
        return self.books[index] if index < len(self.books) else "Índice fuera de rango"

    def show_books(self):
        return self.books

    def remove_book(self, index):
        if index < len(self.books):
            removed_book = self.books.pop(index)
            print(f"Libro '{removed_book.title}' eliminado de la biblioteca.")
        else:
            print("Índice fuera de rango")

#se crea la biblioteca
my_library = Library("Biblioteca Central")
#agregamos libros a la biblioteca
libro1 = my_library.add_book(Book("El Viaje de Ana", "Ana Pérez", "12345"))
libro2 = my_library.add_book(Book("La Historia de Carlos", "Carlos Martínez", "67890"))
miembro = Member("Juan", "001")
miembro_vip = MemberVIP("Sofía", "002")
#prestamos los libros
miembro.borrow_book(libro1)
miembro_vip.borrow_book(libro2)
#intento el prestamo de un libro no disponible
miembro.borrow_book(libro2)
#devolvemos los libros
miembro.return_book(libro1)
miembro_vip.return_book(libro2)
#se muestran todos los libros en la biblioteca
for book in my_library.show_books():
    print(book)