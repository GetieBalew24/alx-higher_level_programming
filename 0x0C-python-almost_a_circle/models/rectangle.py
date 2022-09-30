#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width : Width of the new Rectangle.
            height : Height of the new Rectangle.
            x : x coordinate of the new Rectangle.
            y : y coordinate of the new Rectangle.
            id : The identityer of the new Rectangle.
        Raises:
            TypeError: If the width or height is not an int.
            ValueError: If the width or height <= 0.
            TypeError: If the  x or y is not an int.
            ValueError: If the x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
