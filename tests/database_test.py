from unittest import TestCase, main

from database import Database


class DatabaseTest(TestCase):
    def setUp(self):
        Database.instance = None

    def tearDown(self):
        Database.instance = None

    # Negative
    def test_database_get_instance_negative(self):
        self.assertIsNone(Database.instance)

    # Positive
    def test_database_get_instance(self):
        self.assertIsNotNone(Database.get_instance())


if __name__ == '__main__':
    main()
