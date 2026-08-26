import sys

input = sys.stdin.readline

# 최솟값(구슬 중 가장 큰 값) ~ 최댓값(전체 합) 안에 답이 있다. 그 값을 찾아.
def get_min_max_sum(m, marbles):
    left = max(marbles)
    right = sum(marbles)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        group_count = 1
        current_sum = 0
        for marble in marbles:
            if current_sum + marble > mid:
                group_count += 1
                current_sum = marble
            else:
                current_sum += marble

        if group_count <= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def get_group_counts(n, m, marbles, max_limit):
    counts = []
    current_sum = 0
    current_count = 0

    for i in range(n - 1, -1, -1):
        if current_sum + marbles[i] > max_limit or i + 1 < m - len(counts):
            counts.append(current_count)
            current_sum = marbles[i]
            current_count = 1
        else:
            current_sum += marbles[i]
            current_count += 1

    counts.append(current_count)
    counts.reverse()
    return counts


n, m = map(int, input().split())
marbles = list(map(int, input().split()))

target_max = get_min_max_sum(m, marbles)
group_counts = get_group_counts(n, m, marbles, target_max)

print(target_max)
print(*group_counts)