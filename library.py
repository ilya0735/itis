library = {
    		"Война и мир": {
			"author": "Л. Толстой",
			"year": 1869,
			"ratings": [5, 4, 5]
		},
    		"Преступление и наказание": {
			"author": "Ф. Достоевский",
			"year": 1866,
			"ratings": [5, 5, 4]
		}
}



def add_book():
    try:
        user_book_name = input("Название книги:")
        user_book_name = user_book_name[0].upper() + user_book_name[1:].lower()
    except IndexError:
        print("У книги должно быть название")

    flag = 1
    while flag:
        try:
            user_book_author = input("Автор книги:")
            if user_book_author[1] != ".":
                print("Имя автора должно быть типа: Л.Толстой")
            else:
                flag = 0
            user_book_author = user_book_author[0].upper() + "." + user_book_author[2].upper() + user_book_author[
                3:].lower()
        except IndexError:
            print("Слишком короткое имя. Имя автора должно быть типа: Л.Толстой")


    flag = 1
    while flag:
        try:
            user_book_year = int(input("Год написания книги:"))
            flag = 0
        except ValueError:
            print("Введите год")

    flag = 1
    while flag:
        try:
            user_book_rating = input("Рейтинг книги:")
            user_book_rating_list = list(map(int, user_book_rating.split()))

            flag_in_rating = 0

            for x in user_book_rating_list:
                if 1 <= x <= 5:
                    flag_in_rating = 1
                else:
                    flag_in_rating = 0
                    print("рейтинг должен быть от 1 до 5")
                    break

            if flag_in_rating == 1:
                flag = 0

        except ValueError:
            print("Введите число")


    library[user_book_name] = {
        "author": user_book_author,
        "year": user_book_year,
        "ratings": user_book_rating_list

    }

    print("Книга успешно записана!")


def show_books():
    print("=======================================================================")
    print()
    print("Книги которые хранятся в библиотеке на данный момент:")
    print()
    for book in library:
        print(book)
    print()
    print("=======================================================================")


def find_book():
    try:
        user_book_name = input("Название книги данные о которой хотите найти:")
        user_book_name = user_book_name[0].upper() + user_book_name[1:].lower()
        book_data = library[user_book_name]
        print("=======================================================================")
        print("Данные по книге:")
        print()
        print(f"Название книги: {user_book_name}", f"Автор: {book_data["author"]}",
              f"Год написания: {book_data["year"]}",  f"Рейтинги: {book_data["ratings"]}", sep="\n")
        print()
        print("=======================================================================")
    except KeyError:
        print("Такой книги в библиотеке нет")


def delete_book():
    try:
        user_book_name = input("Название книги которую хотите удалить:")
        user_book_name = user_book_name[0].upper() + user_book_name[1:].lower()
        library.pop(user_book_name)
        print(f"Книга {user_book_name} успешно удалена")
    except KeyError:
        print("Такой книги в библиотеке нет")


def add_book_rating():
    try:
        user_book_name = input("Название книги:")
        user_book_name = user_book_name[0].upper() + user_book_name[1:].lower()
        book_data = library[user_book_name]
    except KeyError or IndexError:
        print("Такой книги в библиотеке нет")
        print()
        return None

    flag = 1
    while flag:
        try:
            new_user_book_rating = input("Добавить книге рейтинг:")
            new_user_book_rating_list = list(map(int, new_user_book_rating.split()))

            flag_in_rating = 0

            for x in new_user_book_rating_list:
                if 1 <= x <= 5:
                    flag_in_rating = 1
                else:
                    flag_in_rating = 0
                    print("рейтинг должен быть от 1 до 5")
                    break

            if flag_in_rating == 1:
                flag = 0

        except ValueError:
            print("Введите число")


    new_rating = book_data["ratings"]

    for i in range(len(new_user_book_rating_list)):
        new_rating.append(new_user_book_rating_list[i])

    library[user_book_name].update({"ratings":new_rating})
    print("Рейтинг успешно добавлен")
    print()


def show_books_released_after_user_year():
    flag = 1
    while flag:
        try:
            user_book_year_border = int(input("Год написания книги:"))
            flag = 0
        except ValueError:
            print("Введите год")

    book_list = []
    for book in library:
        book_year = library[book].get('year')
        if user_book_year_border < book_year:
            book_list.append(book)

    if len(book_list) == 0:
        print("Таких книг в списке нет")

    for book in book_list:
        print(book)
    print()


def show_books_upper_user_border():
    flag = 1
    while flag:
        try:
            user_book_rating = int(input("Рейтинг книги:"))
            book_rate_list = []
            if 1 <= user_book_rating <= 5:
                for book in library:
                    book_min_rating = min(library[book].get("ratings"))
                    if user_book_rating < book_min_rating:
                        book_rate_list.append(book)
                flag = 0

                if len(book_rate_list) == 0:
                    print("Таких книг в списке нет")

                print("Книги из списка рейтингом выше:")
                for book in book_rate_list:
                    print(book)
            else:
                print("Рейтинг должен быть от 1 до 5")
        except ValueError:
            print("Введите число")


def write_book_in_txt():
    file = open("library.txt", "w")
    for book in library:
        book_data = library[book]
        author, year = book_data["author"], str(book_data["year"])
        rating = ""
        for rate in book_data['ratings']:
            rating = rating + str(rate) + ","
        rating = rating[:-1]
        list = [book, author, year, rating]
        list_for_write = ",".join(list)+"\n"
        file.write(list_for_write)
    print("Библиотека успешно записана в файл library.txt")


def read_book_from_txt():
    file = open("library.txt", "r")
    for line in file:
        list_from_file = line.split(",")
        list_from_file[-1] = list_from_file[-1][:1]
        book = list_from_file[0]
        author = list_from_file[1]
        year = int(list_from_file[2])
        ratings = [int(x) for x in list_from_file[3:]]


        library[book] = {
            "author": author,
            "year": year,
            "ratings":  ratings

        }
    print("Книги успешно прочитаны из файла library.txt")



print("1. Добавить книгу", "2. Показать все книги в библиотеке","3. Найти данные о книге",
    "4. Удалить книгу","5. Добавить книге рейтинг","6. Вывести список книг выпущеных после выбраного года",
    "7. Вывести книги минимальный рейтинг которых выше указаного","8. Записать книги в файл library.txt в папке приложения",
    "9. Экспортировать книги из файла library.txt в папке приложения","10. Выход из программы", sep="\n")
print("","",sep="\n")

while True:
    choice = input("Введите номер команды:")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        find_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        add_book_rating()
    elif choice == "6":
        show_books_released_after_user_year()
    elif choice == "7":
        show_books_upper_user_border()
    elif choice == "8":
        write_book_in_txt()
    elif choice == "9":
        read_book_from_txt()
    elif choice == "10":
        print("Спасибо, что воспользовались моей программой!")
        break
    else:
        print("Введите корректное значение")