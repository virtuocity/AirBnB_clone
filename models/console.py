#!/usr/bin/python3
""" Command interpreter for AirBnbClone console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Cmd class"""
    prompt = '(hbnb) '

    def preloop(self):
        """
        handles intro to command interpreter
        """
        print('.----------------------------.')
        print('|    Welcome to hbnb CLI!    |')
        print('|   for help, enter \'help\'   |')
        print('|   To quit, enter \'quit\'   |')
        print('.----------------------------.')

    def postloop(self):
        """
        handles exit to command interpreter
        """
        print('.----------------------------.')
        print('|  Nagayat!  |')
        print('.----------------------------.')


    def do_quit(self, line):
        """quit: quit
        USAGE: Command to quit the program
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
