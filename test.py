import unittest
from datetime import date
from tinhtuoi import calculate_age

class TestCalculateAge(unittest.TestCase):
    def test_calculate_age(self):
        birthdate = date(2020, 1, 1)
        age = calculate_age(birthdate)
        self.assertEqual(age, 3)

if __name__ == '__main__':
    unittest.main()