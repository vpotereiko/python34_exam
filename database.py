# singleton pattern
class Database:
    """
    Singleton pattern
    """
    __instance = None
    operations = list
    categories = list
    reports = list
    records = list

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

    def __new__(cls, file=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

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
