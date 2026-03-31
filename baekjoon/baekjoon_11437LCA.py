import sys
from collections import deque

input = sys.stdin.readline

# BFS로 부모와 깊이 찾기
def find_structure_bfs(start_node):
    queue = deque([start_node])
    depth[start_node] = 0

    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if depth[neighbor] == -1:
                depth[neighbor] = depth[curr] + 1
                parent[neighbor] = curr
                queue.append(neighbor)


# 공통 조상 찾기
def get_lca(a, b):
    # a가 더 깊도록
    if depth[a] < depth[b]:
        a, b = b, a

    # 두 노드의 높이가 같아질 때까지 a를 올려
    while depth[a] != depth[b]:
        a = parent[a]

    # 두 노드가 같아질 때까지 둘 다 위로 올려
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (n + 1)
depth = [-1] * (n + 1)

find_structure_bfs(1)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(get_lca(u, v))