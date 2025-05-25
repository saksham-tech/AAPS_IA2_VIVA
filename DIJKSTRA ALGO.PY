import heapq
from collections import defaultdict

def dijkstra(n, edges, start):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    heap = [(0, start)]
    dist = [float('inf')] * n
    dist[start] = 0
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

print(dijkstra(4, [[0,1,4], [0,2,1], [2,1,2], [1,3,1], [2,3,5]], 0))
