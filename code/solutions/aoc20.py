from code.utils import parse_input
import re
input = parse_input(20, '\n\n', sample=False)

tile_to_edges = {}
matches = {}

def get_tile_num(tile):
    tile_lines = tile.split('\n')
    return tile_lines[0].split(' ')[1]


def parse_edges(tile):
    num = get_tile_num(tile)
    tile_lines = tile.split('\n')

    tile_to_edges[num] = {}
    tile_to_edges[num]['top'] = [c for c in tile_lines[1]]
    tile_to_edges[num]['bottom'] = [c for c in tile_lines[-1]]
    tile_to_edges[num]['left'] = [l[0] for l in tile_lines[1:]]
    tile_to_edges[num]['right'] = [l[-1] for l in tile_lines[1:]]

    tile_to_edges[f'r{num}'] = {}
    tile_to_edges[f'r{num}']['top'] = list(reversed(tile_to_edges[num]['top']))
    tile_to_edges[f'r{num}']['bottom'] = list(reversed(tile_to_edges[num]['bottom']))
    tile_to_edges[f'r{num}']['left'] = list(reversed(tile_to_edges[num]['right']))
    tile_to_edges[f'r{num}']['right'] = list(reversed(tile_to_edges[num]['left']))


def match_edges(tile, ot):
    for pos, edge in tile_to_edges[tile].items():
        for pos2, edge2 in tile_to_edges[ot].items():
            if edge == edge2:
                if tile not in matches:
                    matches[tile] = set()
                if ot not in matches:
                    matches[ot] = set()
                matches[tile].add(f'{pos+tile} -> {pos2+ot}')
                matches[ot].add(f'{pos2+ot} -> {pos+tile}')

for tile in input:
    parse_edges(tile)

for tile in tile_to_edges.keys():
    for ot in tile_to_edges.keys():
        if ot == tile or ot == 'r' + tile or tile == 'r' + ot:
            continue
        match_edges(tile, ot)


print([f'{key}: {km}' for key, km in sorted(matches.items(), key=lambda i: len(i[1])) if not key.startswith('r')])