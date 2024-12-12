import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password(10)
        self.assertEqual(len(password), 8)

    def test_password_contains_uppercase(self):
        password = generate_password(10, use_uppercase=True)
        self.assertRegex(password, '[A-Z]')
