# python3

import sys
import threading
from collections import defaultdict


def compute_height(n, parents):
    g = defaultdict(list)
    # implement graph
    for node, parent in enumerate(parents):
        if parent != -1:
            g[parent].append(node)
        else :
            root = node
    
    # breadth first search
    to_explore = [root]
    visited = {root : 1}
    max_depth = 1
    while to_explore:
        current_node = to_explore.pop(0)
        for n in g[current_node]:
            if n not in visited.keys():
                visited[n] = visited[current_node] + 1
                to_explore.append(n)
                if (visited[current_node] + 1) > max_depth:
                    max_depth = visited[current_node] + 1
    return max_depth

# print(compute_height("5" , [int(x) for x in "4 -1 4 1 1".split(" ")]))

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
