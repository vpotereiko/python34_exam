from hashlib import sha256 as hashlib_sha256
from json import dumps, loads

import database


class User:
    # from database import Database
    # db = Database.get_instance()

    @staticmethod
    def user_hash(login, passwd, skip_validations=True):
        """
        :param login:
        :param passwd:
        :param skip_validations:
        :return:
        """
        pass_str = login + passwd
        if skip_validations:
            return hashlib_sha256(pass_str.encode()).hexdigest()
        if not isinstance(login, str):
            raise TypeError('login must be string')
        if not isinstance(passwd, str):
            raise TypeError('passwd must be string')
        if not skip_validations and not login:
            raise ValueError('login must be not empty')
        if not skip_validations and not passwd:
            raise ValueError('passwd must be not empty')
        if not skip_validations and len(login) < 3:
            raise ValueError('login must be more than 3 symbols')
        if not skip_validations and len(passwd) < 3:
            raise ValueError('passwd must be more than 3 symbols')
        return hashlib_sha256(pass_str.encode()).hexdigest()

    def __init__(self, login, passwd):
        self.login = login
        self.passwd = User.user_hash(login, passwd)

    def log_in(db_users: list = None):
        current_user = None
        while current_user is None:
            username = input("Enter username: ")
            password = input("Enter password: ")
            users = {str(u): u.passwd for u in db_users}
            if username in users and users[username] == User.user_hash(username, password):
                current_user = username
            else:
                print("Wrong username or password")
        return current_user

    def sign_up(self, users: list = None):
        current_user = None
        while current_user is None:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username not in users:
                users[username] = password
                current_user = username
        return current_user

    @classmethod
    def register(cls):
        user_login = input('Input your login: ')
        user_passwd = input('Input your password: ')
        new_user = User(user_login, User.user_hash(user_login, user_passwd))
        db = database.Database.get_instance()
        if db.users is None:
            db.users = list[User]
        db.users = list(db.users)
        db.users.append(new_user)
        with open('users.json', 'w') as f:
            f.write(dumps(db.users))
        db.__loged_user = new_user
        return True, user_login

    def __str__(self):
        return self.login

    def __json__(self):
        return {'login': self.login, 'passwd': self.passwd}
