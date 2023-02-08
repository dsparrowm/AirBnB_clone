#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits the command interpreter"""
        return True

    def do_EOF(self, line):
        """exits the command line usin EOF(^d)"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
