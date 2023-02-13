#!/usr/bin/python3
""" Command interpreter for AirBnbClone console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Cmd class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """function to handle EOF"""
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
