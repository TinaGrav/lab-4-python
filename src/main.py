from book_class import Book
from book_collection import BookCollection
from IndexCollection import IndexCollection
from Library import Library
from simulation import run_simulation
print("Привет! Это симуляция библиотеки. Здесь можно рандомно выполнить одно из следующих действий:")
print("добавление новой ĸниги, удаление случайной ĸниги, поисĸ по рандомному автору, обновление индеĸса, попытĸа получить ĸнигу, ĸоторой нет")
print("Если одно из выпавших действий - попытка получить несуществующую книгу, программа завершает свою работу.")
print("")
seed = int(input("Введите количество рандомных действий, которые хотите выполнить: "))
library = Library()
run_simulation(library, seed)