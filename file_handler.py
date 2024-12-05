
from models import Author, Book, Reader, Librarian, BorrowRecord


def load_data(filename):
    """Загрузить данные из текстового файла."""
    authors, books, readers, librarians, borrow_records = [], [], [], [], []

    with open(filename, "r", encoding="utf-8") as file:
        section = None
        for line in file:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1]
            elif line and section:
                if section == "Authors":
                    name, birth_year, country = line.split(",")
                    authors.append(Author(name, int(birth_year), country))
                elif section == "Books":
                    title, author, genre, year, isbn = line.split(",")
                    books.append(Book(title, author, genre, int(year), isbn))
                elif section == "Readers":
                    name, reader_id, email, phone = line.split(",")
                    readers.append(Reader(name, int(reader_id), email, phone))
                elif section == "Librarians":
                    name, librarian_id, email, phone, schedule = line.split(",")
                    librarians.append(Librarian(name, int(librarian_id), email, phone, schedule))
                elif section == "BorrowRecords":
                    title, reader_name, librarian_name, borrow_date, return_date = line.split(",")
                    # Поиск объектов по именам
                    book = next((b for b in books if b.title == title), title)
                    reader = next((r for r in readers if r.name == reader_name), reader_name)
                    librarian = next((l for l in librarians if l.name == librarian_name), librarian_name)
                    borrow_records.append(BorrowRecord(book, reader, librarian, borrow_date, return_date if return_date != "None" else None))

    return authors, books, readers, librarians, borrow_records

def save_data(authors, books, readers, librarians, borrow_records):
    """Сохранить данные в файл с постоянным именем."""
    filename = "library_data.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("[Authors]\n")
        for author in authors:
            file.write(f"{author.name},{author.birth_year},{author.country}\n")

        file.write("\n[Books]\n")
        for book in books:
            file.write(f"{book.title},{book.author},{book.genre},{book.year},{book.isbn}\n")

        file.write("\n[Readers]\n")
        for reader in readers:
            file.write(f"{reader.name},{reader.reader_id},{reader.email},{reader.phone}\n")

        file.write("\n[Librarians]\n")
        for librarian in librarians:
            file.write(
                f"{librarian.name},{librarian.librarian_id},{librarian.email},{librarian.phone},{librarian.schedule}\n")

        file.write("\n[BorrowRecords]\n")
        for record in borrow_records:
            return_date = record.return_date if record.return_date else "Книга не возвращена"
            file.write(f"{record.book.title if isinstance(record.book, Book) else record.book},"
                       f"{record.reader.name if isinstance(record.reader, Reader) else record.reader},"
                       f"{record.librarian.name if isinstance(record.librarian, Librarian) else record.librarian},"
                       f"{record.borrow_date},{return_date}\n")

    print(f"Итоговый файл сохранен: {filename}")



