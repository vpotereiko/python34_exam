from unittest import TestCase, main

from database import Database


class DatabaseTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Positive
    def test_database_get_instance(self):
        self.assertIsNotNone(Database.get_instance())

    # Negative
    # def test_database_get_instance_negative(self):
    #     self.assertIsNone(Database.get_instance())


if __name__ == '__main__':
    main()
