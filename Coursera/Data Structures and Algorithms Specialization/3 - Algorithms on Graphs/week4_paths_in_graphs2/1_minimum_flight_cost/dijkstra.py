#Uses python3

import sys
import queue
import heapq


def distance(adj, s, t):
    #write your code here
    h = []
    visited = set()
    # Initialization first node
    heapq.heappush(h, (0, s))
    while h:
        d, current_node = heapq.heappop(h)
        
        if current_node in visited:
            continue
        if current_node == t:
            return d
        
        visited.add(current_node)
        for edge in adj[current_node]:
            if edge[0] not in visited:
                heapq.heappush(h, (d + edge[1], edge[0]))
    return -1


if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
    s, t = map(int, input().split())
    print(distance(adj, s, t))
