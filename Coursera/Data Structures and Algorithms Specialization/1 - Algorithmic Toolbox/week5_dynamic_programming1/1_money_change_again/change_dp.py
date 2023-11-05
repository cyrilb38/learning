# Uses python3
import sys

def get_change(m):
    #write your code here
    COINS = (1, 3, 4)

    T = {x : None for x in range(m+1)} # on prépopule le tableau
    T[0] = 0
    for i in range(1, max(COINS)):
        T[-i] = float("Inf")

    for i in range(1,m+1):
        T[i] = min(
            [T[i - coin] for coin in COINS]
        ) + 1
    
    return T[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
