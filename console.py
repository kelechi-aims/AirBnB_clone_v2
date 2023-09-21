#!/usr/bin/python3
"""This is the console for AirBnB"""

import cmd
import os
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """This class is the entry point of the command interpreter"""
    
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at the end of the file"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            obj = eval("{}()".format(my_list[0]))
            for arg in my_list[1:]:
                if "=" in arg:
                    pair = arg.split("=")
                    key = pair[0]
                    value = pair[1]
                    if value[0] == value[-1] == '"':
                        value = value.replace("_", " ")
                        value = value.split('"')[1]
                        value = value.split('"')[0]
                    else:
                        try:
                            value = int(value)
                        except:
                            try:
                                value = float(value)
                            except:
                                continue
                obj.__dict__[key] = value
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    # Other methods like do_show, do_destroy, do_all, do_update, count, etc.

if __name__ == '__main__':
    HBNBCommand().cmdloop()
