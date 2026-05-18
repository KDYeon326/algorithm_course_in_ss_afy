def solution(money):
    n = len(money)

    if n == 1:
        return money[0]

    dp = [[0, 0] for _ in range(n)]

    dp[0][0] = money[0]
    dp[0][1] = 0

    dp[1][0] = max(money[0], money[1])
    dp[1][1] = money[1]

    for i in range(2, n):
        if i < n - 1:
            dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + money[i])
        else:
            dp[i][0] = dp[i - 1][0]

        dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + money[i])

    return max(dp[n - 1][0], dp[n - 1][1])