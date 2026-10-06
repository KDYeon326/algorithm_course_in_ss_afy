import heapq
import sys

input = sys.stdin.readline

def build_graph(edge_count):
    graph = {}
    for _ in range(edge_count):
        u, v, weight = input().split()
        weight = int(weight)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    return graph


# 헛간을 시작점으로 다익스트라 써서 소가 있는 목장(A~Y)를 만나는 순간 끝
def find_fastest_cow_dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 팝한 노드가 소의 목장(A ~ Y)인 경우, 가장 먼저 도달하는 소
        if "A" <= current_node <= "Y":
            return current_node, current_distance

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return "", float("inf")


edge_count = int(input().strip())
graph = build_graph(edge_count)
fastest_cow, min_distance = find_fastest_cow_dijkstra(graph, "Z")
print(f"{fastest_cow} {min_distance}")