import sys
input = sys.stdin.readline

def able_pipe_connect_directions():
    return {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        '+': [(1, 0), (-1, 0), (0, 1), (0, -1)],
        '1': [(1, 0), (0, 1)],
        '2': [(-1, 0), (0, 1)],
        '3': [(-1, 0), (0, -1)],
        '4': [(1, 0), (0, -1)],
    }


def find_missing_pipe(R, C, board):
    pipe_info = able_pipe_connect_directions()
    target_i, target_j = -1, -1

    for i in range(R):
        for j in range(C):
            current = board[i][j]

            if current not in ('.', 'M', 'Z'):
                for di, dj in pipe_info[current]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == '.':
                        target_i, target_j = ni, nj
                        break
            if target_i != -1: break
        if target_i != -1: break

    connected_directions = []

    check_list = [
        (-1, 0, ('|', '+', '1', '4')),  # 상 - 위쪽 파이프가 아래로 열려있어야 함
        (1, 0, ('|', '+', '2', '3')),  # 하 -아래쪽 파이프가 위로 열려있어야 함
        (0, -1, ('-', '+', '1', '2')),  # 좌 - 왼쪽 파이프가 오른쪽으로 열려있어야 함
        (0, 1, ('-', '+', '3', '4'))  # 우 - 오른쪽 파이프가 왼쪽으로 열려있어야 함
    ]

    for di, dj, possible_pipes in check_list:
        ni, nj = target_i + di, target_j + dj
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] in possible_pipes:
            connected_directions.append((di, dj))

    connected_directions.sort()

    answer_pipe_type = ''
    for pipe_type, pipe_directions in pipe_info.items():
        if sorted(pipe_directions) == connected_directions:
            answer_pipe_type = pipe_type
            break

    return target_i + 1, target_j + 1, answer_pipe_type


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

answer_i, answer_j, answer_pipe_type = find_missing_pipe(R, C, grid)
print(f"{answer_i} {answer_j} {answer_pipe_type}")