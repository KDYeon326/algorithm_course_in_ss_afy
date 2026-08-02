import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find_min_collisions():
    visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]
    queue = deque()

    queue.append((0, 0, 0, 0))
    visited[0][0][0] = 0

    while queue:
        r, c, d, collisions = queue.popleft()

        nr = r + dr[d]
        nc = c + dc[d]

        # 오른쪽 경계 밖으로 탈출 성공
        if nc == m:
            print(collisions)
            return

        # 상, 하, 좌 경계로 나가는 경우는 탈출 불가
        if nr < 0 or nr >= n or nc < 0:
            continue

        # 다음 칸이 빈 칸인 경우 계속 직진 (충돌 X)
        if grid[nr][nc] == '.':
            if visited[nr][nc][d] == -1 or visited[nr][nc][d] > collisions:
                visited[nr][nc][d] = collisions
                queue.appendleft((nr, nc, d, collisions))

        # 다음 칸이 벽(#)인 경우 멈추고 방향 전환 (충돌 +1)
        elif grid[nr][nc] == '#':
            next_collisions = collisions + 1
            for new_d in range(4):
                if visited[r][c][new_d] == -1 or visited[r][c][new_d] > next_collisions:
                    visited[r][c][new_d] = next_collisions
                    queue.append((r, c, new_d, next_collisions))

    print(-1)


find_min_collisions()