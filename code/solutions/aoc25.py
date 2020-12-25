from code.utils import parse_input
input = parse_input(25, '\n', sample=False)
card_public = int(input[0])
door_public = int(input[1])


subject = 7
door_loop = card_loop = None
cache = {}

curr = 1
cache[0] = 1
i = 1
while not door_loop or not card_loop:
    curr = curr*subject % 20201227
    cache[i] = curr
    if curr == door_public:
        door_loop = i

    if curr == card_public:
        card_loop = i

    i += 1
    if door_loop and card_loop:
        break

print(cache[door_loop])
print(cache[card_loop])

sub2 = cache[door_loop]
curr2 = 1
for i in range(card_loop):
    curr2 = curr2*sub2 % 20201227

print(curr2)

sub3 = cache[card_loop]
curr3 = 1
for i in range(door_loop):
    curr3 = curr3*sub3 % 20201227

print(curr3)