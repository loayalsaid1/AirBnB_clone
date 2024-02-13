#!/usr/bin/python3
"""Test user"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test the user class"""
    def test_attributes(self):
        """test attirbutes of the instance"""
        user = User()

        # Check if all attributes are present
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_values(self):
        """Check initial values are empty strings"""
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test the types"""
        user = User()

        # Check attribute types
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
