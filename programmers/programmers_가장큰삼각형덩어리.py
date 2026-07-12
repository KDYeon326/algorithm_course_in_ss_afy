from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 삼각형 모양(0: |\, 1: |/, 2: \|, 3: /|)에 따른 이동 가능 방향 (dx, dy의 인덱스)
dir_map = [[1, 2], [0, 2], [0, 3], [1, 3]]

# 위아래 이동 시, 다음 격자의 대각선 모양(-1 또는 1)에 따라 결정되는 다음 state
# updown_state[현재 모양][다음 격자가 -1이면 0번째, 1이면 1번째]
updown_state = [[1, 0], [0, 1], [0, 1], [1, 0]]


def is_valid(x, y, n, m):
    """좌표가 격자 내부인지 판별합니다."""
    return 0 <= x < n and 0 <= y < m


def bfs(start_x, start_y, start_state, group_num, grid, group, n, m):

    queue = deque([(start_x, start_y, start_state)])
    group[start_x][start_y][start_state] = group_num

    size = 0
    while queue:
        cx, cy, cstate = queue.popleft()
        size += 1

        # 현재 삼각형 모양 판별 (0: |\, 1: |/, 2: \|, 3: /|)
        if grid[cx][cy] == -1:
            shape = 0 if cstate == 0 else 2
        else:
            shape = 1 if cstate == 0 else 3

        # 인접한 2개의 방향 탐색
        for i in range(2):
            nd = dir_map[shape][i]
            nx = cx + dx[nd]
            ny = cy + dy[nd]

            if not is_valid(nx, ny, n, m):
                continue
            if group[nx][ny][0] == group_num or group[nx][ny][1] == group_num:
                continue

            # 다음 삼각형의 state 결정
            if nd == 0 or nd == 1:  # 위 또는 아래로 이동하는 경우
                next_grid_type = 0 if grid[nx][ny] == -1 else 1
                n_state = updown_state[shape][next_grid_type]
            else:  # 좌우로 이동하는 경우
                n_state = 1 if nd == 2 else 0

            group[nx][ny][n_state] = group_num
            queue.append((nx, ny, n_state))

    return size


def solution(grid):

    n = len(grid)
    m = len(grid[0])
    group = [[[0, 0] for _ in range(m)] for _ in range(n)]

    answer = 0
    group_num = 1

    for i in range(n):
        for j in range(m):
            for k in range(2):
                if group[i][j][k] == 0:
                    group_size = bfs(i, j, k, group_num, grid, group, n, m)
                    if group_size > answer:
                        answer = group_size
                    group_num += 1

    return answer