#!/usr/bin/python3
import sys

def uppercase(s):
    for iterator in s:
        temp = iterator
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(iterator) - 32)
        sys.stdout.write("{}".format(temp))
    print()
