# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    pointer = 0
    index = 0
    count = 0
    while (pointer < distance) and (index < len(stops)-1):
        while (stops[index] < pointer + tank) and (index < len(stops)-1):
            index += 1
        if stops[index] == pointer:
            return -1
        pointer = stops[index]
        count += 1
    if (pointer + tank) < distance:
        return -1
    return count

# print(compute_min_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_refills(700, 200, [100, 200, 300, 400]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
