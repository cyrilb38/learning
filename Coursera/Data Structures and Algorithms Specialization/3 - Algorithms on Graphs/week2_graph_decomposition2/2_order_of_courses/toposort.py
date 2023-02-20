#Uses python3

import sys
from collections import defaultdict

def dfs(adj, node, time, visited):
    #write your code here
    time += 1
    # print(node, visited, time)
    visited[node]["pre"] = time
    for neighbor in adj[node]:
        if neighbor not in visited.keys():
            time, visited = dfs(adj, neighbor, time, visited)
    time+= 1
    visited[node]["post"] = time
    return time, visited


def toposort(adj):
    visited = defaultdict(dict)
    time = 0
    for node in adj.keys():
        if node not in visited.keys():
            time, visited = dfs(adj, node, time, visited)
    #write your code here
    return [k for k, v in sorted(visited.items(), key=lambda item: -item[1]["post"])]


# test = {
#     "A" : ["B"],
#     "B" : ["C"],
#     "C" : ["D"],
#     "D" : [],
#     "E" : ["F"],
#     "F" : []
# }
# print(toposort(test))

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
    order = toposort(adj)
    for x in order:
        print(x, end=' ')

