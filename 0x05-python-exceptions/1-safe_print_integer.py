#!/usr/bin/bash

def safe_print_interger(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

