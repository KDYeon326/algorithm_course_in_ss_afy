import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])

a = [int(x) for x in data[1::4]]
b = [int(x) for x in data[2::4]]
c = [int(x) for x in data[3::4]]
d = [int(x) for x in data[4::4]]

# C와 D의 모든 합을 딕셔너리에 카운트
cd_count = {}
for i in range(n):
    ci = c[i]
    for j in range(n):
        s = ci + d[j]
        cd_count[s] = cd_count.get(s, 0) + 1

# A와 B의 모든 합을 구하며 target = -(A+B)이 cd_count에 있는지 확인
count = 0
for i in range(n):
    ai = a[i]
    for j in range(n):
        target = -(ai + b[j])
        if target in cd_count:
            count += cd_count[target]

print(count)