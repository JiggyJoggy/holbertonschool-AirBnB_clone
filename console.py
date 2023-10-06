#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The command line"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True
    
    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
