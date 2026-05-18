def add_max_path(triangle, row_index, col_index):
    """현재 위치에 아래 행의 두 값 중 더 큰 값을 더해주는 함수"""
    triangle[row_index][col_index] += max(
        triangle[row_index + 1][col_index],
        triangle[row_index + 1][col_index + 1]
    )


def solution(triangle):
    """정수 삼각형의 최대 경로 합을 구하는 함수"""
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            add_max_path(triangle, i, j)

    return triangle[0][0]