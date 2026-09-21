import sys

input = sys.stdin.readline
directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_safe(r, c, board, visited, n):

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == '*':
                break
            if visited[nr][nc]:
                return False
            nr += dr
            nc += dc
    return True


def dfs(tiles, idx, board, visited, n):
    if idx == len(tiles):
        return 0

    max_bishops = dfs(tiles, idx + 1, board, visited, n)

    r, c = tiles[idx]
    if is_safe(r, c, board, visited, n):
        visited[r][c] = True
        max_bishops = max(max_bishops, 1 + dfs(tiles, idx + 1, board, visited, n))
        visited[r][c] = False

    return max_bishops


T = int(input())
for _ in range(T):
    N = int(input())
    board = [input().strip() for _ in range(N)]

    white_tiles = []
    black_tiles = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                if (r + c) % 2 == 0:
                    white_tiles.append((r, c))
                else:
                    black_tiles.append((r, c))

    visited = [[False] * N for _ in range(N)]
    white_max = dfs(white_tiles, 0, board, visited, N)
    black_max = dfs(black_tiles, 0, board, visited, N)

    print(white_max + black_max)