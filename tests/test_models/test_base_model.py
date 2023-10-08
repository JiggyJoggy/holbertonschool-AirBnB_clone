#!/usr/bin/python3
"""Unittest classes"""
import unittest
from models.base_model import BaseModel
from genericpath import exists


class TestBaseModel(unittest.TestCase):
    """Instances method tests"""
    def settingUp(self):
        self.test1 = BaseModel()
        self.test2 = BaseModel()

    def tearDown(self):
        del self.test1
        del self.test2

    def test_id(self):
        self.assertTrue(self.test1.id, exists)
        self.assertTrue(self.test2.id, exists)
        self.assertTrue(type(self.test1.id) is str)
        self.assertTrue(type(self.test2.id) is str)
        self.assertEqual(len(self.test1.id), 36)
        self.assertEqual(len(self.test2.id), 36)
        self.assertNotEqual(self.test1.id, self.test2.id)

    def test_created_at(self):
        self.assertTrue(self.test1.created_at, exists)
        self.assertTrue(self.test2.created_at, exists)
        self.assertNotEqual(self.test1.created_at, self.test2.created_at)

    def test_updated_at(self):
        self.assertTrue(self.test1.updated_at, exists)
        self.assertTrue(self.test2.updated_at, exists)
        self.assertEqual(self.test1.created_at, self.test1.updated_at)
        self.assertEqual(self.test2.created_at, self.test2.updated_at)
        self.assertNotEqual(self.test1.updated_at, self.test2.updated_at)

class TestBaseModel_str(unittest.TestCase):
    """__str__ tests"""


class TestBaseModel_to_dict(unittest.TestCase):
    """Dictionary tests"""
    


if __name__ == '__main__':
    unittest.main()