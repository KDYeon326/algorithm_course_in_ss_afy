from collections import deque


def check_air_in_or_out(n, m, grid):
    out_visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    out_visited[0][0] = True

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if not out_visited[ni][nj] and grid[ni][nj] <= 0:
                    out_visited[ni][nj] = True
                    queue.append((ni, nj))

    for i in range(n):
        for j in range(m):
            if grid[i][j] <= 0:
                if out_visited[i][j]:
                    grid[i][j] = 0  # 외부
                else:
                    grid[i][j] = -1  # 내부


def melt_cheese(n, m, grid):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    melt_list = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                touch_count = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 0:
                            touch_count += 1
                if touch_count >= 2:
                    melt_list.append((i, j))

    for i, j in melt_list:
        grid[i][j] = 0

    return len(melt_list)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time = 0
total_cheese = 0

for row in grid:
    for val in row:
        if val == 1:
            total_cheese += 1

while total_cheese > 0:
    check_air_in_or_out(n, m, grid)
    melted_count = melt_cheese(n, m, grid)
    total_cheese -= melted_count
    time += 1

print(time)