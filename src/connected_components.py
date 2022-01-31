# Connected components are like islands
# Same graph but no connection between vert clusters
# example - road maps for Hawaii and California

# The problem: have access to all the nodes in a graph, how many connected components are in the graph?
# How many islands not connected to other islands?

# Plan: have a list of all the nodes, visit a node and traverse its connections and keep of log of nodes that have been visited
# once you've traversed all the nodes in that island, increment a count and repeat until all nodes in the graph have been visited
'''
for each node in the graph:
    if the node isn't visited:
        increment the counter
        traverse from that node and mark all its connected nodes as visited
return the counter
'''
# example of what a graph could look like in this situation: adjacenecy list
example_graph = [
    [1], # places node 0 goes
    [0,2], # places node 1 goes
    [1], # places node 2 goes
    [4, 6], # places node 3 goes
    # ...etc
]
from collections import deque
# There is a baking class with N students where some students are friends with others
# via the transitive property of direct friendships, friends of friends, etc. friend circles have formed
# friend circles represent connected components
# Given an N*N matrix, friendships, return how many friend circles are in the class

# def friend_circles(friendships):
#     # init a counter
#     count = 0
#     # nodes look like this: friendships[i]
#     # connections look like this: friendships[i][j]; if node i is friends with node j this value will be 1, if they aren't its 0
    
#     labeled_friendships = [(i, arr) for i, arr in enumerate(friendships)]
#     visited = set()
#     to_visit = deque(labeled_friendships)
#     # to_visit.append((0, friendships[0]))
#     while len(to_visit) > 0:
#         current_node = to_visit.popleft()
#         if current_node[0] not in visited:
#             print("currentnode b4 count", current_node)
#             count += 1
#             # visited.add(current_node[0])
#         for i, friend in enumerate(current_node[1]):
#             if friend == 1:
#                 print("friend", i)
#                 visited.add(i)

#     return count

def friend_circles(friendships):
    # init a counter
    count = 0
    # nodes look like this: friendships[i]
    # connections look like this: friendships[i][j]; if node i is friends with node j this value will be 1, if they aren't its 0
    
    labeled_friendships = [(i, arr) for i, arr in enumerate(friendships)]
    visited = set()
    to_visit = deque(labeled_friendships)
    # to_visit.append((0, friendships[0]))
    while len(to_visit) > 0:
        current_node = to_visit.popleft()
        if current_node[0] not in visited:
            print("currentnode b4 count", current_node)
            count += 1
            # visited.add(current_node[0])
        for i, friend in enumerate(current_node[1]):
            if friend == 1:
                print("friend", i)
                visited.add(i)

    return count


print(friend_circles([
    [1,1,0,0],
    [1,1,0,1],
    [0,0,1,0],
    [0,1,0,1]
])) # 2
print(friend_circles([
    [1,1,0],
    [1,1,1],
    [0,1,1]
])) # 1