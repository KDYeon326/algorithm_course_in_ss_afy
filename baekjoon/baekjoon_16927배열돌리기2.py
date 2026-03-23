import sys
input = sys.stdin.readline

def get_bounds(depth):
    top = depth
    left = depth
    bottom = N - 1 - depth
    right = M - 1 - depth
    return top, left, bottom, right


def extract(depth):
    top, left, bottom, right = get_bounds(depth)
    result = []

    # 위
    for j in range(left, right):
        result.append(arr[top][j])

    # 오른쪽
    for i in range(top, bottom):
        result.append(arr[i][right])

    # 아래
    for j in range(right, left, -1):
        result.append(arr[bottom][j])

    # 왼쪽
    for i in range(bottom, top, -1):
        result.append(arr[i][left])

    return result


def insert(depth, data):
    top, left, bottom, right = get_bounds(depth)
    idx = 0

    for j in range(left, right):
        arr[top][j] = data[idx]
        idx += 1

    for i in range(top, bottom):
        arr[i][right] = data[idx]
        idx += 1

    for j in range(right, left, -1):
        arr[bottom][j] = data[idx]
        idx += 1

    for i in range(bottom, top, -1):
        arr[i][left] = data[idx]
        idx += 1


def rotate(data):
    k = R % len(data)
    return data[k:] + data[:k]


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for depth in range(min(N, M) // 2):
    direction_data = extract(depth)
    rotated_data = rotate(direction_data)
    insert(depth, rotated_data)

for row in arr:
    print(*row)