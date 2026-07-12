tree_children = []  # 트리 구조
next_child_pointer = []  # 어느 간선으로 내려보낼껀지


def initialize_tree(edges, total_nodes):

    global tree_children, next_child_pointer

    tree_children = [[] for _ in range(total_nodes + 1)]
    next_child_pointer = [0] * (total_nodes + 1)

    # 부모 노드 인덱스에 자식 노드 추가
    for parent, child in edges:
        tree_children[parent].append(child)

    # 각 노드의 자식 노드 정렬
    for i in range(1, total_nodes + 1):
        tree_children[i].sort()


def drop_cards():
    # 루트(1번)에서 출발하여 리프 노드까지 트리 리스트를 왔다갔다 하며 아래로


    current_node = 1

    # 리프 노드까지 계속 내려감
    while tree_children[current_node]:
        parent = current_node
        pointer = next_child_pointer[parent]

        # 현재 가리키고 있는 자식 노드로 이동
        current_node = tree_children[parent][pointer]

        # 이 부모 노드를 다음에 방문할 때는 다음 자식을 가리키도록 간선 바꾸기
        next_child_pointer[parent] = (pointer + 1) % len(tree_children[parent])

    return current_node


def verify_target(visit_counts, target, total_nodes):
    # 각 리프 노드가 방문된 횟수로 target을 만들 수 있는지 검사

    satisfied_count = 0
    leaf_node_count = 0

    for i in range(1, total_nodes + 1):

        # 자식이 있다면 리프 노드가 아니므로 건너뜀
        if tree_children[i]:
            continue

        leaf_node_count += 1
        count = visit_counts[i]
        target_val = target[i - 1]

        # 한 번도 안 왔는데 목표치가 있다면 아직 더 던져야 함
        if count == 0:
            if target_val == 0:
                satisfied_count += 1
            continue

        # 1로만 다 채웠을 때 초과하면 탈락 (영원히 불가능)
        if count * 1 > target_val:
            return "FAIL"

        # 1만 채운 것과 3으로 다 채운 것 사이에 target이 들어오면 만족
        if count * 1 <= target_val <= count * 3:
            satisfied_count += 1

    # 모든 리프 노드가 만족하면 성공, 아니면 계속 진행
    if satisfied_count == leaf_node_count:
        return "SUCCESS"
    return "KEEP_GOING"


def make_cards_numbers(drop_history, target):
    # 공이 떨어진 순서를 바탕으로 사전 순으로 가장 작은 1, 2, 3 조합을 만듭니다.

    total_drops = len(drop_history)
    result_cards = [1] * total_drops

    # 각 노드별로 남은 점수 계산
    remaining_scores = [0] + list(target)  # 인덱스 맞추기 위해 앞에 [0] 추가
    for node in drop_history:
        remaining_scores[node] -= 1

    # 사전 순 최적화를 위해 맨 뒤의 공부터 역순으로 탐색하며 점수를 채움
    for i in range(total_drops - 1, -1, -1):
        node = drop_history[i]

        if remaining_scores[node] >= 2:
            result_cards[i] += 2
            remaining_scores[node] -= 2
        elif remaining_scores[node] == 1:
            result_cards[i] += 1
            remaining_scores[node] -= 1

    return result_cards


def solution(edges, target):
    total_nodes = len(target)

    # 트리 구조 생성
    initialize_tree(edges, total_nodes)

    drop_history = []
    visit_counts = [0] * (total_nodes + 1)

    # 조건을 만족하거나 실패할 때까지 트리 안을 왔다갔다 반복 이동
    while True:
        # 루트에서 출발해 리프 노드까지 이동
        reached_leaf = drop_cards()

        drop_history.append(reached_leaf)
        visit_counts[reached_leaf] += 1

        # 검사
        status = verify_target(visit_counts, target, total_nodes)

        if status == "SUCCESS":
            break
        elif status == "FAIL":
            return [-1]

    # 사전 순으로 가장 빠른 1, 2, 3 카드 배열 구성
    return make_cards_numbers(drop_history, target)