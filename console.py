#!/usr/bin/python3
"""Console module for HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for the console using cmd"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        print("Exiting...")
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program (Ctrl+D)
        """
        print("Exiting...")
        return True

    def emptyline(self):
        """Print nothing if line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()