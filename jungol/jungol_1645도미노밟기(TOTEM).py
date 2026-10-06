import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
domino_count = n * n - n // 2
dominoes = [None] * (domino_count + 1)
for i in range(1, domino_count + 1):
    u, v = map(int, input().split())
    dominoes[i] = (u, v)

# 그리드 및 1차원 배열을 이용한 위치 관리 (메모리 최적화)
max_cols = 2 * n
grid = [[0] * max_cols for _ in range(n)]

domino_r = [0] * (domino_count + 1)
domino_c_idx = [0] * (domino_count + 1)

domino_id = 1
for r in range(n):
    if r % 2 == 0:
        for c_idx in range(n):
            c1 = c_idx * 2
            c2 = c_idx * 2 + 1
            grid[r][c1] = domino_id
            grid[r][c2] = domino_id
            domino_r[domino_id] = r
            domino_c_idx[domino_id] = c_idx
            domino_id += 1
    else:
        for c_idx in range(n - 1):
            c1 = c_idx * 2 + 1
            c2 = c_idx * 2 + 2
            grid[r][c1] = domino_id
            grid[r][c2] = domino_id
            domino_r[domino_id] = r
            domino_c_idx[domino_id] = c_idx
            domino_id += 1

# BFS 탐색 (set dict 다 포기하고 생성 없이)
visited = [False] * (domino_count + 1)
distance = [0] * (domino_count + 1)
parent = [0] * (domino_count + 1)

queue = deque([1])
visited[1] = True
distance[1] = 1

max_node = 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while queue:
    current = queue.popleft()
    if current > max_node:
        max_node = current

    r = domino_r[current]
    c_idx = domino_c_idx[current]

    if r % 2 == 0:
        cells = [(r, c_idx * 2), (r, c_idx * 2 + 1)]
    else:
        cells = [(r, c_idx * 2 + 1), (r, c_idx * 2 + 2)]

    curr_neighbors = set()
    for cell_idx, (cr, cc) in enumerate(cells):
        u_num = dominoes[current][cell_idx]

        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < max_cols:
                v_id = grid[nr][nc]
                if v_id != 0 and v_id != current:
                    if nr % 2 == 0:
                        v_cell_idx = 0 if (nc % 2 == 0) else 1
                    else:
                        v_cell_idx = 0 if (nc % 2 == 1) else 1
                    v_num = dominoes[v_id][v_cell_idx]

                    if u_num == v_num:
                        curr_neighbors.add(v_id)

    for nxt in curr_neighbors:
        if not visited[nxt]:
            visited[nxt] = True
            distance[nxt] = distance[current] + 1
            parent[nxt] = current
            queue.append(nxt)

path = []
curr = max_node
while curr != 0:
    path.append(curr)
    curr = parent[curr]
path.reverse()

print(distance[max_node])
print(*(path))