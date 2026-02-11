import sys
from collections import deque
from itertools import permutations, product

input = sys.stdin.readline

def rotate(layer):
    new = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[j][4 - i] = layer[i][j]
    return new

def bfs(maze):
    # 시작/끝 막히면 바로 패스
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return 1000

    q = deque([(0,0,0,0)])  # z, x, y, dist
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True

    while q:
        z, x, y, d = q.popleft()
        if z == 4 and x == 4 and y == 4:
            return d

        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
            if 0<=nz<5 and 0<=nx<5 and 0<=ny<5:
                if not visited[nz][nx][ny] and maze[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = True
                    q.append((nz,nx,ny,d+1))

    return 1000


origin = []
for _ in range(5):
    layer = [list(map(int, input().split())) for _ in range(5)]
    origin.append(layer)

# 각 판 4회전 미리 저장해둔다.
boards = []
for k in range(5):
    tmp = []
    cur = origin[k]
    for _ in range(4):
        tmp.append(cur)
        cur = rotate(cur)
    boards.append(tmp)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

ans = 1000

for order in permutations(range(5)):               # 0~4까지 순열 판 5개
    for rotation in product(range(4), repeat=5):        # 중복순열 0~3(회전 방향)까지를 판 5개 돌려
        maze = [[[0]*5 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            maze[i] = boards[order[i]][rotation[i]]  # 필요한거 위에 저장해둔데로 꺼내서 대입만.

        distance = bfs(maze)
        if distance < ans:
            ans = distance

        # 최단 가능 값 = 12 -> 바로 종료
        if ans == 12:
            print(12)
            sys.exit()

print(ans if ans != 1000 else -1)
