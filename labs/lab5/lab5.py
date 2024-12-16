import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Рік: {self.year}, Жанр: {self.genre}"

class HomeLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre)
        self.books.append(book)
        print(f"Книга \"{title}\" додана до бібліотеки.")

    def remove_book(self, number):
        if 0 <= number < len(self.books):
            removed_book = self.books.pop(number)
            print(f"Книга \"{removed_book.title}\" видалена з бібліотеки.")
        else:
            print("Книга з таким номером не знайдена.")

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key, None) == value]
        return results

    def get_book_by_number(self, number):
        if 0 <= number < len(self.books):
            return self.books[number]
        else:
            print("Книга з таким номером не знайдена.")
            return None

    def display_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        else:
            for i, book in enumerate(self.books):
                print(f"{i}. {book}")

library = HomeLibrary()

library.add_book("Кобзар", "Тарас Шевченко", 1840, "Поезія")
library.add_book("Тіні забутих предків", "Михайло Коцюбинський", 1911, "Проза")
library.add_book("Захар Беркут", "Іван Франко", 1883, "Історичний роман")

print("\nСписок книг у бібліотеці:")
library.display_books()

print("\nПошук книг за автором Тарас Шевченко:")
found_books = library.search_books(author="Тарас Шевченко")
for book in found_books:
    print(book)

print("\nОтримання книги за номером 1:")
book = library.get_book_by_number(1)
if book:
    print(book)

print("\nВидалення книги за номером 0:")
library.remove_book(0)

print("\nСписок книг у бібліотеці після видалення:")
library.display_books()
