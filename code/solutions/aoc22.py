from code.utils import parse_input
import re
players = parse_input(22, '\n\n', sample=False)

def get_cards(player_input):
    cards = player_input.split('\n')[1:]
    cards = [int(c) for c in cards]
    return cards

player_cards = [get_cards(i) for i in players]

# part one
while len(player_cards[0]) > 0 and len(player_cards[1]) > 0:
    p1 = player_cards[0].pop(0)
    p2 = player_cards[1].pop(0)

    if p1 > p2:
        player_cards[0].append(p1)
        player_cards[0].append(p2)
    elif p2 > p1:
        player_cards[1].append(p2)
        player_cards[1].append(p1)
    else:
        import ipdb
        ipdb.set_trace()

winning_deck = player_cards[0] + player_cards[1]

total = 0
for i in range(1, len(winning_deck)+1):
    total += i * winning_deck[-i]

print(total)


# part two
def get_key(p1_cards, p2_cards):
    return ','.join([str(i) for i in p1_cards])+'|'+','.join([str(j) for j in p2_cards])


def game(p1_cards, p2_cards, level=0):
    cache = set()

    while len(p1_cards) > 0 and len(p2_cards) > 0:
        cache_key = get_key(p1_cards, p2_cards)
        if cache_key in cache:
            winner = 0
            p1 = p1_cards.pop(0)
            p2 = p2_cards.pop(0)
        else:
            cache.add(cache_key)
            p1 = p1_cards.pop(0)
            p2 = p2_cards.pop(0)

            if p1 <= len(p1_cards) and p2 <= len(p2_cards):
                # print(f'{"".join(["." for i in range(level)])} -- {p1}({len(p1_cards)}) vs {p2}({len(p2_cards)})')
                winner, _ = game(p1_cards[:p1], p2_cards[:p2], level=level+1)
            elif p1 > p2:
                winner = 0
            else:
                winner = 1

        if winner == 0:
            p1_cards.append(p1)
            p1_cards.append(p2)
        else:
            p2_cards.append(p2)
            p2_cards.append(p1)

    if len(p1_cards) == 0:
        return 1, p2_cards
    else:
        return 0, p1_cards


_, winning_deck = game(player_cards[0], player_cards[1], level=0)


total = 0
for i in range(1, len(winning_deck)+1):
    total += i * winning_deck[-i]

print(total)