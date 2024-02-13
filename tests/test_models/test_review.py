#!/usr/bin/python3
"""Test review"""


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Review"""
    def test_attributes(self):
        """Test values"""
        review = Review()

        # Check if all attributes are present
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        # Check initial values
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_types(self):
        """Test types"""
        review = Review()

        # Check attribute types
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_inheretence(self):
        """test inheritence of basemodel"""
        self.assertIsInstance(Review(), BaseModel)


if __name__ == '__main__':
    unittest.main()
