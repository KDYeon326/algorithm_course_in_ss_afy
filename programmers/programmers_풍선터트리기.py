def solution(a):
    # 풍선이 2개 이하이면 다 가능
    if len(a) <= 2:
        return len(a)

    # 투 포인터 렛츠고
    left = 0
    right = len(a) - 1

    left_min = a[left]
    right_min = a[right]

    # 양 끝 풍선 2개는 무조건 살아남으므로 2부터 시작
    able_num = 2

    # 두 포인터가 만날 때까지 while
    while left + 1 < right:
        # 왼쪽 수가 더 크다면, 왼쪽 포인터를 오른쪽으로 이동
        if left_min > right_min:
            left += 1
            # 새로운 수가 기존 왼쪽 최솟값보다 작다면 가능.
            if a[left] < left_min:
                left_min = a[left]
                able_num += 1
        # 오른쪽 수가 더 크거나 같다면, 오른쪽 포인터를 안쪽으로 이동
        else:
            right -= 1
            # 새로운 수가 오른쪽 최솟값보다 작다면 가능
            if a[right] < right_min:
                right_min = a[right]
                able_num += 1

    return able_num