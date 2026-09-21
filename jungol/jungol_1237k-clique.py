import sys

input = sys.stdin.readline

def find_cliques(current_node, current_clique):
    if len(current_clique) > 0:
        counts[len(current_clique) - 1] += 1

    for next_node in range(current_node + 1, n):
        # 연결 여부 확인용
        is_connected_to_all = True

        # 기존 클리큐에 있는 모든 노드와 하나씩 비교
        for node in current_clique:
            if matrix[node][next_node] == 0:  # 연결되어 있지 않다면
                is_connected_to_all = False
                break  # 가지치기

        # 모두 연결되어 있는 경우 진행
        if is_connected_to_all:
            current_clique.append(next_node)
            find_cliques(next_node, current_clique)
            current_clique.pop()


n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]
counts = [0] * n

find_cliques(-1, [])

print(", ".join(map(str, counts)))