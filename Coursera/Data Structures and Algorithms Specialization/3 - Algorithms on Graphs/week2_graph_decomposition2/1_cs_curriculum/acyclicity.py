#Uses python3

import sys
from collections import defaultdict


def acyclic(adj):
    visited = defaultdict(list)
    for node in adj:
        if node not in visited.keys():
            to_visit = [node]
            while to_visit:
                current_node = to_visit.pop()
                # print(visited, current_node)
                for neighbor in adj[current_node]:
                    if neighbor in visited[current_node]:
                        # print(visited, neighbor, current_node)
                        return 1
                    if neighbor not in visited.keys():
                        visited[neighbor] += visited[current_node]
                        visited[neighbor].append(current_node)
                        to_visit.append(neighbor)
    return 0

# test = {
#     "A" : ["B"],
#     "B" : ["C"],
#     "C" : ["D"],
#     "D" : ["A"],
# }
# print(acyclic(test))

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
    print(acyclic(adj))
