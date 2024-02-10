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
        self.b1 = BaseModel()
        

    def tearDown(self):
        """Run after each testcase"""
        del self.b1
    
    def test_None_file_storage(self):
        """Test by passing None to filestorage"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_attributes(self):
        """Test the attibutes of the class"""
        # Attributes
        self.assertTrue(hasattr(FileStorage,
                                "_File_Storage__file_path"))
        self.assertTrue(hasattr(FileStorage,
                                "_File_Storage__objects"))
        
        # Types
        self.assertIsInstance(FileStorage._File_Storage__file_path, str)
        self.assertIsInstance(FileStorage._File_Storage__objects, dict)

    def test_all(self):
        """Test all method"""
        storage = FileStorage()
        attrs = self.b1.to_dict()
        storage._FileStorage__objects.update(attrs)
        attrs2 = BaseModel().to_dict()
        storage._FileStorage__objects.update(attrs2)
        
        

        self.assertEqual(storage.all(), attrs.update(attr))
