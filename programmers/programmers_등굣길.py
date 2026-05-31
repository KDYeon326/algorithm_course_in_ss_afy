def count_unique_paths_with_list(m, n, puddles):
    # (n + 1) x (m + 1) 크기의 DP 테이블 생성
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 시작점(집) 초기화
    dp[1][1] = 1

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if r == 1 and c == 1:
                continue

            # 물웅덩이
            if [c, r] in puddles:
                dp[r][c] = 0
                continue

            # 최단 경로 수 누적
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % 1000000007

    return dp[n][m]


def solution(m, n, puddles):
    answer = count_unique_paths_with_list(m, n, puddles)
    return answer