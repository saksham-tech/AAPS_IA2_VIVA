class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = None
for val in [5, 3, 7, 2, 4, 6, 8]:
    root = insert(root, val)
inorder(root)

#Time Complexity: O(log n)
