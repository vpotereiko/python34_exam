# 28052024
# III.
# Реалізуйте додаток «Облік витрат». Основне завдання додатка — зберігати
#  інформацію про витрати користувача.
#  Інтерфейс додатка має надавати такі можливості:
#  ● Додавання категорій витрат.
#  ● Видалення категорій витрат.
#  ● Додавання певної витрати. Потрібно вказувати таку інформацію:
#  ■ Назвавитрати.
#  ■ Дата.
#  ■ Категорія.
#  ● Збереження витрат у файл.
#  ● Завантаження витрат із файлу.
#  ● Створення звітів за такими параметрами:
#  ■ Задатою.
#  ■ Заназвою.
#  ■ Закатегорією.
#  ■ Відображення максимальної витрати у кожній категорії.
# ■ Відображення максимальної витрати у вказаному періоді часу.
#  ■ Відображення мінімальної витрати у кожній категорії.
#  ■ Відображення мінімальної витрати у вказаному періоді часу.
#  Правильне використання патернів проєктування, SOLID-принципів, механізмів
#  тестування під час реалізації завдання дозволить отримати більш високу оцінку.


from enum import Enum


class Day(Enum):
    MONDAY = 1,
    TUESDAY = 2,
    WEDNESDAY = 3,
    THURSDAY = 4,
    FRIDAY = 5,
    SATURDAY = 6,
    SUNDAY = 7


class Month(Enum):
    JANUARY = 1,
    FEBRUARY = 2,
    MARCH = 3,
    APRIL = 4,
    MAY = 5,
    JUNE = 6,
    JULY = 7,
    AUGUST = 8,
    SEPTEMBER = 9,
    OCTOBER = 10,
    NOVEMBER = 11,
    DECEMBER = 12


class Category:
    def __init__(self, name):
        self.name = name
        self.owner = None


class Operation:
    def __init__(self, name):
        self.name = name


# class Period(Enum):
#     custom_period = 1

class Report:
    pass


class Record:
    def __int__(self, period, category, operation, amount, date):
        self.period = period
        self.category = category
        self.operation = operation
        self.amount = amount
        self.date = date


class Database:
    _instances = {}
    operations = list[Operation]
    categories = list[Category]
    reports = list[Report]
    records = list[Record]

    def __new__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__new__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class User:
    db = Database()


if __name__ == '__main__':
    pass
