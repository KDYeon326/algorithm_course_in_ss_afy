import sys
from collections import deque

input = sys.stdin.readline

# 지정된 플레이어의 성을 주어진 횟수(max_steps)만큼만 BFS로 확장
def expand_castle(player_id, max_steps):
    is_expanded = False

    for _ in range(max_steps):
        # 더 이상 확장할 출발지가 없으면 종료
        if not queues[player_id]:
            break

        # 현재 레벨에 있는 큐의 길이만큼만 탐색하여 동일 턴 내의 이동 거리를 제어
        q_len = len(queues[player_id])
        for _ in range(q_len):
            r, c = queues[player_id].popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                # 격자 범위 내에 있고, 빈 칸인 경우에만 새로운 성 건설
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
                    grid[nr][nc] = str(player_id)
                    ans[player_id] += 1
                    queues[player_id].append((nr, nc))
                    is_expanded = True

    return is_expanded

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))

grid = []
queues = [deque() for _ in range(p + 1)]
ans = [0] * (p + 1)

for r in range(n):
    row = list(input().rstrip())
    grid.append(row)
    for c in range(m):
        if row[c] != '.' and row[c] != '#':
            player = int(row[c])
            queues[player].append((r, c))
            ans[player] += 1
ㅠ
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while True:
    game_continued = False

    for i in range(1, p + 1):
        if queues[i]:
            # 함수 실행 결과, 단 한 칸이라도 새 성을 확장했다면 게임 계속 진행
            if expand_castle(i, s[i]):
                game_continued = True

    # 1번부터 P번 플레이어 모두가 어떠한 성도 확장하지 못했다면 게임 종료
    if not game_continued:
        break

print(*(ans[1:]))