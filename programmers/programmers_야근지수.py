def solution(n, works):
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    works.append(0)

    works_count = len(works)

    for i in range(works_count - 1):
        # 현재까지 확인한 가장 큰 수의 갯수
        same_height_count = i + 1

        # 가장 큰 수와 두번재로 큰 수 차이
        height_difference = works[i] - works[i + 1]

        # 가장 큰 수를 두번재로 큰 수로 만드는데 드는 총 사이클(?)
        required_time = height_difference * same_height_count

        if n >= required_time:
            n -= required_time
        else:
            base_sub = n // same_height_count  # 가장 큰 수에서 얼마나 뺄지
            extra_sub_count = n % same_height_count  # 1씩 더 빼야 하는 횟수

            # 계산
            for j in range(same_height_count):
                works[j] = works[i] - base_sub
                if j < extra_sub_count:
                    works[j] -= 1

            break

    answer = sum(w ** 2 for w in works)
    return answer