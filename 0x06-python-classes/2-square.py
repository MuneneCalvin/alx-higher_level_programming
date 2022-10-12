#!/usr/bin/bash

class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size 

