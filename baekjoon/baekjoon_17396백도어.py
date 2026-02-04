import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

view = list(map(int, input().split()))
# 상대 넥서스(N-1)는 시야가 있어도 갈 수 있으므로 0으로
view[N - 1] = 0

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    # 시야가 있는 분기점으로 연결된 간선은 여기서 무시
    if view[u] == 1 or view[v] == 1:
        continue
    graph[u].append((v, t))
    graph[v].append((u, t))

INF = float('inf')
distance = [INF] * N
distance[0] = 0

# 힙 큐 (누적 시간, 현재 노드)
hp = [(0, 0)]

while hp:
    accumulated_time, current = heapq.heappop(hp)

    # 이미 확인한 거리보다 길다면 무시
    if distance[current] < accumulated_time:
        continue

    for neighbor, weight in graph[current]:
        new_time = accumulated_time + weight
        # 더 짧은 경로를 찾은 경우 갱신
        if new_time < distance[neighbor]:
            distance[neighbor] = new_time
            heapq.heappush(hp, (new_time, neighbor))

if distance[N - 1] == INF:
    print(-1)
else:
    print(distance[N - 1])