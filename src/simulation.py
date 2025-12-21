import random
from simul_functions import add_book
from simul_functions import remove_book
from simul_functions import search_book
from simul_functions import new_index
from simul_functions import unexisting_book
from Library import Library
from book_class import Book

def run_simulation(library, steps: int = 20, seed: int or None = None) -> None:
    for i in range(steps):
        rand_number = random.randint(0, 4)
        if rand_number == 0:
            print(f"{i + 1}. Добавление рандомной книги")
            add_book(library)
            print("")
        elif rand_number == 1:
            print(f"{i + 1}. Удаление рандомной книги")
            if library:
                remove_book(library)
            else:
                print("No books to remove")
            print("")
        elif rand_number == 2:
            print(f"{i + 1}. Поиск книги по случайно выбранному автору")
            search_book(library)
            print("")
        elif rand_number == 3:
            print(f"{i + 1}. Обновление индексов")
            new_index(library)
            print("")
        elif rand_number == 4:
            print(f"{i + 1}. Попытка получить несуществующую книгу")
            unexisting_book(library)


