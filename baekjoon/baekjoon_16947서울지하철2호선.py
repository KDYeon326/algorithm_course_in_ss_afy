import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 사이클 판단
def find_cycle(curr, prev):
    visited[curr] = True

    for next in graph[curr]:
        if next == prev:
            continue

        if not visited[next]:
            parent[next] = curr
            if find_cycle(next, curr):
                return True
        else:
            # 사이클 발견
            is_cycle[next] = True
            x = curr
            while x != next:
                is_cycle[x] = True
                x = parent[x]
            return True

    return False


# 거리 계산
def calc_distance():
    distance = [-1] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if is_cycle[i]:
            distance[i] = 0
            q.append(i)

    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if distance[next] == -1:
                distance[next] = distance[curr] + 1
                q.append(next)

    return distance


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
parent = [-1] * (n + 1)
is_cycle = [False] * (n + 1)

find_cycle(1, -1)          # 사이클 찾기
distance = calc_distance()     # 거리 계산

print(*distance[1:])