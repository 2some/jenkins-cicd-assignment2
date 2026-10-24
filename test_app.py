import unittest
from app import greet, add_numbers


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Obinna"), "Hello, Obinna!")

    def test_greet_removes_extra_spaces(self):
        self.assertEqual(greet("  Obinna  "), "Hello, Obinna!")

    def test_greet_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()