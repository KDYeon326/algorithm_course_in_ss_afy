import sys
from collections import deque
input = sys.stdin.readline

# 바닥과 연결된 미네랄 BFS
def bfs():
    visited = [[False] * C for _ in range(R)]
    q = deque()

    c = 0
    while c < C:
        if cave[R - 1][c] == 'x':
            visited[R - 1][c] = True
            q.append((R - 1, c))
        c += 1

    while q:
        x, y = q.popleft()
        d = 0
        while d < 4:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                if cave[nx][ny] == 'x' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            d += 1

    return visited


# 클러스터 낙하
def drop(cluster, cluster_set, visited):
    min_distant = R

    i = 0
    while i < len(cluster):
        x, y = cluster[i]
        dist = 0
        nx = x + 1
        while nx < R:
            if cave[nx][y] == 'x' and (nx, y) not in cluster_set:
                break
            if visited[nx][y]:
                break
            nx += 1
            dist += 1
        min_distant = min(min_distant, dist)
        i += 1

    i = 0
    while i < len(cluster):
        x, y = cluster[i]
        cave[x][y] = '.'
        i += 1

    i = 0
    while i < len(cluster):
        x, y = cluster[i]
        cave[x + min_distant][y] = 'x'
        i += 1


R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
throw_list = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

i = 0
while i < N:
    h = R - throw_list[i]

    # 막대 던지기
    if i % 2 == 0:      # 왼 -> 오
        c = 0
        while c < C:
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                break
            c += 1
    else:               # 오 -> 왼
        c = C - 1
        while c >= 0:
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                break
            c -= 1

    # 바닥 연결 확인
    visited = bfs()

    # 공중에 떠 있는 클러스터
    floating = []
    floating_set = set()

    r = 0
    while r < R:
        c = 0
        while c < C:
            if cave[r][c] == 'x' and not visited[r][c]:
                floating.append((r, c))
                floating_set.add((r, c))
            c += 1
        r += 1

    if floating:
        drop(floating, floating_set, visited)

    i += 1

r = 0
while r < R:
    print(''.join(cave[r]))
    r += 1