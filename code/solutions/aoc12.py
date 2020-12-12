from code.utils import parse_input

inputs = parse_input(12, '\n', sample=False)
inputs = [[d[0],int(d[1:])] for d in inputs]


def get_increments(instruction, amount, direction):
    turns = ['N', 'E', 'S', 'W']

    if instruction == 'N':
        return [-amount, 0, direction]
    if instruction == 'W':
        return [0, -amount, direction]
    if instruction == 'E':
        return [0, amount, direction]
    if instruction == 'S':
        return [amount, 0, direction]
    if instruction == 'L':
        return [0, 0, turns[(turns.index(direction) - int(amount/90)) % len(turns)]]
    if instruction == 'R':
        return [0, 0, turns[(turns.index(direction) + int(amount/90)) % len(turns)]]
    if instruction == 'F':
        return get_increments(direction, amount, direction)


wa = -1
wr = 10
sa = 0
sr = 0
facing = 'E'

for [ii, ia] in inputs:
    [oa, orow, od] = get_increments(ii, ia, facing)
    if ii in ('N','W','E','S'):
        wa += oa
        wr += orow
    elif ii == 'R':
        facing = od
        amount = int(ia/90) % 4
        for thing in range(amount):
            new_wa = wr
            new_wr = -1 * wa
            wa = new_wa
            wr = new_wr
    elif ii == 'L':
        facing = od
        amount = int(ia/90) % 4
        for thing in range(amount):
            new_wa = wr * -1
            new_wr = wa
            wa = new_wa
            wr = new_wr
    elif ii == 'F':
        sa += ia * wa
        sr += ia * wr

print(abs(sa) + abs(sr))