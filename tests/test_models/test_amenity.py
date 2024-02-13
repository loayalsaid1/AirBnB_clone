#!/usr/bin/python3
"""Test City"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """test the Amenity class"""
    def test_attributes(self):
        """Test values"""
        amenity = Amenity()

        # Check if all attributes are present
        self.assertTrue(hasattr(amenity, 'name'))

        # Check initial value is an empty string
        self.assertEqual(amenity.name, "")

    def test_attribute_types(self):
        """Test types"""
        amenity = Amenity()

        # Check attribute type
        self.assertIsInstance(amenity.name, str)

    def test_inheretence(self):
        """test inheritence of basemodel"""
        self.assertIsInstance(Amenity(), BaseModel)


if __name__ == '__main__':
    unittest.main()
