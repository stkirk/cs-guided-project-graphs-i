class GraphNode:
    def __init__(self, value) -> None:
        self.value = value
        # for linked list we had next, trees have left and right
        self.neighbors = [] #<-- adjacency list of connections
    def __repr__(self) -> str:
        return f"Node({repr(self.value)})"

# dictionary of nodes to work with:
nodes = {
    "E": GraphNode("E"),
    "F": GraphNode("F"),
    "G": GraphNode("G"),
    "H": GraphNode("H"),
    "I": GraphNode("I"),
    "J": GraphNode("J"),
    "A": GraphNode("A")
}
# add neighbors, point E back to H to make a cyclic graph
# two loops: (H)->(G)->(E)->(H) and (H)->(F)->(E)->(H)
nodes["E"].neighbors = [nodes["H"], nodes["A"]]
nodes["F"].neighbors = [nodes["E"]]
nodes["G"].neighbors = [nodes["E"], nodes["A"]]
nodes["H"].neighbors = [nodes["F"], nodes["G"], nodes["I"], nodes["J"]] # main hub
nodes["I"].neighbors = [] # dead-end node
nodes["J"].neighbors = [] # dead-end node
nodes["A"].neighbors = [] # dead-end node

from collections import deque

# Breadth first search
def shortest_path(start, end):
    # still need to keep track of visited nodes with a set
    visited = set()
    # init the queue of nodes we need to visit
    to_visit = deque()
    # we want the queue to store a tuple and keep track of two things: 
    # the place we need to visit and the path it took to get there
    to_visit.append((start, [start]))
    
    # loop while q has nodes in it
    while len(to_visit) > 0:
        # pop front of the queue, which is a tuple with the node to visit and the path it took to get there 
        current_node, path_so_far = to_visit.popleft()
        # visit only nodes that haven't been visited, keeping track in visited set
        print('current_node-->', current_node, 'path so far-->', path_so_far)
        # if current node is the end node, return the path
        if current_node == end:
            return path_so_far

        if current_node not in visited:
            # currently visiting node, add it to the visited set
            visited.add(current_node)

            # do the desired operation
            # print('current_node-->', current_node) # visit

            # add all the current_node's neighbors(connected nodes) and a copy of the path we've taken so far plus the neighbor node
            for neighbor in current_node.neighbors: # if neighbors aren't built in to current_node, write a helper function outside of this function and invoke it here to get the neighbor nodes

                to_visit.append((neighbor, path_so_far + [neighbor])) # concatenating two lists with a plus sign creates a new list, don't want to mutate original path_so_far
    
    # if we get here, there was no route to the end node
    return None

print(shortest_path(nodes["H"], nodes["A"]))
print(shortest_path(nodes["I"], nodes["G"]))
