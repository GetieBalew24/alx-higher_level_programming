#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle

class Base:
    """Represent the base model.

    Represents the "base" for all other classes in this project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): Identityer of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs : A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
    @staticmethod
    def from_json_string(json_string):
        """Returns JSON strings in list """
        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attrs already set """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        # update temp with obj func update()
        temp.update(**dictionary)
        return temp
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances """
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        # Converting str to list
        text = cls.from_json_string(text)
        for item in text:
            # Formatting dicts into str format
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file"""
        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)
    
    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for key, value in dict(item).items():
                    res_dict[key] = int(value)
                # formatting with create()
                res.append(cls.create(**res_dict))
        return res
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles : A list of Rectangle objects to draw.
            list_squares : A list of Square objects to draw.
        """
        gui = turtle.Turtle()
        gui.screen.bgcolor("green")
        gui.pensize(3)
        gui.shape("turtle")
        gui.color("#ffffff")
        for rect in list_rectangles:
            gui.showturtle()
            gui.up()
            gui.goto(rect.x, rect.y)
            gui.down()
            for i in range(2):
                gui.forward(rect.width)
                gui.left(90)
                gui.forward(rect.height)
                gui.left(90)
            gui.hideturtle()
            
        gui.color("#b5e3d8")
        for sq in list_squares:
            gui.showturtle()
            gui.up()
            gui.goto(sq.x, sq.y)
            gui.down()
            for i in range(2):
                gui.forward(sq.width)
                gui.left(90)
                gui.forward(sq.height)
                gui.left(90)
            gui.hideturtle()
            
        turtle.exitonclick()
