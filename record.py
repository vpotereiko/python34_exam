from __future__ import annotations

from category import Category
from operation import Operation
from period import Period


class Record:
    def __init__(self,
                 operation: Operation | None = None,  # назва витрати
                 date=None,                           # дата
                 category: Category | None = None,    # категорія
                 amount=0.00,
                 period: Period | None = None,
                 comment: str = ''):
        self.period = period
        self.category = category
        self.operation = operation
        self.amount = amount
        self.date = date
        self.comment = comment

    def addnew(db_records,db_categories,db_operations):
        print("Введіть назву категорії")
        category = input()
        print("Введіть назву операції")
        operation = input()
        print("Введіть суму")
        amount = input()
        print("Введіть дату")
        date = input()
        print("Введіть коментарій")
        comment = input()
        new_record = Record(operation,date,category,amount,None,comment)
        db_records.append(new_record)
        db_categories.append(new_record.category)
        db_operations.append(new_record.operation)
        return new_record

    def __str__(self):
        return f"{str(self.category)} {str(self.operation)} {str(self.amount)} {str(self.date)}"

    def __json__(self):
        return f"{self.category.name} {self.operation.name} {self.amount} {self.date}"
