# Iterative Deepening Depth-First Search (IDDFS)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree():
    nodes = {}
    
    n = int(input("Enter number of nodes: "))
    
    # Create nodes
    for i in range(n):
        val = input(f"Enter value of node {i+1}: ")
        nodes[val] = TreeNode(val)
    
    root_val = input("Enter root node value: ")
    
    e = int(input("Enter number of edges: "))
    
    # Build tree
    for i in range(e):
        parent = input("Enter parent node: ")
        child = input("Enter child node: ")
        nodes[parent].children.append(nodes[child])
    
    return nodes[root_val]


def dls(node, goal, limit, depth, visited_order):
    if node is None:
        return False
    
    visited_order.append(node.value)
    
    # Check if goal found
    if node.value == goal:
        return True
    
    # Stop if limit reached
    if depth == limit:
        return False
    
    # Explore children
    for child in node.children:
        if dls(child, goal, limit, depth + 1, visited_order):
            return True
    
    return False


def iddfs(root, goal, max_depth):
    for limit in range(max_depth + 1):
        visited_order = []
        print(f"\nIteration with depth limit = {limit}:")
        
        found = dls(root, goal, limit, 0, visited_order)
        
        print("Visited nodes:", " ".join(visited_order))
        
        if found:
            print(f"Goal node '{goal}' found at depth {limit}")
            return
    
    print(f"\nGoal node '{goal}' not found within depth limit")


# ------------------ Main ------------------

root = build_tree()

goal = input("Enter goal node to search: ")
max_depth = int(input("Enter maximum depth limit: "))

iddfs(root, goal, max_depth)