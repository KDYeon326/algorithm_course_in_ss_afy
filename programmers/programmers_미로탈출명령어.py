def solution(n, m, x, y, r, c, k):
    dist = abs(r - x) + abs(c - y)

    if k < dist or (k - dist) % 2 != 0:
        return "impossible"

    answer = []

    while k > 0:
        if x < n:
            if abs(r - (x + 1)) + abs(c - y) <= k - 1:
                x += 1
                answer.append("d")
                k -= 1
                continue

        if y > 1:
            if abs(r - x) + abs(c - (y - 1)) <= k - 1:
                y -= 1
                answer.append("l")
                k -= 1
                continue

        if y < m:
            if abs(r - x) + abs(c - (y + 1)) <= k - 1:
                y += 1
                answer.append("r")
                k -= 1
                continue

        if x > 1:
            if abs(r - (x - 1)) + abs(c - y) <= k - 1:
                x -= 1
                answer.append("u")
                k -= 1
                continue

    return "".join(answer)