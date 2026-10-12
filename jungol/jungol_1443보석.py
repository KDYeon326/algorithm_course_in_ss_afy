import sys

input = sys.stdin.readline

N, M, T, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(T)]

# 정사각형의 왼쪽 아래 꼭짓점의 x, y 좌표 후보
# 정사각형이 지도를 벗어나지 않도록 양 끝 좌표를 추가
xs = {0, N - K}
ys = {0, M - K}

for x, y in gems:
    # 금강석을 정사각형의 왼쪽 변에 맞추는 경우
    # 금강석의 x 좌표가 정사각형의 왼쪽 좌표가 됨
    xs.add(max(0, min(x, N - K)))

    # 금강석을 정사각형의 오른쪽 변에 맞추는 경우
    # 정사각형의 왼쪽 좌표는 금강석의 x 좌표 - K
    xs.add(max(0, min(x - K, N - K)))

    # 금강석을 정사각형의 아래쪽 변에 맞추는 경우
    ys.add(max(0, min(y, M - K)))

    # 금강석을 정사각형의 위쪽 변에 맞추는 경우
    ys.add(max(0, min(y - K, M - K)))

# 정사각형에 포함되는 금강석의 최대 개수
max_count = 0

# 최댓값을 만드는 정사각형의 왼쪽 아래 x 좌표와 문제에서 요구하는 왼쪽 위 y 좌표
answer_x = 0
answer_y = 0

for x in xs:
    for y in ys:
        count = 0

        # 금강석이 현재 정사각형에 있는지 확인
        for gx, gy in gems:
            if x <= gx <= x + K and y <= gy <= y + K:
                count += 1

        if count > max_count:
            max_count = count
            answer_x = x

            # y는 왼쪽 아래 꼭짓점의 좌표이므로 왼쪽 위 꼭짓점의 y 좌표는 y + K
            answer_y = y + K

print(answer_x, answer_y)
print(max_count)