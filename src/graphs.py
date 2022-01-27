# Graphs
# If you can get the neighbors for a node, you can run graph algorithms on them

# Adjacency List Representation: uses list or dictionary to store connections
class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        # for linked list we had next, trees have left and right
        self.connections = [] #<-- adjacency list
        # Alternate adjacency list with a dictionary
        self.adj_dict = {
            "E": ["F", "G"],
            "F": ["E", "H"],
            #...
        }

# Adjacency Matrix Representation:
# A matrix is a 2d array, kind of looks like multiplication table or grid
# 1's denote something is connected, 0's no connection
# any number other than zero indicates a connection with its value relating to the edge weight

'''
  | A B C D
  ---------
A | 0 1 0 0
B | 1 0 0 0
C | 1 1 1 0
D | 0 0 0 1
'''
adjacency_matrix = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
]
if adjacency_matrix[0][1] == 1:
    print("there's a connection between A and B")

# What is A connected to?
connections_a = [i for i, v in enumerate(adjacency_matrix[0]) if v == 1]


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
# add neightbors
nodes["E"].neighbors = []
nodes["F"].neighbors = [nodes["E"]]
nodes["G"].neighbors = [nodes["E"]]
nodes["H"].neighbors = [nodes["F"], nodes["G"], nodes["I"], nodes["J"]]
nodes["I"].neighbors = []
nodes["J"].neighbors = []
print(nodes["H"].neighbors)

# Depth First Traversal of the nodes graph (acyclic: can't get caught in a loop)

def dft(n):
    print(n) # visit

    for neighbor in n.neighbors:
        dft(neighbor)

# run on "H" node
dft(nodes["H"])
