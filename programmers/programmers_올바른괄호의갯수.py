def count_valid_parentheses(open_count, close_count, n):
    # 괄호 쌍이 모두 완성된 경우 1개 찾음
    if open_count == n and close_count == n:
        return 1

    total_count = 0

    # 여는 괄호를 더 사용할 수 있는 경우
    if open_count < n:
        total_count += count_valid_parentheses(open_count + 1, close_count, n)

    # 닫는 괄호를 더 사용할 수 있는 경우
    if open_count > close_count:
        total_count += count_valid_parentheses(open_count, close_count + 1, n)

    return total_count


def solution(n):
    return count_valid_parentheses(0, 0, n)