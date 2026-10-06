import heapq
import sys

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = int(1e9)


# 기존 회로가 있는 곳에 비용을 k로 갱신
def mark_circuit_line(grid, r1, c1, r2, c2, k):
    if r1 == r2:
        start_c = min(c1, c2)
        end_c = max(c1, c2)
        for c in range(start_c, end_c + 1):
            grid[r1][c] = k
    elif c1 == c2:
        start_r = min(r1, r2)
        end_r = max(r1, r2)
        for r in range(start_r, end_r + 1):
            grid[r][c1] = k


# 기존 회로 정보를 순회하며 스캔
def process_existing_circuits(grid, k):
    num_circuits = int(input())
    for _ in range(num_circuits):
        data = list(map(int, input().split()))
        count = data[0]
        points = data[1:]
        for i in range(count - 1):
            r1, c1 = points[2 * i], points[2 * i + 1]
            r2, c2 = points[2 * (i + 1)], points[2 * (i + 1) + 1]
            mark_circuit_line(grid, r1, c1, r2, c2, k)


# 시작점에서 도착점까지의 최소 비용과 해당 경로 탐색
def dijkstra(grid, start_r, start_c, end_r, end_c, n):
    distances = [[INF] * (n + 1) for _ in range(n + 1)]
    parent = [[None] * (n + 1) for _ in range(n + 1)]

    pq = []
    distances[start_r][start_c] = grid[start_r][start_c]
    heapq.heappush(pq, (grid[start_r][start_c], start_r, start_c))

    while pq:
        current_cost, r, c = heapq.heappop(pq)

        if r == end_r and c == end_c:
            break

        if current_cost > distances[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 1 <= nr <= n and 1 <= nc <= n:
                next_cost = current_cost + grid[nr][nc]
                if next_cost < distances[nr][nc]:
                    distances[nr][nc] = next_cost
                    parent[nr][nc] = (r, c)
                    heapq.heappush(pq, (next_cost, nr, nc))

    path = []
    curr = (end_r, end_c)
    while curr is not None:
        path.append(curr)
        curr = parent[curr[0]][curr[1]]
    path.reverse()

    return distances[end_r][end_c], path


# 꺾이는 부분만 추출
def extract_corners(path):
    if len(path) <= 2:
        return path

    corners = [path[0]]
    for i in range(1, len(path) - 1):
        prev_r, prev_c = path[i - 1]
        curr_r, curr_c = path[i]
        next_r, next_c = path[i + 1]

        if (curr_r - prev_r, curr_c - prev_c) != (next_r - curr_r, next_c - curr_c):
            corners.append(path[i])

    corners.append(path[-1])
    return corners


n = int(input())
start_r, start_c, end_r, end_c = map(int, input().split())
k = int(input())

grid = [[1] * (n + 1) for _ in range(n + 1)]
process_existing_circuits(grid, k)

min_cost, path = dijkstra(grid, start_r, start_c, end_r, end_c, n)
corners = extract_corners(path)

print(min_cost)
result_list = [len(corners)]
for r, c in corners:
    result_list.append(r)
    result_list.append(c)
print(*(result_list))