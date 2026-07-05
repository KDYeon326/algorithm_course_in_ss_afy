def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


def solution(n, costs):
    total_cost = 0
    edges_count = 0
    parent = list(range(n))

    # 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    for island_a, island_b, cost in costs:
        # 두 섬의 부모 노드가 다르다면(사이클 x) 간선 추가
        if find(parent, island_a) != find(parent, island_b):
            union(parent, island_a, island_b)
            total_cost += cost
            edges_count += 1

            # 모든 섬이 연결되었으면 종료 (간선의 개수는 n - 1개)
            if edges_count == n - 1:
                break

    return total_cost