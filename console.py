#!/usr/bin/python3
""" Entry point of the command interpreter """


import cmd
import models
from models.base_model import BaseModel
import sys
from models import storage
from models.user import User
from models.review import Review
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
import shlex

ourclasses = {"BaseModel": BaseModel, "City": City,
              "Place": Place, "Amenity": Amenity,
              "Review": Review, "State": State,
              "User": User}


class HBNBCommand(cmd.Cmd):
    """ CMD class """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ do_EOF method """
        return True

    def do_quit(self, line):
        """Quit command to exit the program """
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
        if not arg:
            print("** class name missing **")
        elif arg in ourclasses:  # check if arg is pat of dict of classes
            for key, value in ourclasses.items():  # iterate through our dict
                if key == arg:  # find matching arg in dict
                    new_instance = ourclasses[key]()  # creating a new instance

            storage.save()  # save to json file
            print(new_instance.id)  # print id
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ do_show method: Prints the string representation of an instance
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234. """
        toks = arg.split(" ")
        objs = storage.all()
        try:
            if len(toks) == 0:
                print("** class name missing **")
                return
            if toks[0] in ourclasses:  # if first arg matches to in ourclasses
                if len(toks) > 1:  # check if more than 1 argument
                    key = toks[0] + "." + toks[1]  # set key to <class name>.id
                    if key in objs:
                        show_obj = objs[key]
                        print(show_obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """ do_destroy method: Deletes an instance based on the class name
            and id (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234. """
        if not arg:
            print("** class name missing **")
            return
        toks = arg.split(" ")
        objs = storage.all()
        if toks[0] in ourclasses:
            if len(toks) < 2:
                print("** instance id missing **")
                return
            search_match = toks[0] + "." + toks[1]
            if search_match not in objs:
                print("** no instance found **")
            else:
                match_obj = objs[search_match]
                if match_obj:
                    destroy_obj = storage.all()
                    del destroy_obj["{}.{}"
                                    .format(type(match_obj)
                                            .__name__, match_obj.id)]
                    storage.save()
        else:
            print("** class doesn't exist **'")

    def do_all(self, arg):
        """ do_all method:  Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all. """
        objs = storage.all()
        all_instances = []
        if not arg:
            for name in objs:
                all_instances.append(objs[name].__str__())
            print(all_instances)
            return
        toks = arg.split(" ")
        if toks[0] in ourclasses:
            for name in objs:
                if name[0:len(toks[0])] == toks[0]:
                    all_instances.append(objs[name].__str__())
            print(all_instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ do_update method: Updates an instance based on the class name and
            id by adding or updating attribute (save the change into the JSON
            file).
            Ex:
            $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        objs = storage.all()
        toks = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if toks[0] in ourclasses:
            if len(toks) < 2:
                print("** instance id missing **")
                return
            search_match = toks[0] + "." + toks[1]
            if search_match not in objs:
                print("** no instance found **")
            if len(toks) < 3:
                print("** attribute name missing **")
            if len(toks) < 4:
                print("** value missing **")
            else:
                setattr(models.storage.all()[search_match], toks[2], toks[3])
                models.storage.all()[search_match].save()
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """ counts instances """
        toks = arg.split()
        objs = storage.all()
        count = 0
        for x in objs.keys():
            if toks[0] in x:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
