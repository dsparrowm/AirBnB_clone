#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quits the command interpreter"""
        return True

    def do_EOF(self, line):
        """exits the command line usin EOF(^d)"""
        return True
    
    def do_create(self, line) :
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if self.line_ver(line, "create"):
            new_instance = BaseModel()
            print (new_instance.id)
            new_instance.save()
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if self.line_ver(line, "show"):
            args = line.split()
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            print(all_objs[key])
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if self.line_ver(line, "destroy"):
            args = line.split()
            key = f"{args[0]}.{args[1]}"
            all_objs = storage.all()
            del all_objs[key]
            storage.save()

    def do_all(self, line):
        all_objs = storage.all()
        args = line.split()
        res = []
        if len(args) == 0:
            for obj_id in all_objs.keys():
                val = all_objs[obj_id]
                res.append(val)
            print(res)
            

    def emptyline(self):
        pass

    def line_ver(self, arg, com):
        args = arg.split()
        if arg:
            if args[0] in ["BaseModel"]:
                if com in ["create","all"]:
                    return True
                elif com in["show", "destroy"]:
                    if len(args) > 1:
                        key = f"{args[0]}.{args[1]}"
                        all_objs = storage.all()
                        if key in all_objs.keys():
                            return True
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
            else:
                print ("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
