import sys

input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

ans = [0] * n

for i in range(1, n):
    target = i - 1

    # 나보다 키가 작으면 그 탑이 레이저를 쏘았던 바로 그 탑의 위치로
    while target >= 0 and heights[target] < heights[i]:
        target = ans[target] - 1

    if target >= 0:
        ans[i] = target + 1

print(*(ans))