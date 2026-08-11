import sys

input = sys.stdin.readline

n, k = map(int, input().split())
switches = list(map(int, input().split()))

pressed = [0] * n
active_press_count = 0
total_press_count = 0
possible = True

for i in range(n):
    # i - k 위치에서 눌렀던 스위치는 [i-k, i-1]까지만 미치므로 i번째부터는 영향 X
    if i >= k:
        active_press_count -= pressed[i - k]

    # active_press_count가 홀수면 상태 반전 (1 - x), 짝수면 그대로 유지
    if active_press_count % 2 == 1:
        current_state = 1 - switches[i]
    else:
        current_state = switches[i]

    # 가장 왼쪽 스위치가 1이면 0으로 만드는 유일한 방법은 i에서 누르는 것
    if current_state == 1:
        # i부터 K개를 누를 범위가 부족하면 모든 스위치를 0으로 만들기 불가능
        if i + k > n:
            possible = False
            break

        pressed[i] = 1
        active_press_count += 1
        total_press_count += 1

if possible:
    print(total_press_count)
else:
    print(-1)