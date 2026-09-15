import sys

input = sys.stdin.readline().split()
n = int(input[0])
heights = [int(x) for x in input[1:]]


def get_max_histogram_area(heights):
    stack = []
    max_area = 0
    length = len(heights)

    for i in range(length):
        h = heights[i]

        # 내 높이보다 작은게 나오면 더 가로로 넓어질 수 없으니까 넓이 최대값 갱신하고 다시 돌려.
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - 1 - stack[-1]
            max_area = max(max_area, height * width)
        stack.append(i)

    # 근데 계속 높아지면 pop 안되니깐 남아있는거 계산
    while stack:
        height = heights[stack.pop()]
        width = length if not stack else length - 1 - stack[-1]
        max_area = max(max_area, height * width)

    return max_area


print(get_max_histogram_area(heights))