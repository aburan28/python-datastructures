#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Adam Buran"
__version__ = ""
__contact__ = "aburan28@gmail.com"





def binarySearch(array, item):
    first = 0
    last = len(array) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
            return found
        
        
        
if __name__ == '__main__':
    test_array = [random.randint(0,100) for x in xrange(1000)]
    print(binarySearch(test_array, random.choice(test_array)))
    