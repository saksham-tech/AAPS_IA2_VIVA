class FenwickTree:
    def __init__(self, n):
        self.tree = [0]*(n+1)

    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

arr = [1, 2, 3, 4, 5]
ft = FenwickTree(len(arr))
for i, val in enumerate(arr):
    ft.update(i+1, val)
print(ft.query(5))  # 15

#Time Complexity: O(log n)
