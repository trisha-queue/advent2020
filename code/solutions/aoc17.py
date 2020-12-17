from code.utils import parse_input
import re
input = parse_input(17, '\n', sample=False)


XYZW_OFFSETS = []
for ix in (0, -1, 1):
    for iy in (0, -1, 1):
        for iz in (0, -1, 1):
            for iw in (0, -1, 1):
                XYZW_OFFSETS.append([ix, iy, iz, iw])
XYZW_OFFSETS.remove([0,0,0,0])
print(f'num_neighbors is {len(XYZW_OFFSETS)}')


def is_active(x, y, z, w, state):
    if (x not in state or
            y not in state[x] or
            z not in state[x][y] or
            w not in state[x][y][z]):
        return False

    return state[x][y][z][w] == '#'


def calc_new_state(x, y, z, w, state):
    active_neighbors = 0
    for xo, yo, zo, wo in XYZW_OFFSETS:
        if is_active(x+xo, y+yo, z+zo, w+wo, state):
            active_neighbors += 1

    if is_active(x, y, z, w, state):
        if active_neighbors in [2,3]:
            return '#'
        else:
            return '.'
    else:
        if active_neighbors == 3:
            return '#'
        else:
            return '.'


def calc_new_round(state):
    new_state = {}
    for x in state.keys():
        new_state[x] = {}
        for y in state[x].keys():
            new_state[x][y] = {}
            for z in state[x][y].keys():
                new_state[x][y][z] = {}
                for w in state[x][y][z].keys():
                    new_state[x][y][z][w] = calc_new_state(x, y, z, w, state)

                    for xo, yo, zo, wo in XYZW_OFFSETS:
                        if x+xo not in new_state:
                            new_state[x+xo] = {}
                        if y+yo not in new_state[x+xo]:
                            new_state[x+xo][y+yo] = {}
                        if z+zo not in new_state[x+xo][y+yo]:
                            new_state[x + xo][y + yo][z+zo] = {}

                        if w+wo in new_state[x+xo][y+yo][z+zo]:
                            continue
                        wtf = calc_new_state(x+xo, y+yo, z+zo, w+wo, state)
                        new_state[x + xo][y + yo][z + zo][w+wo] = wtf

    return new_state


current_state = {}
for y in range(len(input)):
    aisle = input[y]
    for x in range(len(aisle)):
        if x not in current_state:
            current_state[x] = {}
        if y not in current_state[x]:
            current_state[x][y] = {}
        current_state[x][y][0] = {}
        current_state[x][y][0][0] = input[y][x]

rounds = 6
for r in range(rounds):
    next_state = calc_new_round(current_state)
    current_state = next_state

final_active = 0
for x in current_state.keys():
    for y in current_state[x].keys():
        for z in current_state[x][y].keys():
            for w, fv in current_state[x][y][z].items():
                if fv == '#':
                    final_active += 1

print(final_active)
