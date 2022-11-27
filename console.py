#!/usr/bin/python3
"""
Command Line implemntation for Air BnB clone
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command Line 
    """

    prompt = "(hbnb) "
    allModels = {"BaseModel":BaseModel}

    def do_quit(self, line):
        """Exit program"""
        return True

    def do_EOF(self, line):
        """Exit program (EOF)"""
        return True

    def emptyline(self):
        """Empty line"""
        return

    def do_create(self, line):
        """Create class"""
        if line != "":
            if line in self.allModels.keys():
                newInst = self.allModels[line]()
                newInst.save()
                print(newInst.id)
            else:
                print("** class doesn't exist ** ")
        else:
            print("** class name missing **")
        
    def do_show(self, line):
        """
        Show string representation of a instance based on class name and id
        """
        line_ent = line.split(" ")
        all_inst = storage.all()


        if len(line) == 0:
            print("** class name missing **")
        
        elif line_ent[0] not in self.allModels:
            print("** class doesn't exist **")

        else:
            try:
                if line_ent[1]:
                    name = "{}.{}".format(line_ent[0], line_ent[1])
                    if name not in all_inst.keys():
                        print("** no instance found **")
                    else:
                        print(all_inst[name])
            except IndexError:
                print("** instance Id missing **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()