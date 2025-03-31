#Find the nth smallest element in binary search tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find the minimum value in BST
def min_value(root):
    if root is None:
        return -1

    curr = root
    i = 0
    # leftmost node is minimum, so move
    # till left is not None
    while curr.left is not None:
        curr = curr.left
        i += 1

    # returning the data at the leftmost node
    return curr.data, i

def difference(n):
    i = minV[1]
    diff = i - n
    return diff

def min_n_th_value(root, diff):
    print(diff)
    curr = root
    while diff != 0:
        curr = curr.left
        print(curr.data)
        diff -= 1
    return curr.data

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(18)
    root.right = Node(26)
    root.left.left = Node(13)
    root.right.right = Node(27)
    root.left.left.left = Node(10)
    root.left.left.left.left = Node(8)
    minV = min_value(root)
    print(f"Min Value: {min_value(root)[0]}")
    #print(min_n_th_value(root, 3))
    new_current = root
    n = 3
    diff = difference(n)
    print(f"Smallest and {n}th smallest index difference: {diff}")
    min_n_v = min_n_th_value(new_current, diff)
    #print(diff)
    print(f"{n}th smallest: {min_n_v}")
