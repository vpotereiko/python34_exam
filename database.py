# singleton pattern
class Database:
    """
    Singleton pattern
    """
    __instances = None
    operations = list
    categories = list
    reports = list
    records = list

    @staticmethod
    def get_instance():
        if Database.__instances is None:
            Database.__instances = Database()
        return Database.__instances

    def __new__(cls, file=None):
        if cls.__instances is None:
            cls.__instances = super().__new__(cls)
        return cls.__instances

    def __init__(self):
        from main import Operation, Category, Report, Record

        if not self.operations:
            self.operations = list[Operation]
        if not self.categories:
            self.categories = list[Category]
        if not self.reports:
            self.reports = list[Report]
        if not self.records:
            self.records = list[Record]
