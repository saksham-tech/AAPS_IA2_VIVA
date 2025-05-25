
from bintrees import RBTree
tree = RBTree()
for val in [20, 15, 25, 10, 5]:
    tree.insert(val, val)
print(list(tree.items()))
