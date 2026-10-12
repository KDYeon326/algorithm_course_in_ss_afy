import sys

input = sys.stdin.readline

def find_virus(programs, k):
    prog_a = programs[0]
    prog_b = programs[1]

    a_len = len(prog_a)
    b_len = len(prog_b)

    for length in range(min(a_len, b_len), k - 1, -1):
        # 첫 번째 프로그램의 조각들을 해시셋에 담기 (정방향 + 역방향)
        a_set = set()
        for i in range(a_len - length + 1):
            sub = tuple(prog_a[i:i + length])
            a_set.add(sub)
            a_set.add(sub[::-1])

        # 두 번째 프로그램의 조각들도 해시셋에 담기
        b_set = set()
        for i in range(b_len - length + 1):
            sub = tuple(prog_b[i:i + length])
            b_set.add(sub)
            b_set.add(sub[::-1])

        # 교집합(&)으로 두 프로그램에 공통으로 있는 후보만 추출
        common_candidates = a_set & b_set

        if not common_candidates:
            continue

        if len(programs) == 1:
            return False

        # 프로그램이 딱 2개인 경우, 교집합이 존재하기만 하면 바로 YES
        if len(programs) == 2:
            return True

        # 프로그램이 3개 이상인 경우, 나머지 프로그램들에도 다 들어있는지 확인
        for sub in common_candidates:
            sub_list = list(sub)
            rev_list = list(sub[::-1])

            is_common = True
            for prog in programs[2:]:
                if not contains_subsequence(prog, sub_list, rev_list):
                    is_common = False
                    break

            if is_common:
                return True

    return False


def contains_subsequence(prog, target, target_rev):
    m = len(prog)
    t_len = len(target)

    for i in range(m - t_len + 1):
        segment = prog[i:i + t_len]
        if segment == target or segment == target_rev:
            return True
    return False


n, k = map(int, input().split())

programs = []
for _ in range(n):
    m = int(input())
    prog = list(map(int, input().split()))
    programs.append(prog)

if find_virus(programs, k):
    print("YES")
else:
    print("NO")


'''
N, K = map(int, input().split())

MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 31


def get_hashes(arr):
    size = len(arr)

    powers1 = [1] * (size + 1)
    powers2 = [1] * (size + 1)
    hash1 = [0] * (size + 1)
    hash2 = [0] * (size + 1)

    for i in range(size):
        powers1[i + 1] = powers1[i] * BASE % MOD1
        powers2[i + 1] = powers2[i] * BASE % MOD2

        hash1[i + 1] = (hash1[i] * BASE + arr[i]) % MOD1
        hash2[i + 1] = (hash2[i] * BASE + arr[i]) % MOD2

    return hash1, hash2, powers1, powers2


def get_subhash(h1, h2, p1, p2, start, end):
    length = end - start

    value1 = (h1[end] - h1[start] * p1[length]) % MOD1
    value2 = (h2[end] - h2[start] * p2[length]) % MOD2

    return value1, value2


common = None

for _ in range(N):
    M = int(input())
    arr = list(map(int, input().split()))

    reverse_arr = arr[::-1]

    h1, h2, p1, p2 = get_hashes(arr)
    rh1, rh2, rp1, rp2 = get_hashes(reverse_arr)

    current = set()

    for i in range(M - K + 1):
        forward = get_subhash(h1, h2, p1, p2, i, i + K)
        backward = get_subhash(
            rh1, rh2, rp1, rp2,
            M - i - K, M - i
        )

        current.add(min(forward, backward))

    if common is None:
        common = current
    else:
        common.intersection_update(current)

    if not common:
        print("NO")
        break
else:
    print("YES")
'''