import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
edges = []

for _ in range(M):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))
    edges.append((u, v, l))

dist = [float('inf')] * (N + 1)
hq = []

for _ in range(K):
    shopping_mall = int(input())
    dist[shopping_mall] = 0
    heapq.heappush(hq, (0, shopping_mall))

while hq:
    d, u = heapq.heappop(hq)

    if d > dist[u]:
        continue

    for v, l in graph[u]:
        if dist[v] > d + l:
            dist[v] = d + l
            heapq.heappush(hq, (dist[v], v))

# 오사오입 방지
max_dist_2x = 0

for i in range(1, N + 1):
    if dist[i] * 2 > max_dist_2x:
        max_dist_2x = dist[i] * 2

for u, v, l in edges:
    edge_val = dist[u] + dist[v] + l
    if edge_val > max_dist_2x:
        max_dist_2x = edge_val

# 원래 값 = max_dist_2x / 2
# 사구오입 반올림 적용: (max_dist_2x + 1) // 2
print((max_dist_2x + 1) // 2)