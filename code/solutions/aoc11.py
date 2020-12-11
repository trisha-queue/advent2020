from code.utils import parse_input

input = parse_input(11, '\n', sample=False)
input = [[char for char in word] for word in input]

# If I had been thinking, I would've passed in the raw increments and decrements,
# and those could have carried forward. Instead I did this
def get_increments(direction):
    if direction == 'NW':
        return [-1, -1]
    if direction == 'N':
        return [-1, 0]
    if direction == 'NE':
        return [-1, 1]

    if direction == 'W':
        return [0, -1]
    if direction == 'E':
        return [0, 1]

    if direction == 'SW':
        return [1, -1]
    if direction == 'S':
        return [1, 0]
    if direction == 'SE':
        return [1, 1]


def empty_neighbor(aisles, aisle, row, direction):
    [ia, ir] = get_increments(direction)

    # count = 0
    keep_going = True
    while keep_going:
        # count += 1
        # that time I had an infinite loop
        # if count > 1000:
        #     import ipdb
        #     ipdb.set_trace()
        if aisle < 0 or aisle >= len(aisles):
            return True

        if row < 0 or row >= len(aisles[0]):
            return True

        if aisles[aisle][row] == 'L':
            return True

        if aisles[aisle][row] == '#':
            return False

        if aisles[aisle][row] == '.':
            aisle = aisle + ia
            row = row + ir

    return False


def valid_seat(aisles, aisle, row):
    if aisles[aisle][row] == '.':
        return False
    return True


def all_around_empty(aisles, aisle, row):
    if not valid_seat(aisles, aisle, row):
        return False

    if (empty_neighbor(aisles, aisle-1, row-1, 'NW') and
            empty_neighbor(aisles, aisle-1, row, 'N') and
            empty_neighbor(aisles, aisle-1, row + 1, 'NE') and
            empty_neighbor(aisles, aisle, row - 1, 'W') and
            empty_neighbor(aisles, aisle, row + 1, 'E') and
            empty_neighbor(aisles, aisle + 1, row - 1, 'SW') and
            empty_neighbor(aisles, aisle + 1, row, 'S') and
            empty_neighbor(aisles, aisle + 1, row + 1, 'SE')):
        return True
    return False


def can_move(aisles, aisle, row):
    if not valid_seat(aisles, aisle, row):
        return False

    count = 0
    if not empty_neighbor(aisles, aisle-1, row-1, 'NW'):
        count += 1
    if not empty_neighbor(aisles, aisle - 1, row, 'N'):
        count += 1
    if not empty_neighbor(aisles, aisle - 1, row + 1, 'NE'):
        count += 1
    if not empty_neighbor(aisles, aisle, row - 1, 'W'):
        count += 1
    if not empty_neighbor(aisles, aisle, row + 1, 'E'):
        count += 1
    if not empty_neighbor(aisles, aisle + 1, row - 1, 'SW'):
        count += 1
    if not empty_neighbor(aisles, aisle + 1, row, 'S'):
        count += 1
    if not empty_neighbor(aisles, aisle + 1, row + 1, 'SE'):
        count += 1

    if count >= 5:
        return True

    return False


def round(aisles):
    new_aisles = []
    # lol how do u deep copy
    for aisle in aisles:
        new_aisles.append(aisle.copy())

    for aisle in range(len(aisles)):
        for row in range(len(aisles[0])):
            if aisles[aisle][row] == 'L' and all_around_empty(aisles, aisle, row):
                new_aisles[aisle][row] = '#'

            if aisles[aisle][row] == '#' and can_move(aisles, aisle, row):
                new_aisles[aisle][row] = 'L'

    if new_aisles != aisles:
        return round(new_aisles)

    occupied_seats = 0
    for final_aisle in new_aisles:
        for final_char in final_aisle:
            if final_char == '#':
                occupied_seats += 1

    return occupied_seats


print(round(input))