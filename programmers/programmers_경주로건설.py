from collections import deque


def plus_cost(current_cost, current_dir, next_dir):
    cost = current_cost + 100
    if current_dir != next_dir:
        cost += 500
    return cost


def solution(board):
    N = len(board)
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()

    visited[0][0][0] = 0
    visited[0][0][1] = 0

    if board[0][1] == 0:
        queue.append((100, 0, 1, 0))
        visited[0][1][0] = 100

    if board[1][0] == 0:
        queue.append((100, 1, 0, 1))
        visited[1][0][1] = 100

    while queue:
        current_cost, r, c, d = queue.popleft()

        if visited[r][c][d] < current_cost:
            continue

        for i in range(4):
            nr = r + directions[i][0]
            nc = c + directions[i][1]

            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                next_cost = plus_cost(current_cost, d, i)
                if next_cost <= visited[nr][nc][i]:
                    visited[nr][nc][i] = next_cost
                    queue.append((next_cost, nr, nc, i))

    return min(visited[N - 1][N - 1])