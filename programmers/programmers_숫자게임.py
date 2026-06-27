from collections import deque

def solution(A, B):

    A.sort(reverse=True)
    B.sort(reverse=True)

    # 잦은 pop(0)의 효율성을 위해 deque로 변환
    queue_b = deque(B)
    score = 0

    for a_num in A:
        # B팀의 가장 큰 카드가 A팀의 가장 큰 카드보다 크다면 승리
        if queue_b[0] > a_num:
            queue_b.popleft()  # 가장 큰 카드 사용
            score += 1
        else:
            queue_b.pop()  # 이길 수 없다면 가장 작은 카드를 버림

    return score