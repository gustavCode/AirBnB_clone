#!/usr/bin/python3
"""
The Console
Contains entry point of our command intepreter
"""

import cmd
import json
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Overrides Cmd's emptyline to
        eliminate empty lines
        """
        pass

    def output_errors(self, line, num_of_args):
        """
        Displays error messages to the console

        Args:
            line(any): accept user input from command
            line
            num_of_args(int): number of input arguments
        """

        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        err_msg = ["** class name missing **",
                   "** class doesn't exist **",
                   "** instance id missing **",
                   "** no instance found **",
                   "** attribute name missing **",
                   "** value missing **"]

        if not line:
            print(err_msg[0])
            return 1
        args = line.split()

        if num_of_args >= 1 and args[0] not in classes:
            print(err_msg[1])
            return 1
        elif num_of_args == 1:
            return 0

        if num_of_args >= 2 and len(args) < 2:
            print(err_msg[2])
            return 1
        dt = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]

        if num_of_args >= 2 and key not in dt:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0

        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1

        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1

        return 0

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and
        prints the new instance's id

        Args:
            line(args): Arguments to enter with command
        """
        if (self.output_errors(line, 1) == 1):
            return
        args = line.split(" ")

        ob = eval(args[0])()
        ob.save()

        print(ob.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id

        Args:
            line(any): Arguments to enter with command
        """
        if (self.output_errors(line, 2) == 1):
            return
        args = line.split()
        dt = storage.all()
        
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(dt[key])

    def do_EOF(self, line):
        """
        Function to quit command intepreter
        with `Ctrl-D`

        Args:
            line(args): argument for quitting
            the terminal
        """

        "End of file command to exit program\n"
        return True

    def do_quit(self, line):
        """Function to quit command intepreter 
        bye typing `quit`

        Args:
            line(args): argument for quitting
            the terminal
        """

        "Quit command to exit program\n"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
