import sys
input = sys.stdin.readline

def change_oven_diameter(oven, d):
    for i in range(1, d):
        oven[i] = min(oven[i], oven[i-1]) # 위가 좁으면 오븐이 넓어도 의미 없어서 위쪽 중에 가장 최솟값이 현재 오븐의 넓이와 같다
    return oven


def bake_pizza(oven, pizza, d, n):
    oven_height = d - 1

    for i in range(n):  # 맨 아래부터 오븐 층부터 피자 넣을 수 있는지
        while oven_height >= 0 and oven[oven_height] < pizza[i]:
            oven_height -= 1

        if oven_height < 0:  # 맨 위까지 못넣으면 그냥 피자가 큰거임
            return 0

        oven_height -= 1

    return oven_height + 2


d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

oven = change_oven_diameter(oven, d)

result = bake_pizza(oven, pizza, d, n)

print(result)