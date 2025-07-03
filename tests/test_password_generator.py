
# Using ChatGPT Tools I generated unit tests to maintain and test the integrity of the code
# I generated the code and dually checked it for accuracy

import unittest
from password_generator import create_password, created_passwords

class TestPasswordGenerator(unittest.TestCase):
    
    def test_password_length(self):
        # Test that password length is between 16 and 24
        pwd = create_password()
        self.assertTrue(16 <= len(pwd) <= 24)
    
    def test_password_character_types(self):
        # Test that password contains at least one uppercase, lowercase, digit, and special char
        pwd = create_password()
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
        self.assertTrue(any(c in special_chars for c in pwd))

    def test_uniqueness(self):
        # Test that creating multiple passwords produces unique results
        generated = set()
        for _ in range(50):
            pwd = create_password()
            self.assertNotIn(pwd, generated)
            generated.add(pwd)

if __name__ == '__main__':
    unittest.main()

