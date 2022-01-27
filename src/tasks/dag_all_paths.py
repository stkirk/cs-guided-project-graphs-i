# given a directed acyclic graph, DAG:
# write a function that can find all possible paths from node 0 -> N-1

# graph parameter is a list of connection lists
# example: node 0 connects to nodes 1 and 2 --> graph[0] = [1, 2]
# return a list of sorted paths lists

from collections import deque
from copy import copy


def dag_paths(graph):
    # calculate end node
    end_node = len(graph) - 1
    # init all_paths list to append to
    all_paths = []
    # perform breadth first traversal to end_node from node 0
    q = deque()
    # append start node, path always starts here
    q.append([0])
    while len(q) > 0:
        current_path = q.popleft()
        last_node_in_path = current_path[len(current_path) - 1]
        if last_node_in_path == end_node:
            all_paths.append(current_path)
        # otherwise, want to add next connection onto current path and append it to the q
        #connections is a list
        connections = graph[last_node_in_path]
        for node in connections:
            path_to_append_to = copy(current_path)
            path_to_append_to.append(node)
            q.append(path_to_append_to)
    
    return [sorted(path) for path in all_paths]


print(dag_paths([[1, 2],[3],[3],[4],[]])) # [[0,1,3,4], [0,2,3,4]]
'''
                (0)-->(1)
                 |     |
                 +     +
                (2)-->(3)
                       |
                       +
                      (4)
'''
