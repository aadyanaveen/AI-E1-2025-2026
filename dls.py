# Depth-Limited Search (DLS) with User Input

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
        child = inpu4t("Enter child node: ")
        nodes[parent].children.append(nodes[child])
    
    return nodes[root_val]


def depth_limited_search(root, limit):
    def dls_recursive(node, depth):
        if node is None:
            return
        
        print(node.value, end=" ")
        
        if depth == limit:
            return
        
        for child in node.children:
            dls_recursive(child, depth + 1)
    
    dls_recursive(root, 0)


# ------------------ Main ------------------

root = build_tree()

limit = int(input("Enter depth limit: "))

print("DLS Traversal:")
depth_limited_search(root, limit)