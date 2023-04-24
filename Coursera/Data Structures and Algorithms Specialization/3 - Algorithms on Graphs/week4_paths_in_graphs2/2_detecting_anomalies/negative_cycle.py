#Uses python3

import sys

def check_negative_cycle(adj, root):
    shortest_graph = {}
    for node in adj.keys():
        shortest_graph[node] = {}
        shortest_graph[node]["d"] = 10 ** 18 # equivalent to inf
        shortest_graph[node]["parent"] = None
    # source
    shortest_graph[root]["d"] = 0
    
    for _ in range(len(adj.keys())-1):
        # we go through every edge to relax them if possible
        for node in adj.keys():
            for edge in adj[node]:
                if (shortest_graph[edge[0]]["d"] > (shortest_graph[node]["d"] + edge[1])):
                    shortest_graph[edge[0]]["d"] = shortest_graph[node]["d"] + edge[1]
                    shortest_graph[edge[0]]["parent"] = node

    # last iteration to detect negative cycle
    for node in adj.keys():
        for edge in adj[node]:
            if (shortest_graph[edge[0]]["d"] > (shortest_graph[node]["d"] + edge[1])):
                return 1

    return 0

def negative_cycle(adj):
    #write your code here
    return check_negative_cycle(adj, list(adj.keys())[0])
    # for node in adj.keys():
    #     res = check_negative_cycle(adj, node)
    #     if res == 1:
    #         return 1
    # return 0



if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
    print(negative_cycle(adj))
