import sys

input = sys.stdin.read


def rotate_layer(grid, n, m, r, layer, result):
    top, left = layer, layer
    bottom, right = n - 1 - layer, m - 1 - layer

    elements = []

    # 원본 grid에서 반시계 방향 순서대로 원소 추출
    for c in range(left, right):
        elements.append(grid[top][c])
    for r_idx in range(top, bottom):
        elements.append(grid[r_idx][right])
    for c in range(right, left, -1):
        elements.append(grid[bottom][c])
    for r_idx in range(bottom, top, -1):
        elements.append(grid[r_idx][left])

    total_length = len(elements)
    shift = r % total_length

    # 반시계 방향 이동 적용
    rotated = elements[shift:] + elements[:shift]

    idx = 0
    # 새로운 빈 배열(result)의 해당 위치에 회전된 값 채우기
    for c in range(left, right):
        result[top][c] = rotated[idx]
        idx += 1
    for r_idx in range(top, bottom):
        result[r_idx][right] = rotated[idx]
        idx += 1
    for c in range(right, left, -1):
        result[bottom][c] = rotated[idx]
        idx += 1
    for r_idx in range(bottom, top, -1):
        result[r_idx][left] = rotated[idx]
        idx += 1


input_data = input().split()

n = int(input_data[0])
m = int(input_data[1])
r = int(input_data[2])

grid = []
idx = 3
for _ in range(n):
    grid.append([int(x) for x in input_data[idx : idx + m]])
    idx += m

# 같은 크기의 새로운 빈 배열 생성
result = [[0] * m for _ in range(n)]

layers = min(n, m) // 2
for layer in range(layers):
    rotate_layer(grid, n, m, r, layer, result)

for row in result:
    print(*(row))