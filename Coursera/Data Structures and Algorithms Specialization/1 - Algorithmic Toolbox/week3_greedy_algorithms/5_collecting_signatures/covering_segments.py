# Uses python3
import sys
import heapq

def optimal_points(segments):
    points = []
    #write your code here
    while segments:
        _, end = heapq.heappop(segments)
        # tant que le prochain segment ne commence pas plus loin que la fin la plus proche, on le prend
        while segments and (end >= segments[0][0]):
            _, current_end = heapq.heappop(segments)
            end = min(current_end, end)
        points.append(end)
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        s = tuple([int(x) for x in input().split()])
        heapq.heappush(segments, s) 

    points = optimal_points(segments)
    print(len(points))
    print(*points)
