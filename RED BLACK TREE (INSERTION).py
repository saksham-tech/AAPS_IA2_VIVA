class Node:
    def __init__(self, data):
        self.data = data
        self.color = 1  # 1 for Red, 0 for Black
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.root = self.NULL

    def insert(self, data):
        node = Node(data)
        node.parent = None
        node.data = data
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # New node must be red

        parent = None
        current = self.root

        while current != self.NULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.data} (Red)" if node.color else f"{node.data} (Black)", end=" ")
            self.inorder(node.right)


# Example Usage
rbt = RedBlackTree()
values = [10, 20, 30, 15, 25, 5]
for val in values:
    rbt.insert(val)

print("Inorder traversal with node colors:")
rbt.inorder(rbt.root)
