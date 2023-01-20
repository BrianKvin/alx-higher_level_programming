#!/usr/bin/python3
"""Defines a rectangle model class."""
from models.base import Base


class Rectangle(Base):
    """class rectangle implements Base with the __init__() method"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor Initialize a rectangle
        or a public method
        Private instance attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        call the super class with id (this will use the __init__ logic)
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
        """sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Return's the rectangle's X value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value of the rectangle"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value of the rectangle"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """A public method def area(self) 
        that returns area value of the Rectangle instance
        """
        return (self.__width * self.__height)
