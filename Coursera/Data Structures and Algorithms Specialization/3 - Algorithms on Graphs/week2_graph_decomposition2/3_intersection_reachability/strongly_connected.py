#Uses python3

import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

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


def reverse_adj(adj):
    rev_adj = defaultdict(list)
    for node in adj.keys():
        for neighbor in adj[node]:
            rev_adj[neighbor].append(node)
    return rev_adj

def number_of_strongly_connected_components(adj):
    rev_adj = reverse_adj(adj)
    result = 0
    visited = defaultdict(dict)
    #write your code here
    to_process = toposort(adj)
    for node in to_process:
        if node not in visited.keys():
            result += 1
            _, visited = dfs(rev_adj, node, 0, visited)
    return result

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
    print(number_of_strongly_connected_components(adj))
