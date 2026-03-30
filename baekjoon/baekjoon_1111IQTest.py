import sys

def find_simultaneous_equations_rule(arr):
    # 연립방정식 규칙을 적용해.
    # 인덱스 0, 1, 2만 이용.
    if arr[1] == arr[0]:
        return 0, arr[1]

    # a와 b는 모두 정수니까 // 연산자 사용 (안되면 규칙이 깨져버리는거다)
    a = (arr[2] - arr[1]) // (arr[1] - arr[0])
    b = arr[1] - (a * arr[0])
    return a, b


def validate(arr, a, b):
    # 위에서 찾은 연립방정식을 다른 인덱스의 수에도 적용
    for i in range(len(arr) - 1):
        if arr[i + 1] != (arr[i] * a + b):
            return False
    return True


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print("A")

elif N == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print("A")

else:
    # 연립방정식을 풀어.
    a, b = find_simultaneous_equations_rule(nums)

    # 일관성 검증
    if validate(nums, a, b):
        print(nums[-1] * a + b)
    else:
        print("B")