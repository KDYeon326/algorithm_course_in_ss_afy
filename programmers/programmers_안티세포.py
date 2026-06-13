def get_anti_cell_counts_for_query(current_cells):
    n = len(current_cells)
    MOD = 1_000_000_007

    dp = [0] * (n + 1)
    dp[0] = 1

    history = [{} for _ in range(n + 1)]

    for i in range(1, n + 1):
        cell_val = current_cells[i - 1]

        # 합성 X
        dp[i] = dp[i - 1]
        history[i][cell_val] = i - 1

        target_size = cell_val
        left_idx = i - 1

        # 왼쪽에 크기가 같은 군집이 있는지 확인하며 역추적
        while left_idx > 0 and target_size in history[left_idx]:
            start_of_left = history[left_idx][target_size]
            target_size *= 2
            history[i][target_size] = start_of_left

            # 합성이 가능하므로 이전 상태의 경우의 수를 누적
            dp[i] = (dp[i] + dp[start_of_left]) % MOD
            left_idx = start_of_left

    return dp[n]


def solution(a, s):
    results = []
    current_start = 0

    for length in s:

        current_cells = a[current_start: current_start + length]

        # 해당 세포 배열의 안티세포 경우의 수 계산
        count = get_anti_cell_counts_for_query(current_cells)
        results.append(count)

        current_start += length

    return results