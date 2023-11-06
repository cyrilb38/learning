# Uses python3
import sys

def optimal_sequence(n):
    T = {i : None for i in range(1, n+1)}
    T[1] = [1]

    for i in range(1, n+1):
        actions = [i+1, i*2, i*3]
        for el in actions:
            if el in T.keys():
                if (T[el] is None) or (len(T[el]) > (len(T[i]) + 1)):
                    T[el] = [el] + T[i]

    return reversed(T[n])

input = input()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
