import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def count_down_paths(y, x, m, n, map_data, dp):
    if y == m - 1 and x == n - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < m and 0 <= nx < n:
            if map_data[ny][nx] < map_data[y][x]:
                dp[y][x] += count_down_paths(ny, nx, m, n, map_data, dp)

    return dp[y][x]


M, N = map(int, input().split())

map_data = []
for _ in range(M):
    row = list(map(int, input().split()))
    map_data.append(row)

dp = [[-1] * N for _ in range(M)]

result = count_down_paths(0, 0, M, N, map_data, dp)
print(result)