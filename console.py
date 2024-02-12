#!/usr/bin/python3
"""The main console to run, test and debug the AirBnB system"""


import cmd
from models.base_model import BaseModel
from models import storage


classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """The console class"""

    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a instance of <args>[0] class"""
        args = args.split()
        if len(args) > 0:
            model = classes.get(args[0])
            if model is not None:
                obj = model()
                print(obj.id)
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """The help text of <create command"""
        print("Create an object of class <class name>"
                " and print its id")

    def do_show(self, args):
        """Show the string representation of an instance with
        class name and id"""
        args = args.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name missing **")
        elif args_len >= 1 and args[0] not in classes:
            print("** class doesn't exist **")
        elif args_len < 2:
            print("** instance id missing **")
        elif args_len >= 2 and f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            object_attributes = storage.all()[f"{args[0]}.{args[1]}"]
            obj = classes[args[0]](**object_attributes)
            print(obj)

    def help_show(self):
        """help of show"""
        print("show <class name> <id>")
        print("Print the string represenation of the object")

    def do_destroy(self, args):
        """delete an instance"""
        args = args.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name missing **")
        elif args_len >= 1 and args[0] not in classes:
            print("** class doesn't exist **")
        elif args_len < 2:
            print("** instance id missing **")
        elif args_len >= 2 and f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def help_destroy(self):
        """help of destroy"""
        print("destroy <class name> <id>")
        print("delete instanc of class <class name> with id <id>")

    # design of the function could be better without redundency
    def do_all(self, args):
        """Pritn all the instances saved, or all or certain class"""
        args = args.split()
        args_len = len(args)
        instances = []
        objects = storage.all()
        if args_len == 0:
            for key, value in objects.items():
                model = key.split(sep='.')[0]
                obj = classes[model](**value)
                instances.append(str(obj))
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            for key, value in objects.items():
                model = key.split(sep='.')[0]
                if model == args[0]:
                    obj = classes[model](**value)
                    instances.append(str(obj))
        print(instances)

    def help_all(self):
        """help all"""
        print("all [<class name>]")
        print("print either all the objects saved or all obejcts of"
                " <class name>")

    def do_update(self, args):
        """Update an attribute of an instance

            Usage: update <class> <id> <attr_name> <value>
        """
        args = args.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name missing **")
        elif args_len >= 1 and args[0] not in classes:
            print("** class doesn't exist **")
        elif args_len < 2:
            print("** instance id missing **")
        elif args_len >= 2 and f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif args_len < 3:
            print("** attribute name missing **")
        elif args_len < 4:
            print("** value missing **")
        else:
            model = classes[args[0]]
            obj_attrs = storage.all()[f"{args[0]}.{args[1]}"]
            value = args[3]
            if obj_attrs.get(args[2]):
                value = type(obj_attrs[args[2]])(value)
            obj_attrs[args[2]] = value
            storage.save()

    def help_update(self):
        """Help update"""
        print("Usage: update <class name> <id> <attribute> <value>")
        print("Update an attribute of an instance of a certain class")

    def do_EOF(self, line):
        """Handle the EOF"""
        return True

    def help_EOF(self):
        """Document EOF"""
        print("EOF Signal to exit the program\n")

    def do_quit(self, line):
        """Handle the quit command to exit"""
        return True

    def help_quit(self):
        """Document quit"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Handle emptyline"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
