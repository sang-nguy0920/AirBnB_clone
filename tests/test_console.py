#!/usr/bin/python3
""" Tests for this """


import unittest
from models.base_model import BaseModel
import sys


class TestConsole(unittest.TestCase):

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
        self.assertTrue(hasattr(Base, "do_EOF"))
        self.assertTrue(hasattr(Base, "do_quit"))
        self.assertTrue(hasattr(Base, "emptyline"))
        self.assertTrue(hasattr(Base, "do_help"))
        self.assertTrue(hasattr(Base, "non_inter_output"))
        self.assertTrue(hasattr(Base, "do_create"))
        self.assertTrue(hasattr(Base, "do_show"))
        self.assertTrue(hasattr(Base, "do_destroy"))
        self.assertTrue(hasattr(Base, "do_all"))
        self.assertTrue(hasattr(Base, "do_update"))
        self.assertTrue(Base.do_EOF.__doc__)
        self.assertTrue(Base.do_quit.__doc__)
        self.assertTrue(Base.emptyline.__doc__)
        self.assertTrue(Base.do_help.__doc__)
        self.assertTrue(Base.non_inter_output.__doc__)
        self.assertTrue(Base.do_create.__doc__)
        self.assertTrue(Base.do_show.__doc__)
        self.assertTrue(Base.do_destroy.__doc__)
        self.assertTrue(Base.do_all.__doc__)
        self.assertTrue(Base.do_update.__doc__)

    def task_17(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

if __name__ == '__main__':
    unittest.main()
