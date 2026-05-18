import sys

sys.setrecursionlimit(10 ** 6)


def find_empty_room(room_number, rooms):
    if room_number not in rooms:
        rooms[room_number] = room_number + 1
        return room_number

    empty_room = find_empty_room(rooms[room_number], rooms)
    rooms[room_number] = empty_room + 1
    return empty_room


def solution(k, room_number):
    answer = []
    rooms = {}

    for number in room_number:
        assigned_room = find_empty_room(number, rooms)
        answer.append(assigned_room)

    return answer