#Uses python3

import sys
import queue

def bipartite(adj):
    visited = {}
    for node in adj.keys():
        if node not in visited:
            to_process = queue.Queue()
            to_process.put(node)
            visited[node] = 0
            while not to_process.empty():
                current_node = to_process.get()
                for neighbor in adj[current_node]:
                    if neighbor not in visited.keys():
                        visited[neighbor] = (visited[current_node]  + 1) % 2
                        to_process.put(neighbor)
                    else : # check if it is the same kind
                        if visited[neighbor] == visited[current_node]:
                            return 0

    return 1

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(bipartite(adj))
