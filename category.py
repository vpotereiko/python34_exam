class Category:
    def __init__(self, name):
        self.name = name
        self.owner = None

    @staticmethod
    def addnew(db_category):
        category = {i: cc for i, cc in enumerate(db_category)}
        new_ca = None
        while new_ca is None:
            ca_name = input("Enter new category name: ")
            # ca_key: str = (str(ca_name if len(ca_name) > 0 else '')
            if ca_name not in category.items():
                new_ca = Category(ca_name)
                db_category.append(new_ca)
            else:
                print("This category already exists")
        return new_ca

    @staticmethod
    def delete(db_category):
        category = {i: cc for i, cc in enumerate(db_category)}
        del_ca = None
        while del_ca is None:
            ca_name = input("Enter category name to delete: ")
            # ca_key: str = (str(ca_name if len(ca_name) > 0 else '')
            for c in db_category:
                if str(c) == ca_name:
                    del_ca = [cc for cc in db_category if str(cc) == ca_name]
                    db_category.remove(del_ca[0])
                    print(f"This category {ca_name} removed")
            else:
                if del_ca is None:
                    print("This category does not exist")
        return del_ca

    def __str__(self):
        return self.name

    def __json__(self):
        return self.name

