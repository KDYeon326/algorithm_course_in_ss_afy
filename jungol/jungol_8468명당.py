import heapq
import sys

input = sys.stdin.readline


def push_heaps(max_heap, min_heap, height, index):
    # 구간 왼쪽 경계 start가 이동했을 때 이미 구간 밖인지 판별하기 위해 index도 같이 저장
    heapq.heappush(max_heap, (-height, index))
    heapq.heappush(min_heap, (height, index))


def get_current_diff(max_heap, min_heap, start_index):
    # 현재 구간에 속하지 않는 원소들을 힙 최상단에서 제거
    # 원소가 삽입될 때 바로 지우지 않고, 실제 최댓값/최솟값 후보로 올라왔을 때만 유효성을 검사 Laze Deletion
    while max_heap and max_heap[0][1] < start_index:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0][1] < start_index:
        heapq.heappop(min_heap)

    current_max = -max_heap[0][0]
    current_min = min_heap[0][0]
    return current_max - current_min


def find_max_length_by_two_pointers(heights, max_diff):
    max_heap = []
    min_heap = []
    start = 0
    best_length = 0

    # 최대 유효 구간 검색
    for end, height in enumerate(heights):
        push_heaps(max_heap, min_heap, height, end)

        # 구간의 높이 차가 max_diff를 초과하면 조건을 만족할 때까지 start를 당깁니다.
        # start가 증가하면 이전 start 위치에 있던 원소들은 이후 get_current_diff에서 유효 범위 밖으로 걸러집니다.
        while get_current_diff(max_heap, min_heap, start) > max_diff:
            start += 1

        current_length = end - start + 1
        if current_length > best_length:
            best_length = current_length

    return best_length


zone_count, max_diff = map(int, input().split())
heights = list(map(int, input().split()))

print(find_max_length_by_two_pointers(heights, max_diff))