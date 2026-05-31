def check_match(user, ban):
    if len(user) != len(ban):
        return False
    for user_id_char, ban_id_char in zip(user, ban):
        if ban_id_char == '*':
            continue
        if user_id_char != ban_id_char:
            return False
    return True

def find_banned_combinations(depth, user_id, banned_id, visited, current_selected, unique_sets):
    if depth == len(banned_id):
        # 순서가 달라도 같은 멤버면 동일하게 처리하기 위해 정렬 후 튜플로 변환
        unique_sets.add(tuple(sorted(current_selected)))
        return

    for i in range(len(user_id)):
        if visited[i]:
            continue

        # 불량이용자 아이디와 일치하면 선택 진행
        if check_match(user_id[i], banned_id[depth]):
            visited[i] = True
            current_selected.append(user_id[i])

            # 다음 불량 사용자 패턴 매칭을 위해 재귀 호출
            find_banned_combinations(depth + 1, user_id, banned_id, visited, current_selected, unique_sets)

            # 다시 원상복구
            current_selected.pop()
            visited[i] = False


def solution(user_id, banned_id):
    unique_sets = set()
    visited = [False] * len(user_id)
    current_selected = []

    find_banned_combinations(0, user_id, banned_id, visited, current_selected, unique_sets)
    return len(unique_sets)