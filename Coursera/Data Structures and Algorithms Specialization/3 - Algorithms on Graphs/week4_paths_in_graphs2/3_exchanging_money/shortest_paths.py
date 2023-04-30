#Uses python3

import sys
import queue


def shortest_paths(adj, s):
    #write your code here
    shortest_graph = {}
    for node in adj.keys():
        shortest_graph[node] = {}
        shortest_graph[node]["d"] = float("inf")
        shortest_graph[node]["parent"] = None
    # source
    shortest_graph[s]["d"] = 0
    
    for _ in range(len(adj.keys())-1):
        # we go through every edge to relax them if possible
        for node in adj.keys():
            for edge in adj[node]:
                if (shortest_graph[edge[0]]["d"] > (shortest_graph[node]["d"] + edge[1])):
                    shortest_graph[edge[0]]["d"] = shortest_graph[node]["d"] + edge[1]
                    shortest_graph[edge[0]]["parent"] = node

    # last iteration to detect negative cycle
    nodes_to_check = set()
    for node in adj.keys():
        for edge in adj[node]:
            if (shortest_graph[edge[0]]["d"] > (shortest_graph[node]["d"] + edge[1])) and (shortest_graph[edge[0]] != float("inf")):
                nodes_to_check.add(edge[0])

    # identify all nodes in negative cycle
    visited = set()
    if nodes_to_check:
        for node in nodes_to_check:
            # getting to the cycle
            for _ in range(len(adj.keys())):
                node = shortest_graph[node]["parent"]
            first_node_in_cycle = node
            # going upstream to get all the nodes from the cycle
            while shortest_graph[node]["parent"] != first_node_in_cycle:
                shortest_graph[node]["d"] = "-"
                # all the nodes that are connected to this node needs to be tagged as such
                to_visit = [x[0] for x in adj[node] if x[0] not in visited]
                while to_visit:
                    neighbor_node = to_visit.pop()
                    visited.add(neighbor_node)
                    shortest_graph[neighbor_node]["d"] = "-"
                    for connected_node in adj[neighbor_node]:
                        if (connected_node[0] not in visited) and (connected_node[0] not in to_visit):
                            to_visit.append(connected_node[0])
                
                node = shortest_graph[node]["parent"] 

    return shortest_graph


if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
    s = int(input())

    res = shortest_paths(adj, s)
    for x in range(1,len(res)+1):
        if res[x]["d"] == float("inf"):
            print("*")
        else:
            print(res[x]["d"])

