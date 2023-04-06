#!/usr/bin/python3

""" Minimum Operations """


def minOperations(num):
    """
    a method that calculates the fewest number of operations 
    needed to result in exactly n H characters in the file.
    """
    if not isinstance(num, int):
        return 0

    op = 0
    itr = 2
    while (itr <= num):
        if not (num % itr):
            num = int(num / itr)
            op += itr
            itr = 1
        itr += 1
    return op
