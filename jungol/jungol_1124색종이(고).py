import sys

input = sys.stdin.readline


def calculate_max_rectangle_dp(board):
    # DP를 이용해 각 셀마다 가능한 좌우 경계와 높이를 갱신
    max_area = 0
    total_columns = 105

    heights = [0] * total_columns
    left_boundaries = [0] * total_columns
    right_boundaries = [total_columns - 1] * total_columns

    for row in range(1, 101):
        # left 갱신
        current_left = 1
        for col in range(1, 101):
            if board[row][col] == 1:
                left_boundaries[col] = max(left_boundaries[col], current_left)
            else:
                left_boundaries[col] = 1
                current_left = col + 1

        # right 갱신
        current_right = 100
        for col in range(100, 0, -1):
            if board[row][col] == 1:
                right_boundaries[col] = min(right_boundaries[col], current_right)
            else:
                right_boundaries[col] = 100
                current_right = col - 1

        # height, 최종 넓이 계산
        for col in range(1, 101):
            if board[row][col] == 1:
                heights[col] += 1
            else:
                heights[col] = 0

            # 높이가 0이 아닐 때만 현재 위치에서 만들 수 있는 직사각형 넓이 계산
            if heights[col] > 0:
                width = right_boundaries[col] - left_boundaries[col] + 1
                current_area = heights[col] * width
                max_area = max(max_area, current_area)

    return max_area


number_of_papers = int(input())
board = [[0] * 105 for _ in range(105)]

for _ in range(number_of_papers):
    x_coordinate, y_coordinate = map(int, input().split())

    for row in range(y_coordinate, y_coordinate + 10):
        for col in range(x_coordinate, x_coordinate + 10):
            board[row][col] = 1

result = calculate_max_rectangle_dp(board)
print(result)