#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for the console using cmd"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program (Ctrl+D)
        """
        return True

    def emptyline(self):
        """Print nothing if line is empty"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
