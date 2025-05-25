from collections import deque
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(2)
