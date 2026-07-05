import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)


def build_team_map(links):
    team_map = defaultdict(list)
    for manager, member in links:
        team_map[manager].append(member)
    return team_map


def calculate_tree_dp(manager, team_map, sales, dp):

    # 팀장 겸 팀원이 아니라 오직 팀원인 경우
    if manager not in team_map:
        dp[manager][0] = sales[manager - 1]
        dp[manager][1] = 0
        return

    # 부하 직원들의 DP 값부터 먼저 계산 (후위 순회)
    for member in team_map[manager]:
        calculate_tree_dp(member, team_map, sales, dp)

    # 현재 팀장이 워크숍에 참석하는 경우
    dp[manager][0] = sales[manager - 1]
    for member in team_map[manager]:
        dp[manager][0] += min(dp[member][0], dp[member][1])

    # 팀장이 워크숍에 참석하지 않는 경우
    total_member_min = 0
    has_attended_member = False
    min_diff = float('inf')

    for member in team_map[manager]:
        total_member_min += min(dp[member][0], dp[member][1])

        # 팀원 중 한 명이라도 참석하는 것이 비용상 이득인 경우
        if dp[member][0] <= dp[member][1]:
            has_attended_member = True

        # 불참이 이득인 팀원을 강제 참여시킬 때 발생하는 최소 비용 차이 계산
        min_diff = min(min_diff, dp[member][0] - dp[member][1])

    # 모든 팀원이 불참하는 것이 이득이라면, 가장 손해가 적은 팀원 한 명이 참석
    if not has_attended_member:
        total_member_min += min_diff

    dp[manager][1] = total_member_min


def solution(sales, links):
    sales_len = len(sales)

    # {팀장: [팀원들]}
    team_map = build_team_map(links)

    # dp[i][0] = i번 직원 참석 시 최소 비용
    # dp[i][1] = i번 직원 불참 시 최소 비용
    dp = [[0, 0] for _ in range(sales_len + 1)]

    calculate_tree_dp(1, team_map, sales, dp)

    return min(dp[1][0], dp[1][1])