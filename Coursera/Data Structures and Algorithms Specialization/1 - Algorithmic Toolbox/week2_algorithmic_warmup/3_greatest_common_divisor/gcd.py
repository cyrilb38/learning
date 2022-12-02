# Uses python3
import sys

def gcd_naive(a, b):
    maxounet = max([a, b])
    minounet = min([a, b])
    if minounet == 0:
        return maxounet
    else:
        return gcd_naive(minounet, maxounet % minounet)
    

if __name__ == "__main__":
    input = sys.stdin.read()
    # input = input()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
