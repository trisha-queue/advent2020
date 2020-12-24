from code.utils import parse_input
input = parse_input(24, '\n', sample=False)

final_tiles = {}

valid_directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']
get_offsets = {
    'e': [0, 2],
    'w': [0, -2],
    'se': [-2, 1],
    'nw': [2, -1],
    'sw': [-2, -1],
    'ne': [2, 1]
}

def parse_dirs(line):
    dirs = []

    curr = ''
    for c in line:
        curr += c

        if curr in valid_directions:
            dirs.append(curr)
            curr = ''

    return dirs


def get_pos(dirs):
    aisle = 0
    x = 0
    for d in dirs:
        ao, xo = get_offsets[d]
        aisle += ao
        x += xo

    return f'{int(aisle)},{int(x)}'


for line in input:
    dirs = parse_dirs(line)
    tile_key = get_pos(dirs)

    if tile_key not in final_tiles:
        final_tiles[tile_key] = 0

    final_tiles[tile_key] += 1


def count_black(tile_set):
    final_black = 0
    for turn_count in tile_set.values():
        if turn_count % 2 == 1:
            final_black += 1

    return final_black


print(count_black(final_tiles))
print('end')



# part two
curr_tiles = final_tiles
days = 100


def get_boundaries(tile_set):
    aisles = set()
    xs = set()

    for key in tile_set.keys():
        a, x = key.split(',')
        aisles.add(int(a))
        xs.add(int(x))

    return [min(aisles), max(aisles), min(xs), max(xs)]


for day in range(1, days+1):
    new_tiles = {}
    [min_aisle, max_aisle, min_x, max_x] = get_boundaries(curr_tiles)
    for a in range(min_aisle-2, max_aisle+3):
        for x in range(min_x-2, max_x+3):
            black_neighbors = 0
            for ao, xo in get_offsets.values():
                key = f'{a+ao},{x+xo}'
                neighbor_val = curr_tiles.get(key)
                if neighbor_val and neighbor_val % 2 == 1:
                    black_neighbors += 1

            tile_key = f'{a},{x}'
            tile_val = curr_tiles.get(tile_key) or 0

            if tile_val % 2 == 1 and (black_neighbors == 0 or black_neighbors > 2):
                new_tiles[tile_key] = 0
            elif tile_val % 2 == 0 and black_neighbors == 2:
                new_tiles[tile_key] = 1
            else:
                new_tiles[tile_key] = tile_val

    curr_tiles = new_tiles
    if day % 10 == 0:
        print(f'Day {day}: {count_black(curr_tiles)}')


print(count_black(curr_tiles))