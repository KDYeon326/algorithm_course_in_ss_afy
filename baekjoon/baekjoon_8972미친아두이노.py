import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
arduinos = []

for i in range(R):
    row = list(input().strip())
    for j in range(C):
        if row[j] == 'R':
            arduinos.append((i, j))
        elif row[j] == 'I':
            si, sj = i, j   # 종수 시작 위치
    board.append(row)

moves = input().strip()

# 키패드 방향
di = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dj = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

turn = 0
i, j = si, sj  # 종수 현재 위치

for m in moves:
    turn += 1
    d = int(m)

    # 종수 이동
    i += di[d]
    j += dj[d]

    if (i, j) in arduinos:
        print("kraj", turn)
        sys.exit()

    # 아두이노 이동
    new_positions = dict()

    for p, q in arduinos:
        min_dist = float('inf')
        ni, nj = p, q

        for d in range(1, 10):
            ti = p + di[d]
            tj = q + dj[d]
            dist = abs(ti - i) + abs(tj - j)

            if dist < min_dist:
                min_dist = dist
                ni, nj = ti, tj

        if (ni, nj) == (i, j):
            print("kraj", turn)
            sys.exit()

        if (ni, nj) in new_positions:
            new_positions[(ni, nj)] += 1
        else:
            new_positions[(ni, nj)] = 1

    # 충돌 제거
    arduinos = []
    for pos, count in new_positions.items():
        if count == 1:
            arduinos.append(pos)

result = [['.'] * C for _ in range(R)]
result[i][j] = 'I'
for p, q in arduinos:
    result[p][q] = 'R'

for row in result:
    print(''.join(row))