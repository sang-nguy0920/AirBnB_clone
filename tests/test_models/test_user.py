#!/usr/bin/python3
""" Tests for this """

import unittest
import models
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

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

    def test_docstring(self):
        """ Testing that class docstring exists """
        self.assertIsNotNone(User.__doc__)

if __name__ == '__main__':
    unittest.main()
