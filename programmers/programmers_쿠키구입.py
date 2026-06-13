from bisect import bisect_left

## bisect_left : 정렬된 상태를 유지하면서 새로운 원소를 삽입할 수 있는 가장 왼쪽 인덱스찾는 함수

def solution(cookie):
    answer = 0
    n = len(cookie)

    # 누적 합 생성
    part_sum = [0] * (n + 1)
    for i in range(n):
        part_sum[i + 1] = part_sum[i] + cookie[i]

    # 첫째 아들의 구간 [l, m]을 2중 루프로 순회
    for l in range(n):
        for m in range(l, n - 1):
            # 첫째 아들이 가져가는 쿠키 합
            sum_first = part_sum[m + 1] - part_sum[l]

            # 둘째 아들이 가져가야 할 목표 누적 합 위치
            # sum_second == sum_first가 되려면 part_sum[r + 1]이 아래 값이 되어야 함
            target_part_sum = part_sum[m + 1] + sum_first

            # 이분 탐색으로 만족하는 r이 있는지 찾기
            idx = bisect_left(part_sum, target_part_sum, m + 2, n + 1)

            # 정확히 일치하는 값이 배열 범위 내에 있다면 조건 만족
            if idx <= n and part_sum[idx] == target_part_sum:
                answer = max(answer, sum_first)

    return answer