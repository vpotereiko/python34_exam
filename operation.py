class Operation:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __json__(self):
        return self.name
