#models.py — содержит классы (Book, Author, Reader, и т.д.).
#data.txt — хранит данные (списки объектов).functions.py — содержит вспомогательные функции.main.py — точка входа, где запускается меню.

from file_handler import load_data, save_data
from functions import (
    add_author,
    remove_author,
    add_book,
    remove_book,
    register_reader,
    show_reader_card,
    lend_book,
    return_book,
    show_all_books,
    show_all_data,
)

DATA_FILE = "data.txt"

def main_menu():
    authors, books, readers, librarians, borrow_records = load_data(DATA_FILE)

    while True:
        print("-" * 40)
        print("Библиотека")
        print("-" * 40)
        print("\nМеню:")
        print("1. Добавить автора")
        print("2. Удалить автора")
        print("3. Добавить книгу")
        print("4. Удалить книгу")
        print("5. Зарегистрировать читателя")
        print("6. Просмотр карточки читателя")
        print("7. Выдать книгу")
        print("8. Вернуть книгу")
        print("9. Просмотреть все книги")
        print("10. Показать все данные")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_author(authors)
        elif choice == "2":
            remove_author(authors)
        elif choice == "3":
            add_book(books, authors)
        elif choice == "4":
            remove_book(books)
        elif choice == "5":
            register_reader(readers)
        elif choice == "6":
            show_reader_card(readers, borrow_records)
        elif choice == "7":
            lend_book(books, readers, librarians, borrow_records)
        elif choice == "8":
            return_book(borrow_records)
        elif choice == "9":
            show_all_books(books)
        elif choice == "10":
            show_all_data(books, authors, readers, librarians, borrow_records)
        elif choice == "0":
            save_data(authors, books, readers, librarians, borrow_records)
            print("Работа завершена. Итоговые данные сохранены.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
