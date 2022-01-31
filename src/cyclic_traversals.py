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
}
# add neighbors, point E back to H to make a cyclic graph
# two loops: (H)->(G)->(E)->(H) and (H)->(F)->(E)->(H)
nodes["E"].neighbors = [nodes["H"]]
nodes["F"].neighbors = [nodes["E"]]
nodes["G"].neighbors = [nodes["E"]]
nodes["H"].neighbors = [nodes["F"], nodes["G"], nodes["I"], nodes["J"]] # main hub
nodes["I"].neighbors = [] # dead-end node
nodes["J"].neighbors = [] # dead-end node
print('node (H) neighbors-->', nodes["H"].neighbors)

# Depth First Traversal of the nodes graph
# nodes is cyclic, need to keep track of what nodes have been visited

# make new empty set to keep track of visited nodes, like a dictionary but just for keys
# gives us O(1) lookup to check if a node has been visited
# each node is a unique instance of the GraphNode class, even if there are duplicate values they are still unique objects with different memory addresses
visited = set()

def dft(node):
    # check if node has been visited
    if node not in visited:
        # currently visitind node, add it to the visited set
        visited.add(node)
        # do the desired operation
        print(node) # visit

        # do the depth first traversal for the neightbors
        for neighbor in node.neighbors:
            dft(neighbor)

# run on "H" node
dft(nodes["H"])
print("-----------------")

# Breadth First Traversal of the nodes graph
# use a queue instead of call stack to make our way through nodes
from collections import deque

def bft(node):
    # still need to keep track of visited nodes with a set
    bft_visited = set()
    # init the queue of nodes we need to visit, initialized with the start node
    q = deque([node])
    
    # loop while q has nodes in it
    while len(q) > 0:
        # pop node from the front of the queue
        current_node = q.popleft()
        # visit only nodes that haven't been visited
        if current_node not in bft_visited:
            # currently visiting node, add it to the visited set
            bft_visited.add(current_node)

            # do the desired operation
            print(current_node) # visit

            # add all the current_node's neighbors(connected nodes) to the queue
            for neighbor in current_node.neighbors:
                q.append(neighbor)

bft(nodes["H"])
