#.1) Write a Program to construct the binary tree in python.

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()





class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Example usage
if __name__ == "__main__":
    # Create nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Print the constructed binary tree
    print("Binary Tree Structure:")
    print("   1")
    print(" /   \\")
    print("2     3")
    print(" \\")
    print("  4")
    print("   \\")
    print("    5")
