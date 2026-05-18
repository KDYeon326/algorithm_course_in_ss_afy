from itertools import product


def get_hint(candidate, target):
    s = 0
    b = 0
    for i in range(4):
        if candidate[i] == target[i]:
            s += 1
        elif candidate[i] in target:
            b += 1
    return f"{s}S {b}B"


def solution(n, submit):
    # 1111 ~ 9999까지 후보 생성.
    each_num_string = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    candidates = []

    for a in each_num_string:
        for b in each_num_string:
            for c in each_num_string:
                for d in each_num_string:
                    num_str = a + b + c + d
                    candidates.append(num_str)

    possible_passwords = []
    for word in candidates:  # 서로 다른 숫자이므로 set 써서 4자리 아니면 제거
        if len(set(word)) == 4:
            possible_passwords.append(word)

    # n번의 기회 동안 질문
    for _ in range(n):
        # 남은 후보 중 첫 번째 숫자를 제출
        guess = possible_passwords[0]
        result = submit(int(guess))

        # 정답이면 종료
        if result == "4S 0B":
            return int(guess)

        # 숫자야구 룰에 맞는 후보 필터링
        new_possible = []
        for candi in possible_passwords:
            if get_hint(guess, candi) == result:
                new_possible.append(candi)

        possible_passwords = new_possible

    return int(possible_passwords[0])