# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    window = deque([])
    # initialisation
    for i in range(m):
        # while last element of the list if inferior of the new element to be added, we delete it
        while (len(window) > 0) and (sequence[window[-1]] <= sequence[i]): 
            window.pop()
        window.append(i)
    maximums.append(sequence[window[0]])
    # print(window)
    for i in range(m, len(sequence)):
        while (len(window) > 0) and (sequence[window[-1]] <= sequence[i]): 
            window.pop()
        window.append(i)
        while window[0] <= (i -m):
            window.popleft()
        # print(window)
        maximums.append(sequence[window[0]])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

