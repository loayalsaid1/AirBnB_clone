#!/usr/bin/python3
"""Test user"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """test the State class"""
    def test_attributes(self):
        """Test the attributes of the class"""
        state = State()
        # Check if all attributes are present
        self.assertTrue(hasattr(state, 'name'))
        # Check initial value is an empty string
        self.assertEqual(state.name, "")

    def test_attribute_types(self):
        """test the type of ht eattribute"""
        state = State()
        # Check attribute type
        self.assertIsInstance(state.name, str)

    def test_inheretence(self):
        """test inheritence of basemodel"""
        self.assertIsInstance(State(), BaseModel)


if __name__ == '__main__':
    unittest.main()
