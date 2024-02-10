#!/usr/bin/python3
"""The main console to run, test and debug the AirBnB system"""


import cmd


class HBNBCommand(cmd.Cmd):
    """The console class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle the EOF"""
        return True

    def do_quit(self, line):
        """Handle the quit command to exit"""
        return True

    def emptyline(self):
        """Handle emptyline"""
        pass

    def help_EOF(self):
        """Document EOF"""
        print("EOF Signal to exit the program\n")

    def help_quit(self):
        """Document quit"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
