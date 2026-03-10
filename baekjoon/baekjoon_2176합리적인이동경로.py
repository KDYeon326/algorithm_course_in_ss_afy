import sys
import heapq

input = sys.stdin.readline


def dijkstra(n, graph):
    distance = [float('inf')] * (n + 1)
    hq = []

    distance[2] = 0
    heapq.heappush(hq, (0, 2))

    while hq:
        d, node = heapq.heappop(hq)

        if distance[node] < d:
            continue

        for nxt, cost in graph[node]:
            nd = d + cost

            if distance[nxt] > nd:
                distance[nxt] = nd
                heapq.heappush(hq, (nd, nxt))

    return distance

def dfs(node, graph, dist, dp):

    if node == 2:
        return 1

    if dp[node] != -1:
        return dp[node]

    dp[node] = 0

    for nxt, _ in graph[node]:

        if dist[node] > dist[nxt]:
            dp[node] += dfs(nxt, graph, dist, dp)

    return dp[node]


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

distance = dijkstra(n, graph)
dp = [-1] * (n + 1)

answer = dfs(1, graph, distance, dp)

print(answer)