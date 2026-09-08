import sys

input = sys.stdin.readline

num_trains = int(input())
passengers = list(map(int, input().split()))
k = int(input())

# K개 연속 객차의 승객 합 미리 구하기
# window_sum[i] = i번째 객차를 끝으로 하는 K개 객차의 승객 합
window_sum = [0] * (num_trains + 1)
current_sum = sum(passengers[:k])
window_sum[k] = current_sum

for idx in range(k + 1, num_trains + 1):
    current_sum += passengers[idx - 1] - passengers[idx - 1 - k]
    window_sum[idx] = current_sum

# dp[객차위치][기관차수]
dp = [[0] * 4 for _ in range(num_trains + 1)]

# 겹치지 않게 3개 선택
for train_idx in range(k, num_trains + 1):
    for engine_cnt in range(1, 4):
        skip = dp[train_idx - 1][engine_cnt]
        take = dp[train_idx - k][engine_cnt - 1] + window_sum[train_idx]

        dp[train_idx][engine_cnt] = max(skip, take)

print(dp[num_trains][3])