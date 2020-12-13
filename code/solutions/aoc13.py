from code.utils import parse_input

inputs = parse_input(13, '\n', sample=False)

# part one
dt = int(inputs[0])
buses = [int(b) for b in inputs[1].split(',') if b.isnumeric()]
diff = None
cb = None
for bus in buses:
    ct = ((int(dt/bus)+1)*bus)- dt
    if not diff or ct < diff:
        diff = ct
        cb = bus
print(diff*cb)


# part two
buses2 = []
for bus in inputs[1].split(','):
    if bus.isnumeric():
        buses2.append(int(bus))
    else:
        buses2.append(0)

pairs = []  # pairs is a terrible name. This is really something like "buses_with_offsets"
for i in range(len(buses2)):
    pairs.append([buses2[i],i])

pairs = list(reversed(sorted(pairs)))


# this is really something like "calculate_num"
def num_works(num, offset, increment, pairs):
    if pairs[0][0] == 0:
        return num

    next_n = pairs[0][0]
    next_o = pairs[0][1]

    new_num = num

    # lol, aka (new_num - offset + next_o) % next_n != 0
    # but keeping this monstrosity here for posterity
    while int((new_num - offset + next_o) / next_n) != (new_num - offset + next_o) / next_n:
        new_num += increment

    return num_works(new_num, offset, increment * next_n, pairs[1:])

start = 100000000000000
max_num = pairs[0][0]
max_offset = pairs[0][1]

# this is really something like "start"
current = int(start / max_num) * max_num

answer = num_works(current, max_offset, max_num, pairs[1:])
print(answer-max_offset)