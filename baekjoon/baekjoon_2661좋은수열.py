import sys

def is_good_sequence(sequence):
    length = len(sequence)
    # 비교할 부분 수열의 길이를 1부터 전체 길이의 절반까지 늘려가며 확인
    for i in range(1, length // 2 + 1):
        if sequence[-i:] == sequence[-2*i:-i]:
            return False
    return True

def find_sequence(current_seq):

    # 현재 수열이 나쁜 수열이면 더 이상 진행하지 않음
    if not is_good_sequence(current_seq):
        return False

    # 목표 길이에 도달하면 출력 후 종료
    if len(current_seq) == N:
        print(current_seq)
        return True

    # 1, 2, 3 순서대로 시도
    for char in "123":
        if find_sequence(current_seq + char):
            return True
    return False

N = int(sys.stdin.readline())

find_sequence("")