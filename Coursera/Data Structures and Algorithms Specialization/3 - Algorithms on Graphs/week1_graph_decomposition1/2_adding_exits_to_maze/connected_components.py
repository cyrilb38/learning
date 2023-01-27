#Uses python3

import sys


def number_of_components(adj):
    count = 0
    rest_to_process = [x for x in adj.keys()]
    while rest_to_process:
        count += 1
        first_node = rest_to_process.pop(0)
        visited = [first_node]
        to_visit = adj[first_node]
        while to_visit:
            node = to_visit.pop(0)
            visited.append(node)
            if node in rest_to_process:
                rest_to_process.remove(node)
            for neighbor in adj[node]:
                if (neighbor not in to_visit) and (neighbor not in visited):
                    to_visit.append(neighbor)

    #write your code here
    return count

# test = {
#     "A" : ["B"],
#     "B" : ["A"],
#     "C" : ["D"],
#     "D" : ["C"],
# }
# print(number_of_components(test))

if __name__ == '__main__':
    adj = {}
    n, m = map(int, input().split())
    for node in range(1, n+1):
        adj[node] = []
    for edge in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(number_of_components(adj))
