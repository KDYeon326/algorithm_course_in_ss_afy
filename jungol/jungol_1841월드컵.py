matches = []
for i in range(6):
    for j in range(i + 1, 6):
        matches.append((i, j))

def backtracking(match_idx, results):
    if match_idx == 15:
        return True

    country1, country2 = matches[match_idx]

    # country1 승 / country2 패
    if results[country1][0] > 0 and results[country2][2] > 0:
        results[country1][0] -= 1
        results[country2][2] -= 1
        if backtracking(match_idx + 1, results):
            return True
        results[country1][0] += 1
        results[country2][2] += 1

    # country1 무 / country2 무
    if results[country1][1] > 0 and results[country2][1] > 0:
        results[country1][1] -= 1
        results[country2][1] -= 1
        if backtracking(match_idx + 1, results):
            return True
        results[country1][1] += 1
        results[country2][1] += 1

    # country1 패 / country2 승
    if results[country1][2] > 0 and results[country2][0] > 0:
        results[country1][2] -= 1
        results[country2][0] -= 1
        if backtracking(match_idx + 1, results):
            return True
        results[country1][2] += 1
        results[country2][0] += 1

    return False

def is_valid_result(results):
    for i in range(6):
        if sum(results[i]) != 5:
            return 0

    return 1 if backtracking(0, results) else 0

answers = []
for _ in range(4):
    input_data = list(map(int, input().split()))
    results = [input_data[i:i+3] for i in range(0, 18, 3)]
    answers.append(is_valid_result(results))

print(*answers)