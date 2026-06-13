import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    visited = [False] * len(operations)

    for i, operation in enumerate(operations):
        command, value = operation.split()
        num = int(value)

        if command == "I":

            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True  # 현재 데이터는 큐에 존재

        elif command == "D":
            if num == 1:
                # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    visited[idx] = False  # 삭제
            elif num == -1:
                # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    visited[idx] = False  # 삭제

    # 모든 연산이 끝난 후, 각각의 힙에 남아있는 더미 데이터 정리
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 큐가 비어있다면 [0, 0] 반환, 남아있다면 [최댓값, 최솟값] 반환
    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]