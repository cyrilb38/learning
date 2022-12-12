# Uses python3
import sys

def gcd_naive(a, b):
    maxounet = max([a, b])
    minounet = min([a, b])
    if minounet == 0:
        return maxounet
    else:
        return gcd_naive(minounet, maxounet % minounet)

def lcm_naive(a, b):
    return int(a * b / gcd_naive(a, b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

