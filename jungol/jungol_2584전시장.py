import sys
from bisect import bisect_right

input_data = sys.stdin.read().split()

n = int(input_data[0])
s = int(input_data[1])

# (높이, 가격)
pictures = []
idx = 2
for _ in range(n):
    pictures.append((int(input_data[idx]), int(input_data[idx + 1])))
    idx += 2

pictures.sort()

heights = [p[0] for p in pictures]

# dp[i]: i번째 그림까지 고려했을 때 판매가능 그림들의 최대 가격 합
dp = [0] * n
dp[0] = pictures[0][1]

for i in range(1, n):
    curr_h, curr_c = pictures[i]
    target_h = curr_h - s

    # 현재 그림 아래에 겹쳐 놓을 수 있는 가장 높은 그림의 위치 탐색 (높이 <= curr_h - s)
    pos = bisect_right(heights, target_h) - 1

    # 이전 그림을 포함할 수 있는 경우
    if pos >= 0:
        val = dp[pos] + curr_c
    else:
        val = curr_c

    dp[i] = max(dp[i - 1], val)

print(dp[-1])