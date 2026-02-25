import sys
input = sys.stdin.readline

def can_clear(max_hp):
    cur_hp = max_hp
    atk = A

    for t, a, h in rooms:
        if t == 1:  # 몬스터
            hits = (h + atk - 1) // atk
            damage = (hits - 1) * a
            cur_hp -= damage
            if cur_hp <= 0:
                return False
        else:  # 포션
            atk += a
            cur_hp = min(max_hp, cur_hp + h)

    return True


N, A = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(N)]

left = 1
right = 10**18
answer = right

while left <= right:
    mid = (left + right) // 2
    if can_clear(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)