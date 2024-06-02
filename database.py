# singleton pattern
from json import dump, dumps, load
from typing import List
import json


class Database:
    """
    Singleton pattern
    """
    from user import User
    from record import Record
    from report import Report
    from category import Category
    from operation import Operation

    __instance = None
    __current_user = None
    operations = []
    categories = []
    reports = []
    records = []
    users = []

    def load_data(db_path='def_db.json'):
        try:
            with open(db_path, "r+") as f:
                empl, users = json.load(f)
        except Exception as e:
            print(e)
            return [{'e1': {'e_name': 'Vasia',
                            'e_surname': 'V3',
                            'e_birthday': '27-07-1978'
                            },
                     },
                    {'u1': 'p1'}
                    ]
        return empl, users

    @staticmethod
    def save_data(f_path='def_db.json'):
        from user import User
        from record import Record
        from report import Report
        from category import Category
        from operation import Operation
        op = Operation('o1')
        cat = Category('c1')
        test_rec = Record(cat, op, 100.0)
        test_rec.category = Category('c1')
        test_rec.operation = Operation('o1')
        test_rec2 = Record()
        op = Operation('o1')
        Database.operations.append(op)
        Database.categories.append(Category('c1'))
        u1 = User('u1', 'p1')
        Database.users.append(u1)
        r = Report()
        Database.records.append(test_rec)
        try:
            with open(f_path, "w", encoding='utf-8') as f:
                json.dump([
                    {i: op for i, op in enumerate(Database.operations)},
                    {i: ca for i, ca in enumerate(Database.categories)},
                    {i: rp for i, rp in enumerate(Database.reports)},
                    {i: {"category": rc.category,
                         "operation": rc.operation,
                         "amount": rc.amount,
                         "date": rc.date,
                         "period": rc.period,
                         "comment": rc.comment}
                     for i, rc in enumerate(Database.records)},
                    {str(u): u.passwd for u in Database.users}], f, indent=4, default=str)
        except Exception as e:
            print(e)

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, vals):
        self.__instance = vals

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database.__instance = Database()
        return Database.__instance

    @staticmethod
    def save_users():
        from user import User
        with open('users.json', 'rw+') as f:
            f.write(dumps(Database.users))

    def __new__(cls, file=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        from user import User
        from operation import Operation
        from category import Category
        from report import Report
        from record import Record

        _, _ = Database.load_data()
        # if not isinstance(self.operations, list) or not isinstance(self.categories, list) or
        #     not isinstance(self.reports, list) or
        #     not isinstance(self.records, list) or
        #     not isinstance(self.users, list):
        #     self.operations = list[Operation]
        # if len(self.operations) == 0:
        #     self.operations = list[Operation]
        # if not self.categories:
        #     self.categories = list[Category]
        # if not self.reports:
        #     self.reports = list[Report]
        # if not self.records:
        #     self.records = list[Record]
        # if not self.users:
        #     self.users = list[User]

    @classmethod
    def save(cls, category):
        pass

    @classmethod
    def save_category(cls):
        pass

    @classmethod
    def load_category(cls):
        pass
