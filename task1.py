class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key == root.value:
            print(f"The value {key} already exists in the tree, duplicates are not allowed.")
        elif key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_maximum(root):
    if root is None:
        return "Empty tree"
    current = root
    while current.right is not None:
        current = current.right
    return current.value

def find_minimum(root):
    if root is None:
        return "Empty tree"
    current = root
    while current.left is not None:
        current = current.left
    return current.value

def find_sum(root):
    if root is None:
        return 0
    return root.value + find_sum(root.left) + find_sum(root.right)

# Function to print the results
def print_results(root):
    print(f"Binary Search Tree:\n{root}")
    print(f"Maximum value: {find_maximum(root)}")
    print(f"Minimum value: {find_minimum(root)}")
    print(f"Sum of all values: {find_sum(root)}")

# Test code with improvements
root = Node(10)
root = insert(root, 4)
root = insert(root, 9)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 18)
root = insert(root, 16)
root = insert(root, 11)


print_results(root)
