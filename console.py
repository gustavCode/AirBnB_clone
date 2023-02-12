#!/usr/bin/python3
"""
The Console
Contains entry point of our command intepreter
"""

import cmd
import re
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

def do_destroy(self, line):
        """
        Deletes an instance of a certain class.
        
        Args:
            line(args): to enter with command: <class name> <id>
        """
        if (self.output_errors(line, 2) == 1):
            return
        args = line.split()
        dt = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del dt[key]
        storage.save()

    def do_all(self, line):
        """
        Shows all instances, or instances of a certain class
        
        Args: 
            line(args): enter with command (optional): <class name>
        """
        dt = storage.all()
        if not line:
            print([str(x) for x in dt.values()])
            return
        args = line.split()
        if (self.output_errors(line, 1) == 1):
            return
        print([str(v) for v in d.values()
               if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating an attribute
        
        Args:
            line(args): receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
        """
        if (self.output_errors(line, 4) == 1):
            return
        args = line.split()
        dt = storage.all()
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        attr_k = args[2]
        attr_v = args[3]
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        class_attr = type(dt[key]).__dict__
        if attr_k in class_attr.keys():
            try:
                attr_v = type(class_attr[attr_k])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(dt[key], attr_k, attr_v)
        storage.save()

    def my_count(self, class_n):
        """
        Method counts instances of a certain class
        """
        count_instance = 0
        for instance_object in storage.all().values():
            if instance_object.__class__.__name__ == class_n:
                count_instance += 1
        print(count_instance)

    def default(self, line):
        """
        Method to take care of following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation)
        """
        names = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

        commands = {"all": self.do_all,
                    "count": self.my_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update}

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
        if not args or len(args) < 2 or args[0] not in names \
                or args[1] not in commands.keys():
            super().default(line)
        return

        if args[1] in ["all", "count"]:
            commands[args[1]](args[0])
        elif args[1] in ["show", "destroy"]:
            commands[args[1]](args[0] + ' ' + args[2])
        elif args[1] == "update":
            params = re.match(r"\"(.+?)\", (.+)", args[2])
            if params.groups()[1][0] == '{':
                dic_p = eval(params.groups()[1])
                for k, v in dic_p.items():
                    commands[args[1]](args[0] + " " + params.groups()[0] +
                                      " " + k + " " + str(v))
            else:
                rst = params.groups()[1].split(", ")
                commands[args[1]](args[0] + " " + params.groups()[0] + " " +
                                  rst[0] + " " + rst[1])

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
