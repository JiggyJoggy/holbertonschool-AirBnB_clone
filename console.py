#!/usr/bin/python3
"""Console module for HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand
    Args:
        cmd (console)): cmd.Cmd
    Returns:
        True: creates loop"""
    prompt = "(hbnb)"

    def do_quit(self, *arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, *arg):
        """
        EOF command to exit the program (Ctrl+D)
        """
        return True

    def emptyline(self):
        """Print nothing if line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()