#!/usr/bin/python3
"""Test City"""


import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """test the City class"""
    def test_attributes(self):
        """"Test values"""
        city = City()

        # Check if all attributes are present
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

        # Check initial values are empty strings
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_types(self):
        """test types"""
        city = City()

        # Check attribute types
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_inheretence(self):
        """test inheritence of basemodel"""
        self.assertIsInstance(City(), BaseModel)


if __name__ == '__main__':
    unittest.main()
