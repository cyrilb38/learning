# Uses python3
import sys

def optimal_summands(n):
    summands = []
    current_count = n
    pointer = 1
    while current_count > 0:
        exp_diff = current_count - pointer
        if exp_diff == 0:
            summands.append(pointer)
            current_count -= pointer
        elif (exp_diff <= pointer) :
            pointer += 1
        else :
            summands.append(pointer)
            current_count -= pointer
            pointer += 1
            
        
    return summands

if __name__ == '__main__':
    i = input()
    n = int(i)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
