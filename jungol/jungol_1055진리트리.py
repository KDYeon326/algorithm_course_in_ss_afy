import sys

input = sys.stdin.readline
INF = float('inf')

M, V = map(int, input().split())

input_2_index = (M - 1) // 2
gate = [0] * (input_2_index + 1)
is_changeable = [0] * (input_2_index + 1)

for i in range(1, input_2_index + 1):
    g, c = map(int, input().split())
    gate[i] = g
    is_changeable[i] = c

cost = [[INF, INF] for _ in range(M + 1)]
# cost[i][0]: i번 노드를 0으로 만드는 최소 스위치 변경 횟수
# cost[i][1]: i번 노드를 1로 만드는 최소 스위치 변경 횟수

for i in range(input_2_index + 1, M + 1):
    value = int(input())
    cost[i][value] = 0

# 리프 노드부터 판단
for i in range(input_2_index, 0, -1):
    left = i * 2
    right = i * 2 + 1

    current_gate = gate[i]
    can_change = is_changeable[i]

    # 자식 노드 변경 횟수 미리 가져오고
    left_node_0, left_node_1 = cost[left][0], cost[left][1]
    right_node_0, right_node_1 = cost[right][0], cost[right][1]

    # AND 게이트일 때
    and_make_0 = min(left_node_0 + right_node_0, left_node_0 + right_node_1, left_node_1 + right_node_0)
    and_make_1 = left_node_1 + right_node_1

    # OR 게이트일 때
    or_make_0 = left_node_0 + right_node_0
    or_make_1 = min(left_node_1 + right_node_1, left_node_1 + right_node_0, left_node_0 + right_node_1)

    if current_gate == 1:  # AND 게이트
        cost[i][0] = and_make_0
        cost[i][1] = and_make_1
        if can_change == 1:  # 바꿀 수 있으면
            cost[i][0] = min(cost[i][0], or_make_0 + 1)
            cost[i][1] = min(cost[i][1], or_make_1 + 1)
    else:  # OR 게이트
        cost[i][0] = or_make_0
        cost[i][1] = or_make_1
        if can_change == 1:  # 바꿀 수 있으면
            cost[i][0] = min(cost[i][0], and_make_0 + 1)
            cost[i][1] = min(cost[i][1], and_make_1 + 1)

answer = cost[1][V]

if answer == INF:
    print("IMPOSSIBLE")
else:
    print(answer)