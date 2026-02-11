import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

# 일반 이동
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 말 이동
hi = [-2, -1, 1, 2, 2, 1, -1, -2]
hj = [1, 2, 2, 1, -1, -2, -2, -1]

visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

q = deque()
q.append((0, 0, 0, 0))  # i, j, horse_movement(말처럼 이동), distance(이동 거리)
visited[0][0][0] = True

while q:
    i, j, horse_movement, distance = q.popleft()

    if i == H - 1 and j == W - 1:
        print(distance)
        sys.exit()

    # 일반 이동
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < H and 0 <= nj < W:
            if board[ni][nj] == 0 and not visited[ni][nj][horse_movement]:
                visited[ni][nj][horse_movement] = True
                q.append((ni, nj, horse_movement, distance + 1))

    # 말 이동
    if horse_movement < K:
        for dir in range(8):
            ni = i + hi[dir]
            nj = j + hj[dir]

            if 0 <= ni < H and 0 <= nj < W:
                if board[ni][nj] == 0 and not visited[ni][nj][horse_movement + 1]:
                    visited[ni][nj][horse_movement + 1] = True
                    q.append((ni, nj, horse_movement + 1, distance + 1))

print(-1)