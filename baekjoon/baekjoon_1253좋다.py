import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0

for i in range(n):
    left = 0
    right = n - 1
    target = arr[i]

    while left < right:
        if left != i and right != i:
            s = arr[left] + arr[right]

            if s == target:
                result += 1
                break
            elif s < target:
                left += 1
            else:
                right -= 1
        else:
            if left == i:
                left += 1
            if right == i:
                right -= 1

print(result)