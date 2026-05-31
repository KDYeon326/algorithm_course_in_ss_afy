from collections import deque


def check_able_to_change(word1, word2):
    # 두 단어가 한 글자만 다른지 확인
    count_different_string = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            count_different_string += 1
            if count_different_string > 1:
                return False
    return count_different_string == 1


def solution(begin, target, words):
    # target이 words에 없으면 변환 불가능
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, steps = queue.popleft()

        # 목표 단어에 도달하면 현재까지의 변환 횟수 반환
        if current_word == target:
            return steps

        for word in words:
            if word not in visited and check_able_to_change(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0