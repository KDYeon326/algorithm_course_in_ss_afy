from collections import deque

DI = [0, 0, 0, 1, -1]
DJ = [0, 1, -1, 0, 0]

TURN_LEFT = [0, 4, 3, 1, 2]
TURN_RIGHT = [0, 3, 4, 2, 1]


def find_min_commands(m, n, grid, si, sj, sd, ei, ej, ed):
    visited = [[[False] * 5 for _ in range(n)] for _ in range(m)]
    queue = deque([(si, sj, sd, 0)])
    visited[si][sj][sd] = True

    while queue:
        i, j, d, cnt = queue.popleft()

        if i == ei and j == ej and d == ed:
            return cnt

        # Go k
        for k in range(1, 4):
            ni = i + DI[d] * k
            nj = j + DJ[d] * k

            if 0 <= ni < m and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    break
                if not visited[ni][nj][d]:
                    visited[ni][nj][d] = True
                    queue.append((ni, nj, d, cnt + 1))
            else:
                break

        # Turn dir
        for nd in (TURN_LEFT[d], TURN_RIGHT[d]):
            if not visited[i][j][nd]:
                visited[i][j][nd] = True
                queue.append((i, j, nd, cnt + 1))
    return None


M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())

result = find_min_commands(M, N, grid, si - 1, sj - 1, sd, ei - 1, ej - 1, ed)
# grid (0, 0)이 문제에서 (1, 1)이라서 -1 해줌)
print(result)