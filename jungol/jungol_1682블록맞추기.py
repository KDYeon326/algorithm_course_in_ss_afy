import sys
from collections import deque

input_line = sys.stdin.readline


def find_block_bounds(start_row, start_column):
    queue = deque([(start_row, start_column)])
    board[start_row][start_column] = 2
    max_column = start_column
    max_row = start_row

    while queue:
        current_row, current_column = queue.popleft()
        for neighbor_row, neighbor_column in ((current_row, current_column + 1),
                                              (current_row + 1, current_column),
                                              (current_row, current_column - 1),
                                              (current_row - 1, current_column)):
            if 0 <= neighbor_row < board_size and 0 <= neighbor_column < board_size and board[neighbor_row][
                neighbor_column] == 1:
                board[neighbor_row][neighbor_column] = 2
                queue.append((neighbor_row, neighbor_column))
                if neighbor_column > max_column:
                    max_column = neighbor_column
                if neighbor_row > max_row:
                    max_row = neighbor_row

    return max_column, max_row


def validate_internal_void_space(start_row, start_column, max_column, max_row):
    for void_row in range(start_row, max_row + 1):
        for void_column in range(start_column, max_column + 1):
            if board[void_row][void_column] == 0:
                scan_row, scan_column = void_row, void_column
                void_height = 0
                void_width = 0

                while scan_row <= max_row and board[scan_row][void_column] == 0:
                    void_height += 1
                    scan_row += 1

                while scan_column <= max_column and board[void_row][scan_column] == 0:
                    void_width += 1
                    scan_column += 1

                for inner_row in range(void_row, void_row + void_height):
                    for inner_column in range(void_column, void_column + void_width):
                        if board[inner_row][inner_column] != 0:
                            return False, ""

                if void_row == start_row:
                    if x == void_height and y == void_width and (void_column - start_column) == (u - (w + y)) and (
                            max_column - start_column + 1) == u:
                        return True, 'u'
                elif scan_column == max_column + 1:
                    if x == void_width and y == void_height and (void_row - start_row) == (u - (w + y)) and (
                            max_row - start_row + 1) == u:
                        return True, 'r'
                elif scan_row == max_row + 1:
                    if x == void_height and y == void_width and (void_column - start_column) == w and (
                            max_column - start_column + 1) == u:
                        return True, 'd'
                elif void_column == start_column:
                    if x == void_width and y == void_height and (void_row - start_row) == w and (
                            max_row - start_row + 1) == u:
                        return True, 'l'

                return False, ""

    return False, ""


def validate_protruding_extension(start_row, start_column, max_column, max_row, direction):
    if direction == 'u':
        extension_start_row = start_row - v
        if extension_start_row < 0:
            return False
        for row in range(extension_start_row, start_row):
            for column in range(start_column, max_column + 1):
                if board[row][column] != 0:
                    return False
    elif direction == 'r':
        extension_end_column = max_column + v
        if extension_end_column >= board_size:
            return False
        for row in range(start_row, max_row + 1):
            for column in range(max_column + 1, extension_end_column + 1):
                if board[row][column] != 0:
                    return False
    elif direction == 'd':
        extension_end_row = max_row + v
        if extension_end_row >= board_size:
            return False
        for row in range(max_row + 1, extension_end_row + 1):
            for column in range(start_column, max_column + 1):
                if board[row][column] != 0:
                    return False
    else:
        extension_start_column = start_column - v
        if extension_start_column < 0:
            return False
        for row in range(start_row, max_row + 1):
            for column in range(extension_start_column, start_column):
                if board[row][column] != 0:
                    return False

    return True


board_size = int(input_line().strip())
u, v, w, x, y = map(int, input_line().split())
board = [list(map(int, input_line().split())) for _ in range(board_size)]

match_count = 0
match_positions = []

for row_index in range(board_size):
    for column_index in range(board_size):
        if board[row_index][column_index] == 1:
            max_column, max_row = find_block_bounds(row_index, column_index)
            is_valid, direction = validate_internal_void_space(row_index, column_index, max_column, max_row)

            if is_valid and validate_protruding_extension(row_index, column_index, max_column, max_row, direction):
                match_count += 1
                match_positions.append((row_index + 1, column_index + 1))

print(match_count)
for position in match_positions:
    print(position[0], position[1])