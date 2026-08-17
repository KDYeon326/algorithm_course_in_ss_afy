import sys

input = sys.stdin.readline


def count_bridge_crossings(string, devil_bridge, angel_bridge):
    string_len = len(string)
    bridge_len = len(devil_bridge)

    # dp[bridge_type][string_index][bridge_index]
    # dp[0] : 악돌, dp[1] : 천돌
    dp = [[[0] * bridge_len for _ in range(string_len)] for _ in range(2)]

    # 첫 번째 문자 위치 초기화
    for j in range(bridge_len):
        if devil_bridge[j] == string[0]:
            dp[0][0][j] = 1
        if angel_bridge[j] == string[0]:
            dp[1][0][j] = 1

    # DP
    for i in range(1, string_len):
        target_char = string[i]

        # 이전 단계(i-1)에서 반대편 다리의 누적경로 수
        prev_devil_sum = 0
        prev_angel_sum = 0

        for j in range(bridge_len):
            # 악마의 돌다리 - 이전 천사의 돌다리에서 j 미만 인덱스들의 합
            if devil_bridge[j] == target_char:
                dp[0][i][j] = prev_angel_sum

            # 천사의 돌다리 - 이전 악마의 돌다리에서 j 미만 인덱스들의 합
            if angel_bridge[j] == target_char:
                dp[1][i][j] = prev_devil_sum

            # 다음 인덱스 j+1을 위해 현재 인덱스 j의 값 누적
            prev_devil_sum += dp[0][i - 1][j]
            prev_angel_sum += dp[1][i - 1][j]

    # 마지막 문자까지 도달한 모든 경우의 수 합산
    total_ways = sum(dp[0][string_len - 1]) + sum(dp[1][string_len - 1])
    return total_ways


string = input().strip()
devil = input().strip()
angel = input().strip()

answer = count_bridge_crossings(string, devil, angel)
print(answer)