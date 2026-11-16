import sys
import math
import heapq

input = sys.stdin.readline


def calculate_distance(point_a, point_b):
    delta_x = point_a[0] - point_b[0]
    delta_y = point_a[1] - point_b[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


station_count, max_refuels = map(int, input().split())

stations = [(0, 0)]
for _ in range(station_count):
    x, y = map(int, input().split())
    stations.append((x, y))
stations.append((10000, 10000))

total_nodes = station_count + 2

graph = [[] for _ in range(total_nodes)]
for now_index in range(total_nodes):
    for next_index in range(total_nodes):
        if now_index == next_index:
            continue

        distance = calculate_distance(stations[now_index], stations[next_index])

        # 필요한 연료량 계산 (1리터당 10km)
        fuel_needed = math.ceil(distance / 10)

        graph[now_index].append((next_index, fuel_needed))  # (다음 비행장, 가는데 드는 연료량)

pq = []
heapq.heappush(pq, (0, 0, 0))  # (현재까지 필요한 최대 연료통 용량, 현재 정점, 사용한 급유 횟수)

min_fuel_required = [float('inf')] * total_nodes
min_fuel_required[0] = 0

while pq:
    now_max_fuel, now_index, refuel_count = heapq.heappop(pq)

    if now_index == total_nodes - 1:  # 도착
        print(now_max_fuel)
        break

    if now_max_fuel > min_fuel_required[now_index]:  # 가지치기
        continue

    for next_index, fuel_needed in graph[now_index]:
        next_max_fuel = max(now_max_fuel, fuel_needed)  # 갈수있는 연료를 확인해서

        if next_index != total_nodes - 1:  # 급유 필요
            next_refuel_count = refuel_count + 1
        else:  # 급유 안필요
            next_refuel_count = refuel_count

        if next_refuel_count <= max_refuels:  # 최대 급유 횟수 안넘으면
            if next_max_fuel < min_fuel_required[next_index]:  # 다음 급유지 가는 연료량이 이전 최적 루트 보다 더 적으면 = 더 효율적인 경로 찾으면
                min_fuel_required[next_index] = next_max_fuel
                heapq.heappush(pq, (next_max_fuel, next_index, next_refuel_count))