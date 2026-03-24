import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# states : 현재까지 가능한 상태
# key : 총 비용, value : 해당 비용으로 얻을 수 있는 최대 메모리
states = {0: 0}

for i in range(N):
    # 기존 상태 copy (앱을 선택하지 않는 경우 유지)
    new_states = dict(states)

    for c, m in states.items():
        # i번째 앱을 선택하는 경우
        nc = c + cost[i]
        nm = m + memory[i]

        # 더 좋은 경우만 갱신
        # 1) 해당 비용이 처음 생성
        # 2) 같은 비용이지만 메모리가 더 좋음.
        if nc not in new_states or new_states[nc] < nm:
            new_states[nc] = nm

    # 갱신
    states = new_states

answer = float('inf')

for c, m in states.items():
    if m >= M:
        answer = min(answer, c)

print(answer)