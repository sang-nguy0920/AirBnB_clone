#!/usr/bin/python3
""" Tests for this """

import unittest
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

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
        self.assertTrue(hasattr(Base, "all"))
        self.assertTrue(hasattr(Base, "new"))
        self.assertTrue(hasattr(Base, "save"))
        self.assertTrue(hasattr(Base, "reload"))
        self.assertTrue(Base.all.__doc__)
        self.assertTrue(Base.new.__doc__)
        self.assertTrue(Base.save.__doc__)
        self.assertTrue(Base.reload.__doc__)

if __name__ == '__main__':
    unittest.main()
