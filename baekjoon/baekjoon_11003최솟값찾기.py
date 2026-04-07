import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))


def find_minimums_between_i(n, l, arr):
    q = deque()
    result = []

    for i in range(n):
        # 덱의 마지막 원소가 남아있는 원소보다 크거나 같으면, 어차피 최솟값이 될 수 없으니까 제거
        while q and arr[q[-1]] >= arr[i]:
            q.pop()

        # 현재 인덱스를 덱에 추가
        q.append(i)

        # 덱의 맨 앞 원소가 i-L+1 ~ i를 벗어났으면 제거
        if q[0] <= i - l:
            q.popleft()

        # 덱의 맨 앞 원소는 항상 범위의 최솟값
        result.append(arr[q[0]])

    return result


result_arr = find_minimums_between_i(n, l, arr)
print(*result_arr)