import sys

input = sys.stdin.readline

def make_base_pattern(u, v, w, x, y):
    pattern = []
    for _ in range(v):
        row = [0] * y + [1] * x + [0] * y
        pattern.append(row)
    for _ in range(w):
        row = [1] * u
        pattern.append(row)
    return pattern


def rotate_pattern(mat):
    r_len = len(mat)
    c_len = len(mat[0])
    result = []
    for c in range(c_len):
        new_row = []
        for r in range(r_len - 1, -1, -1):
            new_row.append(mat[r][c])
        result.append(new_row)
    return result


def get_patterns(base_pat):
    rotations = []
    curr = base_pat
    for _ in range(4):
        if curr not in rotations:
            rotations.append(curr)
        curr = rotate_pattern(curr)
    return rotations


def check_matching(board, N, pattern, r, c):
    p_h = len(pattern)
    p_w = len(pattern[0])

    if r + p_h > N or c + p_w > N:
        return False

    for i in range(p_h):
        for j in range(p_w):
            if board[r + i][c + j] + pattern[i][j] != 1:  # 0이면 빈틈(직사각형 X), 2면 겹친거
                return False

    return True


def find_valid_positions(board, N, rotations):
    found_positions = []

    for r in range(N):
        for c in range(N):
            matched = False
            for pat in rotations:
                if check_matching(board, N, pat, r, c):
                    matched = True
                    break
            if matched:
                found_positions.append((r, c))

    return found_positions


N = int(input())
u, v, w, x, y = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

base_pattern = make_base_pattern(u, v, w, x, y)
rotations = get_patterns(base_pattern)
valid_positions = find_valid_positions(board, N, rotations)

print(len(valid_positions))
for r, c in valid_positions:
    print(r, c)