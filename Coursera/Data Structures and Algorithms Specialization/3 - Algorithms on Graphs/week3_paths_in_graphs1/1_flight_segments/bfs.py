#Uses python3

import sys
import queue

def distance(adj, s, t):
    to_process = queue.Queue()
    to_process.put(s)
    visited = {s : 0}
    while not to_process.empty():
        current_node = to_process.get()
        for neighbor in adj[current_node]:
            if neighbor not in visited.keys():
                visited[neighbor] = visited[current_node]  + 1
                to_process.put(neighbor)
            if neighbor == t:
                break
    
    if t in visited.keys():
        return visited[t]
    return -1

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    s, t = map(int, input().split())
    print(distance(adj, s, t))
