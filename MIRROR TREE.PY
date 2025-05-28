def mirror(root):
    if root:
        root.left, root.right = mirror(root.right), mirror(root.left)
    return root

#Time Complexity: O(n)
