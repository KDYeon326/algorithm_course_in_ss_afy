import sys
input = sys.stdin.readline

calculate_limit = 10**9


def num(stack, x):
    stack.append(x)
    return True


def pop(stack):
    if not stack:
        return False
    stack.pop()
    return True


def inv(stack):
    if not stack:
        return False
    stack[-1] = -stack[-1]
    return True


def dup(stack):
    if not stack:
        return False
    stack.append(stack[-1])
    return True


def swp(stack):
    if len(stack) < 2:
        return False
    stack[-1], stack[-2] = stack[-2], stack[-1]
    return True


def add(stack):
    if len(stack) < 2:
        return False
    a = stack.pop()
    b = stack.pop()
    result = b + a
    if abs(result) > calculate_limit:
        return False
    stack.append(result)
    return True


def sub(stack):
    if len(stack) < 2:
        return False
    a = stack.pop()
    b = stack.pop()
    result = b - a
    if abs(result) > calculate_limit:
        return False
    stack.append(result)
    return True


def mul(stack):
    if len(stack) < 2:
        return False
    a = stack.pop()
    b = stack.pop()
    result = b * a
    if abs(result) > calculate_limit:
        return False
    stack.append(result)
    return True


def div(stack):
    if len(stack) < 2:
        return False

    a = stack.pop()
    b = stack.pop()

    if a == 0:
        return False

    result = abs(b) // abs(a)

    if (a < 0) ^ (b < 0):
        result = -result

    if abs(result) > calculate_limit:
        return False

    stack.append(result)
    return True


def mod(stack):
    if len(stack) < 2:
        return False

    a = stack.pop()
    b = stack.pop()

    if a == 0:
        return False

    result = abs(b) % abs(a)

    if b < 0:
        result = -result

    if abs(result) > calculate_limit:
        return False

    stack.append(result)
    return True


def run_ghostack(ghostack, start):

    stack = [start]

    for cmd in ghostack:

        if cmd[0] == "NUM":
            if not num(stack, int(cmd[1])):
                return "ERROR"

        elif cmd[0] == "POP":
            if not pop(stack):
                return "ERROR"

        elif cmd[0] == "INV":
            if not inv(stack):
                return "ERROR"

        elif cmd[0] == "DUP":
            if not dup(stack):
                return "ERROR"

        elif cmd[0] == "SWP":
            if not swp(stack):
                return "ERROR"

        elif cmd[0] == "ADD":
            if not add(stack):
                return "ERROR"

        elif cmd[0] == "SUB":
            if not sub(stack):
                return "ERROR"

        elif cmd[0] == "MUL":
            if not mul(stack):
                return "ERROR"

        elif cmd[0] == "DIV":
            if not div(stack):
                return "ERROR"

        elif cmd[0] == "MOD":
            if not mod(stack):
                return "ERROR"

    if len(stack) != 1:
        return "ERROR"

    return stack[0]


while True:

    ghostack = []

    while True:
        line = input().strip()

        if line == "QUIT":
            sys.exit()

        if line == "END":
            break

        ghostack.append(line.split())

    n = int(input())

    for _ in range(n):
        start = int(input())
        print(run_ghostack(ghostack, start))

    input()
    print()