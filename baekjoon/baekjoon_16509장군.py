from collections import deque

sr, sc = map(int, input().split())
kr, kc = map(int, input().split())

visited = [[False] * 9 for _ in range(10)]

# 상 이동 경우의 수
Sang_moving = [
    ((-1, 0), (-1, -1), (-1, -1)),  # 상 좌상 좌상
    ((-1, 0), (-1, 1), (-1, 1)),    # 상 우상 우상
    ((1, 0), (1, -1), (1, -1)),     # 하 좌하 좌하
    ((1, 0), (1, 1), (1, 1)),       # 하 우하 우하
    ((0, -1), (-1, -1), (-1, -1)),  # 좌 좌상 좌상
    ((0, -1), (1, -1), (1, -1)),    # 좌 좌하 좌하
    ((0, 1), (-1, 1), (-1, 1)),     # 우 우상 우상
    ((0, 1), (1, 1), (1, 1))        # 우 우하 우하
]

q = deque()
q.append((sr, sc, 0))
visited[sr][sc] = True

answer = -1

while q:
    r, c, dist = q.popleft()

    # 장군이요
    if (r, c) == (kr, kc):
        answer = dist
        break

    for move in Sang_moving:
        nr, nc = r, c
        blocked = False

        for i in range(3):
            dr, dc = move[i]
            nr += dr
            nc += dc

            # 범위 체크
            if not (0 <= nr < 10 and 0 <= nc < 9):
                blocked = True
                break

            # 1, 2칸째에서 왕이 있으면 이동 불가
            if i < 2 and (nr, nc) == (kr, kc):
                blocked = True
                break

        if blocked:
            continue

        if not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))

print(answer)