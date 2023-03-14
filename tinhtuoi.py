import unittest
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class TestCalculateAge(unittest.TestCase):
    def test_calculate_age(self):
        birthdate1 = date(2020, 1, 1)
        age1 = calculate_age(birthdate1)
        self.assertEqual(age1, 3)

if __name__ == '__main__':
    unittest.main()