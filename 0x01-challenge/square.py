#!/usr/bin/python3
""" Module for calculating a square"""


class square():
    """
    The Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Return the perimeter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ docstring """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ class caller"""

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
