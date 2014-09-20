"""
Implementation of BFS and Connected Components alg.
"""
from collections import deque


test_graph = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7, 8],
    5: [2, 9, 10],
    6: [2],
    7: [4, 11, 12],
    8: [4],
    9: [5],
    10: [5],
    11: [7],
    12: [7]
}


def bfs_visited(ugraph, start_node):
    """
    ugraph ->       undirected graph to search in
    start_node ->   start_node to search from
    return set of all nodes visited by algorithm
    """
    queue = deque()
    visited = set([start_node])
    queue.append(ugraph[start_node])
    while queue:
        nodes = queue.pop()
        for node in nodes:
            if node not in visited:
                visited.add(node)
                queue.append(ugraph[node])
    return visited

