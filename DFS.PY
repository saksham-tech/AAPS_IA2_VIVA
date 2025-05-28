graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 5],
    4: [1],
    5: [2, 3]
}

def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for nei in graph[node]:
            dfs(nei, visited)

dfs(2)
#Time Complexity: O(V + E)
