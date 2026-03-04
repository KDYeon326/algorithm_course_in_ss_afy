import sys
from collections import deque

input = sys.stdin.readline

def bfs_group(si, sj, group_id):
    queue = deque()
    queue.append((si, sj))
    able_blank_group[si][sj] = group_id
    size = 1

    while queue:
        ci, cj = queue.popleft()

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == 0 and able_blank_group[ni][nj] == -1:
                    able_blank_group[ni][nj] = group_id
                    queue.append((ni, nj))
                    size += 1

    return size


def label_groups():
    able_blank_group_id = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and able_blank_group[i][j] == -1:
                size = bfs_group(i, j, able_blank_group_id)
                able_blank_group_size.append(size)
                able_blank_group_id += 1


def compute_wall_values():
    count_able_blank_grid = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                temp_groups = set()

                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 0:
                            temp_groups.add(able_blank_group[ni][nj])

                total = 1
                for groupid in temp_groups:
                    total += able_blank_group_size[groupid]

                count_able_blank_grid[i][j] = total % 10

    return count_able_blank_grid


n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

able_blank_group = [[-1] * m for _ in range(n)]
able_blank_group_size = []

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

label_groups()
count_able_blank_grid = compute_wall_values()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            print(count_able_blank_grid[i][j], end="")
        else:
            print(0, end="")
    print()