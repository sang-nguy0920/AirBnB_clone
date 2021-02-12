#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ CMD class """
    prompt = '(hbnb)'
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_empty(self):
        pass

    def do_create(self, arg):
        if  len(arg) < 0:
            print("** class name missing **")
        if not arg:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
