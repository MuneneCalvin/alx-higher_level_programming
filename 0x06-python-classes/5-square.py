#!/usr/bin/bash

class Square:
    """class square that defines a square"""
    def __init__(self, size=0)
    """init square
    Args: value (int): size of the square.
    """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print('#', end='')
            print()
        else:
            print()

