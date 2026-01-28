import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

# i부터 j까지 팰린드롬이면 1
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 길이 1 (무조건 팰린드롬)
for i in range(1, n + 1):
    dp[i][i] = 1

# 길이 2
for i in range(1, n):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

# 길이 3 이상
for length in range(3, n + 1):          # 구간 길이
    for i in range(1, n - length + 2):  # 시작점
        j = i + length - 1              # 끝점
        if arr[i] == arr[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])