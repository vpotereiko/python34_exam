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

import database
from record import Record, Category
from user import User


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


# class Category:
#     def __init__(self, name):
#         self.name = name
#         self.owner = None
#
#     @classmethod
#     def add(cls):
#         pass
#
#     @classmethod
#     def delete(cls):
#         pass
#

# class Operation:
#     def __init__(self, name):
#         self.name = name


# class Period(Enum):
#     custom_period = 1

# class Report:
#     @classmethod
#     def create_report(cls):
#         pass


# class Record:
#     def __int__(self, period, category, operation, amount, date):
#         self.period = period
#         self.category = category
#         self.operation = operation
#         self.amount = amount
#         self.date = date


# class Menu:
#
#     @staticmethod
#     def generate_main_menu_items(items: dict | None = None) -> tuple[dict[str, str], list[str]]:
#         if items is None:
#             items = {
#                 "0. Register ": user.User.register,
#                 "1. Log in ": user.User.login,
#                 "2. Add category": Category.add,
#                 "3. Delete category": Category.delete,
#                 "4. Save to file": database.Database.save_category,
#                 "5. Load from file": database.Database.load_category,
#                 "6. Create report": Report.create_report,
#                 "7. Exit": "exit()",
#             }
#             keys = {}
#             for item in items.items():
#                 keys.update({
#                     f"\n{item[0]}": '',
#                 })
#             actions = []
#             for item in items.items():
#                 actions.append(item[1])
#             return keys, actions
#
#     def __init__(self):
#         pass
#

if __name__ == '__main__':
    # Singleton
    user_db = database.Database.get_instance()
    print(user_db)

    rec = Record()
    rec.category = Category('food')
    user_db.users = []
    user_db.operations = []
    user_db.categories = []
    user_db.records = []
    user_db.reports = []
    current_user = None
    while True:
        if current_user:
            print(f"\nLogged in as {current_user}")
            choice = input("1. Додавання категорій витрат\n"
                           "2. Видалення категорій витрат\n"
                           "3. Додавання певної витрати\n"
                           "4. Збереження витрат у файл\n"
                           "5. Завантаження витрат із файлу\n"
                           "6. Створення звітів за параметрами\n"
                           "7. Перегляд усіх внесних витрат\n"
                           "8. Вихід\n"
                           "9. Вихід з програми\n"
                           "Виберіть дію: ")
            # choice = input("1. Search empl.\n"
            #    "2. Add empl.\n"
            #    "3. Edit empl.\n"
            #    "4. Delete empl.\n"
            #    "5. Show all empl.\n"
            #    "6. Sava data.\n"
            #    "7. Log out.\n"
            #    "8. Exit.\n"
            #    "Choose an option: ")
            if choice == "1":
                # user_db = Database.get_instance()
                new_cateory = Category.addnew(user_db.categories)
                print(f"{new_cateory} успішно додано")
            elif choice == "2":
                del_cateory = Category.delete(user_db.categories)
            elif choice == "3":
                new_record = Record.addnew(user_db.records,user_db.categories,user_db.operations)
            elif choice == "4":
                file_name = input("Enter file name: ")
                user_db.save_data(file_name)
            elif choice == "5":
                pass  # show_all_empl(empl)
            elif choice == "6":
                pass  # save_data(empl, users)
            elif choice == "7":
                print(*user_db.records)
            elif choice == "8":
                current_user = None
            elif choice == "9":
                break
        else:
            choice = input("1. Log in.\n"
                           "2. Sign up.\n"
                           "3. Search report.\n"
                           "4. Show all records.\n"
                           "5. Exit.\n"
                           "Choose an option: ")
            if choice == "1":
                from user import User
                from database import Database
                user_db = Database.get_instance()
                Database.save_data()
                current_user = User.log_in(Database.users)
            elif choice == "2":
                current_user = User.sign_up(user_db.users)
                # current_user = sign_up(users)
            elif choice == "3":
                pass  # load all records Database.load_data()
            elif choice == "4":
                print(*user_db.records, sep='\n')
            elif choice == "5":
                break


    #
    # menu_view, menu_actions = Menu.generate_main_menu_items()
    # print(*menu_view)
    # user_input = ''
    # while (user_input := input('0-7\n')) != '7':
    #     if int(user_input) in range(0, len(menu_actions)):
    #         match user_input:
    #             case '0':
    #                 status, user_name = menu_actions[0]()
    #                 if status:
    #                     print(f"Register as {user_name}")
    #             case '1':
    #                 status, user_name = menu_actions[1]()
    #                 if status:
    #                     print(f"Login as {user_name}")
    #             case '2':
    #                 menu_actions[2]()
    #             case '3':
    #                 menu_actions[3]()
    #             case '4':
    #                 menu_actions[4]()
    #             case '5':
    #                 menu_actions[5]()
    #             case '6':
    #                 menu_actions[6]()
    #             case '7':
    #                 menu_actions[7]()
    #             case _:
    #                 print('Invalid input')
    #     else:
    #         print('Invalid input')
