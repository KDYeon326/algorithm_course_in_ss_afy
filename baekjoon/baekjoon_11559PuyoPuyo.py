import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

boom_count = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    exploded = False

    # 터질 그룹 찾기
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                color = board[i][j]
                queue = deque()
                group = []

                queue.append((i, j))
                visited[i][j] = True
                group.append((i, j))

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < 12 and 0 <= ny < 6:
                            if not visited[nx][ny] and board[nx][ny] == color:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                group.append((nx, ny))

                # 4개 이상이면 펑
                if len(group) >= 4:
                    exploded = True
                    for x, y in group:
                        board[x][y] = '.'

    # 아무 것도 안 터졌으면 종료
    if not exploded:
        break

    # 중력
    for j in range(6):
        stack = []
        for i in range(12):
            if board[i][j] != '.':
                stack.append(board[i][j])

        for i in range(11, -1, -1):
            if stack:
                board[i][j] = stack.pop()
            else:
                board[i][j] = '.'

    boom_count += 1

print(boom_count)