#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
         Args:
            *args (ints): New attribute values.
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
    def update(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()
    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
    def __str__(self):                 
        """Return the print() and str() representation of a Square."""      
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)  
