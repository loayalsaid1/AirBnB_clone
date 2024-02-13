#!/usr/bin/python3
"""Test the base model class V1"""


from models.base_model import BaseModel
import datetime
import unittest
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test the base case model

        Test cases:
            has id
            string id
            unique id
            has created_at
            and updated_at
            both are datetime objects
            __str__ fucntion

    """

    def setUp(self):
        """Run before each test"""
        self.b1 = BaseModel()

    def tearDown(self):
        """Run after each testcase"""
        del self.b1

    # TEST EACH ATTRIBUTE WITH IT'S SPECIFICATIONS
    # id
    def test_id_exists(self):
        """test if id exists"""
        o1 = BaseModel()
        self.assertTrue(hasattr(o1, "id"))

    def test_id_type(self):
        """Test id type"""
        o1 = BaseModel()
        self.assertTrue(type(o1.id) is str)

    def test_id_unique(self):
        """test if id is unique"""
        b2 = BaseModel()

        self.assertNotEqual(self.b1.id, b2.id)

    # created_at
    def test_created_at_existence(self):
        """test created_at existence"""
        self.assertTrue(hasattr(self.b1, "created_at"))

    def test_created_at_attr_type(self):
        """Test the type of created_at"""
        self.assertTrue(type(self.b1.created_at) is datetime.datetime)

    def test_updated_at_existence(self):
        """test updated_at existence"""
        self.assertTrue(hasattr(self.b1, "updated_at"))

    def test_updated_at_attr_type(self):
        """Test the type of created_at"""
        self.assertTrue(type(self.b1.updated_at) is datetime.datetime)

    def test_equal_create_and_updatetime(self):
        """test if the create and update time are the same"""
        self.assertEqual(self.b1.created_at, self.b1.updated_at)

    def test_create_time_change(self):
        """test if 2 objects have diffenret create time"""
        b2 = BaseModel()
        self.assertNotEqual(self.b1.created_at, b2.created_at)

    # str method
    def test_str_format(self):
        """Test str method"""
        self.assertEqual(str(self.b1), "[BaseModel] ({}) {}".format(
            self.b1.id, self.b1.__dict__))

    # save method
    def test_save_method(self):
        """test save method's effect"""
        old_value = self.b1.updated_at
        sleep(1)
        self.b1.save()

        self.assertLess(old_value, self.b1.updated_at)

    # to_dict method
    def test_to_dict_return_type(self):
        """test to_dict return type"""
        self.assertTrue(type(self.b1.to_dict()) is dict)

    def test_to_dict_attributes(self):
        """test to_dict attributes"""
        self.b1.num = 1
        self.b1.nothing = "nothing"

        attributes = self.b1.to_dict()

        for key in self.b1.__dict__:
            self.assertTrue(key in attributes)

        self.assertTrue("__class__" in attributes)

    def test_to_dict_dates_format(self):
        """Test the format of created_at and updated_at"""
        created_at = self.b1.created_at.isoformat()
        updated_at = self.b1.updated_at.isoformat()

        attributes = self.b1.to_dict()

        self.assertEqual(created_at, attributes['created_at'])
        self.assertEqual(updated_at, attributes['updated_at'])


if __name__ == "__main__":
    unittest.main()
