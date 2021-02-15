#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    """ CMD class """
    prompt = '(hbnb) '
    def do_EOF(self, line):
        """ do_EOF method """
        return True

    def do_quit(self, line):
        """ do_quit method """
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_help(self, *args):
        """ do_help method """
        self.non_inter_output()
        cmd.Cmd.do_help(self, *args)

    @staticmethod
    def non_inter_output():
        """ non_inter_output method: trying to get correct output """
        if sys.stdin.isatty() is False:
            print("")

    def do_create(self, arg):
        """ do_create method """
        if  len(arg) < 0:
            print("** class name missing **")
        if not arg:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
