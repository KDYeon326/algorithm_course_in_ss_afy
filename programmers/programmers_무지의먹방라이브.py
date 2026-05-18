def solution(food_times, k):
    # 전체를 다 먹는 데 걸리는 총 시간이 k초 이하이면 음식 X
    if sum(food_times) <= k:
        return -1

    total_food_count = len(food_times)

    # [음식 시간, 인덱스] // 음식 시간 기준으로 오름차순 정렬
    sorted_food_list = sorted([[time, index + 1] for index, time in enumerate(food_times)])

    previous_ate_food_time = 0  # 바로 직전에 완전히 다 먹어서 사라진 음식의 양
    remaining_food_count = total_food_count  # 현재 회전판에 남아있는 음식의 개수

    # 음식 양을 기준으로 정렬하여 시간을 넘겨
    for current_index, (current_minimum_food_time, _ ) in enumerate(sorted_food_list):
        # 이번 음식을 완전히 다 먹기 위해 추가로 회전해야 하는 바퀴 수
        cycle_count_minimum_food = current_minimum_food_time - previous_ate_food_time

        # 이 음식을 완전히 비우기 위해 소모되는 총 시간 (추가 바퀴 수 * 남은 음식 개수)
        total_time_minimum_food = cycle_count_minimum_food * remaining_food_count

        # 남은 k초가 사이클을 돌릴 수 있는지 확인
        if k >= total_time_minimum_food:
            k -= total_time_minimum_food
            remaining_food_count -= 1
            previous_ate_food_time = current_minimum_food_time
        else:  # K가 적당히 남아서 더이상의 사이클은 X
            # 현재 인덱스부터 순회하면 답 추출
            left_food_list = sorted_food_list[current_index:]

            # 남아있는 음식들을 원래 인덱스대로 정렬해서
            left_food_list_original_index  = sorted(left_food_list, key=lambda x: x[1])

            # K번째 음식을 구해
            target_food_position = k % remaining_food_count

            return left_food_list_original_index[target_food_position][1]