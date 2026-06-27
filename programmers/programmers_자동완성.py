def count_common_prefix(word1, word2):
    length = min(len(word1), len(word2))
    for i in range(length):
        if word1[i] != word2[i]:
            return i
    return length


def solution(words):
    words.sort()
    n = len(words)
    total_typing = 0

    for i in range(n):
        current_word = words[i]

        # 이전 단어와의 공통 접두사 길이 확인
        if i > 0:
            prev_len = count_common_prefix(current_word, words[i - 1])
        else:
            prev_len = 0

        # 다음 단어와의 공통 접두사 길이 확인
        if i < n - 1:
            next_len = count_common_prefix(current_word, words[i + 1])
        else:
            next_len = 0

        required_len = max(prev_len, next_len)

        # 구분하려면 공통 부분보다 1글자 더 입력해야 함
        total_typing += min(required_len + 1, len(current_word))

    return total_typing