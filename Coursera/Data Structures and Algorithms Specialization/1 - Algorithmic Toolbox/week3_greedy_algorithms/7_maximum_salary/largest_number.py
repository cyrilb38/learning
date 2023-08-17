#Uses python3

import sys
from functools import cmp_to_key

def compare_largest_number(x, y):
    """
    custom compare function which look for the biggest number
    x and y are string
    """
    if x == y:
        return 0
    elif int(x + y) > int(y + x):
        return -1
    else:
        return 1

def largest_number(a):
    #write your code here
    return "".join(sorted(a, key=cmp_to_key(compare_largest_number)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
