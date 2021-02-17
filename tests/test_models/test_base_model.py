#!/usr/bin/python3
""" Tests for this """

import unittest
from models.base_model import BaseModel
import json


class TestBaseModel(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_documentation(self):
        """ Test that all methods exist and contain correct documentation """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "__str__"))
        self.assertTrue(hasattr(Base, "save"))
        self.assertTrue(hasattr(Base, "to_dict"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.__str__.__doc__)
        self.assertTrue(Base.save.__doc__)
        self.assertTrue(Base.to_dict.__doc__)

if __name__ == '__main__':
    unittest.main()
