import json

FILE_NAME = "books.json"


def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_books(library):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(library, file, ensure_ascii=False, indent=4)


def add_book(library):
    print("\n--- Добавление книги ---")
    title = input("Название: ")
    author = input("Автор: ")
    genre = input("Жанр: ")
    year = input("Год выпуска: ")
    description = input("Короткое описание: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "description": description,
        "read": False,
        "favorite": False
    }

    library.append(book)
    print("Книга залетела в библиотеку 📚")


def show_books(library):
    print("\n--- Моя библиотека ---")
    if not library:
        print("Пока пусто. Самое время добавить первую книгу.")
        return

    for index, book in enumerate(library, start=1):
        read_status = "прочитана" if book["read"] else "не прочитана"
        favorite_status = "★" if book["favorite"] else ""
        print(
            f"{index}. {book['title']} — {book['author']} | "
            f"{book['genre']}, {book['year']} | {read_status} {favorite_status}"
        )
        print(f"   Описание: {book['description']}")


def search_books(library):
    print("\n--- Поиск книги ---")
    keyword = input("Введите название или автора: ").lower()
    found_books = []

    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            found_books.append(book)

    if not found_books:
        print("Такой книги тут не найдено 🤔")
        return

    print("\nНашлось вот что:")
    for index, book in enumerate(found_books, start=1):
        print(f"{index}. {book['title']} — {book['author']}")


def mark_as_read(library):
    print("\n--- Отметить книгу ---")
    if not library:
        print("Библиотека пустая, отмечать пока нечего.")
        return

    show_books(library)

    try:
        index = int(input("Введите номер книги: ")) - 1
        if 0 <= index < len(library):
            library[index]["read"] = not library[index]["read"]
            if library[index]["read"]:
                print("Готово, книга отмечена как прочитанная ✅")
            else:
                print("Окей, книга снова отмечена как не прочитанная.")
        else:
            print("Такого номера нет.")
    except ValueError:
        print("Нужно ввести именно число.")


def toggle_favorite(library):
    print("\n--- Избранное ---")
    if not library:
        print("Библиотека пустая, в избранное пока нечего добавлять.")
        return

    show_books(library)

    try:
        index = int(input("Введите номер книги: ")) - 1
        if 0 <= index < len(library):
            library[index]["favorite"] = not library[index]["favorite"]
            if library[index]["favorite"]:
                print("Книга добавлена в избранное ★")
            else:
                print("Книга убрана из избранного.")
        else:
            print("Такого номера нет.")
    except ValueError:
        print("Нужно ввести именно число.")


def delete_book(library):
    print("\n--- Удаление книги ---")
    if not library:
        print("Библиотека пустая, удалять пока нечего.")
        return

    show_books(library)

    try:
        index = int(input("Введите номер книги, которую хочешь удалить: ")) - 1
        if 0 <= index < len(library):
            removed_book = library.pop(index)
            print(f"Книга «{removed_book['title']}» удалена 🗑")
        else:
            print("Такого номера нет.")
    except ValueError:
        print("Нужно ввести именно число.")


def main():
    library = load_books()

    while True:
        print("\n==============================")
        print("      Т-Библиотека 📚")
        print("==============================")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу")
        print("4. Отметить как прочитанную / не прочитанную")
        print("5. Добавить или убрать из избранного")
        print("6. Удалить книгу")
        print("7. Сохранить и выйти")

        choice = input("Выбери действие: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            show_books(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            mark_as_read(library)
        elif choice == "5":
            toggle_favorite(library)
        elif choice == "6":
            delete_book(library)
        elif choice == "7":
            save_books(library)
            print("Сохранил, всё ок 👌")
            break
        else:
            print("Такого пункта нет, попробуй ещё раз.")


if __name__ == "__main__":
    main()
