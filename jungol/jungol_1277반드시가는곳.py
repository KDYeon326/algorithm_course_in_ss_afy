from collections import deque
import sys

input = sys.stdin.readline


def get_reachable_from(start_i, start_j, block_i, block_j):
    queue = deque([(start_i, start_j)])
    visited = {(start_i, start_j)}

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        now_i, now_j = queue.popleft()
        for idx in range(4):
            next_i, next_j = now_i + di[idx], now_j + dj[idx]
            if 0 <= next_i < n and 0 <= next_j < n:
                if next_i == block_i and next_j == block_j:
                    continue
                if grid[next_i][next_j] != '#' and (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    queue.append((next_i, next_j))

    return visited


n = int(input())
grid = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_i, start_j = i, j
        elif grid[i][j] == 'E':
            end_i, end_j = i, j

start_2_end = get_reachable_from(start_i, start_j, -1, -1)
end_2_start = get_reachable_from(end_i, end_j, -1, -1)

candidates = start_2_end.intersection(end_2_start)
candidates.remove((start_i, start_j))
candidates.remove((end_i, end_j))

must_visit = set()
for i, j in candidates:
    reachable_without = get_reachable_from(start_i, start_j, i, j)
    if (end_i, end_j) not in reachable_without:
        must_visit.add((i, j))

for i, j in must_visit:
    grid[i][j] = 'o'

for row in grid:
    print("".join(row))