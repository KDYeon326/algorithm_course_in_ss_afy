from collections import deque
import sys

input = sys.stdin.readline

def spread_fire(fire_queue, fire_board):
    rd = [-1, 1, 0, 0]
    cd = [0, 0, -1, 1]

    while fire_queue:
        now_r, now_c = fire_queue.popleft()

        for d in range(4):
            next_r = now_r + rd[d]
            next_c = now_c + cd[d]

            if 0 <= next_r < R and 0 <= next_c < C:
                if grid[next_r][next_c] != 'X' and grid[next_r][next_c] != 'D' and fire_board[next_r][next_c] == -1:
                    fire_board[next_r][next_c] = fire_board[now_r][now_c] + 1
                    fire_queue.append((next_r, next_c))

def escape_to_fire(jaewoo_queue, visited, fire_board, end_r, end_c):
    rd = [-1, 1, 0, 0]
    cd = [0, 0, -1, 1]

    while jaewoo_queue:
        now_r, now_c, time = jaewoo_queue.popleft()

        if now_r == end_r and now_c == end_c:
            print(time)
            return

        for d in range(4):
            next_r = now_r + rd[d]
            next_c = now_c + cd[d]

            if 0 <= next_r < R and 0 <= next_c < C:
                if not visited[next_r][next_c] and grid[next_r][next_c] != 'X':
                    if fire_board[next_r][next_c] == -1 or time + 1 < fire_board[next_r][next_c]:
                        visited[next_r][next_c] = True
                        jaewoo_queue.append((next_r, next_c, time + 1))

    print("impossible")


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

fire_queue = deque()
jaewoo_queue = deque()
fire_board = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

end_r = 0
end_c = 0

for now_r in range(R):
    for now_c in range(C):
        if grid[now_r][now_c] == '*':
            fire_queue.append((now_r, now_c))
            fire_board[now_r][now_c] = 0
        elif grid[now_r][now_c] == 'S':
            jaewoo_queue.append((now_r, now_c, 0))
            visited[now_r][now_c] = True
        elif grid[now_r][now_c] == 'D':
            end_r = now_r
            end_c = now_c

spread_fire(fire_queue, fire_board)
escape_to_fire(jaewoo_queue, visited, fire_board, end_r, end_c)