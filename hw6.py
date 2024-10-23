class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = 'Прочитана' if self.read else 'Непрочитана'
        return f'"{self.title}" автор: {self.author}, год: {self.year}, статус: {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def find_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        return found_books

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                return f'Книга "{title}" отмечена как прочитанная.'
        return f'Книга "{title}" не найдена.'

    def mark_book_as_unread(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_unread()
                return f'Книга "{title}" отмечена как непрочитанная.'
        return f'Книга "{title}" не найдена.'


def main():
    library = Library()

    while True:
        print("\nКоманды:")
        print("1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Найти книгу по названию")
        print("4. Найти книги по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Отметить книгу как непрочитанную")
        print("7. Выйти")

        choice = input("Выберите команду (1-7): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год публикации: ")
            book = Book(title, author, year)
            library.add_book(book)
            print(f'Книга "{title}" добавлена в библиотеку.')

        elif choice == '2':
            print("Список книг в библиотеке:")
            library.list_books()

        elif choice == '3':
            title = input("Введите название книги для поиска: ")
            found_books = library.find_by_title(title)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print(f'Книги с названием "{title}" не найдены.')

        elif choice == '4':
            author = input("Введите автора для поиска: ")
            found_books = library.find_by_author(author)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print(f'Книги автора "{author}" не найдены.')

        elif choice == '5':
            title = input("Введите название книги для отметки как прочитанной: ")
            print(library.mark_book_as_read(title))

        elif choice == '6':
            title = input("Введите название книги для отметки как непрочитанной: ")
            print(library.mark_book_as_unread(title))

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
