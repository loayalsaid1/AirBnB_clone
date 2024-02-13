#!/usr/bin/python3
"""Test FileStorage class"""


import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Run before any testcase"""
        FileStorage._FileStorage__objects.clear()

        self.b1 = BaseModel()

    def tearDown(self):
        """Run after each testcase"""
        FileStorage._FileStorage__objects.clear()

        del self.b1

    def test_None_file_storage(self):
        """Test by passing None to filestorage"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_attributes(self):
        """Test the attibutes of the class"""
        # Attributes
        self.assertTrue(hasattr(FileStorage,
                                "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage,
                                "_FileStorage__objects"))

        # Types
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """Test all method"""
        obj1 = self.b1
        obj2 = BaseModel()

        FileStorage._FileStorage__objects = {"id1": obj1, "id2": obj2}

        expected = {"id1": obj1, "id2": obj2}
        self.assertEqual(FileStorage().all(),  expected)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        FileStorage().new(obj)

        self.assertIn(obj, FileStorage._FileStorage__objects.values())
