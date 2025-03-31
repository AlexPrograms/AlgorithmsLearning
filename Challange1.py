"""Find the nth smallest element in binary search tree"""


# Python code to find minimum value in BST
# using using iterationl
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find the minimum value in BST
def minValue(root):
    # base case
    if root is None:
        return -1

    curr = root

    # leftmost node is minimum, so move
    # till left is not None
    while curr.left is not None:
        curr = curr.left

    # returning the data at the leftmost node
    return curr.data


def minNthValue(minValue, root, k):
    if root is None:
        return -1
    i = 0

    curr = minValue
    while i!=k:
        curr = curr.right
        i += 1

    return curr


if __name__ == "__main__":
    # Representation of input binary search tree
    #        5
    #       / \
    #      4   6
    #     /     \
    #    3       7
    #   /
    #  1
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)
    root.left.left.left = Node(1)
    minV = minValue(root)
    print(minValue(root))
    print(minNthValue(minV, root, 3))

#Second challange depth for search on graph