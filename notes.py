import os


class NotesManager:
    @staticmethod
    def add_note(title, text):
        try:
            os.mkdir("notes")
        except FileExistsError:
            pass

        with open(f"notes/{title}.txt", "w", encoding="utf-8") as f:
            f.write(text)

    @staticmethod
    def list_notes():
        try:
            return os.listdir("notes")
        except FileNotFoundError:
            pass

    @staticmethod
    def read_note(title):
        try:
            with open(f"notes/{title}.txt", "r", encoding="utf-8") as f:
                text = f.read()
                return text
        except FileNotFoundError:
            pass

    @staticmethod
    def delete_note(title):
        try:
            os.remove(f"notes/{title}.txt")
        except FileNotFoundError:
            pass

    @staticmethod
    def clear_notes():
        for note in os.listdir("notes"):
            try:
                os.remove(f"notes/{note}")
            except FileNotFoundError:
                pass



notes_manager = NotesManager()

print("1) Добавить заметку",
      "2) Вывести файлы заметок",
      "3) Вывести текст заметки",
      "4) Удалить заметку",
      "5) Удалить все заметки",
      "0) Выход", sep="\n")

while True:
    user_input = input("Введите команду: ")
    if user_input == "1":
        user_title = input("Введите название заметки: ")
        user_text = input("Введите текст заметки: ")
        notes_manager.add_note(user_title, user_text)
    elif user_input == "2":
        print(notes_manager.list_notes())
    elif user_input == "3":
        user_title = input("Введите название заметки: ")
        print(notes_manager.read_note(user_title))
    elif user_input == "4":
        user_title = input("Введите название заметки: ")
        notes_manager.delete_note(user_title)
    elif user_input == "5":
        notes_manager.clear_notes()
    elif user_input == "0":
        break



