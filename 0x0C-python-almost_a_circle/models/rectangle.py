#!/usr/bin/python3
"""Defines a rectangle model class."""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor Initialize a rectangle
        Private instance attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        class the super class with id (this will use the __init__ logic)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle
        if type(value) != int:
            raise TypeError('Width must be an integer')
        if value <= 0:
            raise ValueError('Width must be > 0')
        self.__width = value
        """

    @property
    def height(self):
        """Returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """Return's the rectangle's X value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """Returns the value of y"""
        self.__y

    @y.setter
    def y(self, value):
    """sets the y value of the rectangle"""
    self.__y = value
