from bisect import bisect_right
import sys

input = sys.stdin.readline


def record_zero_days(rainy_day):
    # 비 안오는 날의 index 기록
    zero_days = []
    for day_index, lake_number in enumerate(rainy_day):
        if lake_number == 0:
            zero_days.append(day_index)
    return zero_days


def find_next_free_zero(index, next_free):
    # 아직 사용되지 않은 가장 가까운 비 안오는 날의 위치를 탐색
    while len(next_free) > index and index != next_free[index]:
        next_free[index] = next_free[next_free[index]]
        index = next_free[index]
    return index


def find_drink_days(lake_count, rainy_day):
    zero_days = record_zero_days(rainy_day)
    zero_count = len(zero_days)
    rain_count = len(rainy_day) - zero_count

    # 비가 오는 날보다 0의 개수가 적으면 모든 비를 대비해 호수를 비울 수 없음
    if zero_count < rain_count:
        return False, []

    drink_plan = [0] * zero_count
    next_free = list(range(zero_count + 1))
    last_rain_day = [-1] * (lake_count + 1)

    for day_index, lake_number in enumerate(rainy_day):
        if lake_number == 0:
            continue

        # 직전 비가 온 날 이후에 등장하는 첫 번째 0 인덱스부터 빈 자리를 찾음
        start_pos = bisect_right(zero_days, last_rain_day[lake_number])
        chosen_zero_idx = find_next_free_zero(start_pos, next_free)

        # 사용할 수 있는 0이 없거나 현재 비가 오는 날 이후의 0이라면 실패
        if chosen_zero_idx >= zero_count or zero_days[chosen_zero_idx] > day_index:
            return False, []

        # 가장 빠른 가용 0 날짜에 호수를 배정하고 다음 빈 인덱스로 연결
        drink_plan[chosen_zero_idx] = lake_number
        next_free[chosen_zero_idx] = chosen_zero_idx + 1
        last_rain_day[lake_number] = day_index

    return True, drink_plan


for _ in range(4):
    lake_count, day_count = map(int, input().split())
    rainy_day = list(map(int, input().split()))
    is_possible, drink_day = find_drink_days(lake_count, rainy_day)
    if not is_possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, drink_day)))