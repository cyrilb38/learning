#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    to_visit = adj[x]
    found = False
    visited = [x]
    while to_visit and not found:
        current_node = to_visit.pop(0)
        visited.append(current_node)
        for neighbor in adj[current_node]:
            if neighbor == y:
                found = True
            elif (neighbor not in visited) and (neighbor not in to_visit):
                to_visit.append(neighbor)

    return int(found * 1)

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    x, y = map(int, input().split())
    print(reach(adj, x, y))
