import sys


def count_set_bits(n):
    bit_counts = [0] * n
    for i in range(n):
        bit_counts[i] = bit_counts[i >> 1] + (i & 1)
    return bit_counts


def solve_building_cost_dp(n, costs):
    max_mask = 1 << n  # 가능한 모든 장소 조합의 개수 (O, X 2개씩해서 2^n)
    inf = float('inf')
    dp = [inf] * max_mask
    parent_mask = [0] * max_mask  # 경로 역추적 위해 이전 상태 배열
    assigned_place = [0] * max_mask  # 마지막으로 선택된 장소 기록하는 배열

    bit_counts = [0] * max_mask
    for i in range(1, max_mask):
        bit_counts[i] = bit_counts[i >> 1] + (i & 1)

    dp[0] = 0

    for mask in range(max_mask):
        if dp[mask] == inf:  # 도달할 수 없으면
            continue

        building_index = bit_counts[mask]  # 현재 켜진 비트(1) 수 = 지금까지 배치한 건물 수
        if building_index == n:  # 다 배치했으면 끝
            continue

        # 안지어진 곳 탐색
        for place_index in range(n):
            if not (mask & (1 << place_index)):  # 비트가 0이라면
                next_mask = mask | (1 << place_index)  # 비어있으면 해당 장소 추가
                current_cost = dp[mask] + costs[building_index][place_index]

                # 갱신
                if current_cost < dp[next_mask]:
                    dp[next_mask] = current_cost
                    parent_mask[next_mask] = mask  # 이전 상태
                    assigned_place[next_mask] = place_index + 1  # 이번에 선택된 장소 번호 기록 (1부터 시작하니까 인덱스+1)

    return dp, parent_mask, assigned_place


def reconstruct_path(n, parent_mask, assigned_place):
    path = [0] * n
    current_mask = (1 << n) - 1  # 모든 장소가 꽉 찬 최종 상태부터 거꾸로 추적합니다.

    # 마지막 건물부터 첫 번째 건물까지 역순으로 탐색
    for building_index in range(n - 1, -1, -1):
        path[building_index] = assigned_place[current_mask]
        current_mask = parent_mask[current_mask]  # 이전 상태로 이동

    return path


input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블, 이전 상태 기록 배열, 장소 기록 배열
dp_table, parent_mask, assigned_place = solve_building_cost_dp(n, costs)

maximum_mask = (1 << n) - 1
minimum_cost = dp_table[maximum_mask]
optimal_path = reconstruct_path(n, parent_mask, assigned_place)

print(minimum_cost)
print(*optimal_path)