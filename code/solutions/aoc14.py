from code.utils import parse_input
import re
lines = parse_input(14, '\n', sample=False)


def binary_to_int(answer_list):

    return [int(a, 2) for a in answer_list]


def all_permutations(astring):
    if not astring:
        return ['']

    prefix = ''
    suffix = astring

    while len(suffix) > 0 and suffix[0] != 'X':
        prefix += suffix[0]
        suffix = suffix[1:]

    if not suffix:
        fset = set()
        fset.add(prefix)
        return fset

    answers = set()
    suffix_permutations = all_permutations(suffix[1:])
    for perm in suffix_permutations:
        answers.add(prefix + '0' + perm)
        answers.add(prefix + '1' + perm)

    return answers


def transform(value, mask):
    new_value = [c for c in mask]
    for index in range(1,len(new_value)+1):
        if new_value[-index] == '1':
            continue
        elif new_value[-index] == '0':
            if index <= len(value):
                new_value[-index] = f'{value[-index]}'
            else:
                new_value[-index] = '0'
        else:
            new_value[-index] = 'X'

    return binary_to_int(all_permutations(new_value))


def count_xes(mask):
    count = 0
    for c in mask:
        if c == 'X':
            count += 1

    return count

i = 0
memory = {}
while i < len(lines):
    if lines[i].startswith('mask'):
        mask = lines[i].split(' = ')[1]
    i += 1
    while i < len(lines) and lines[i].startswith('mem'):
        pos, val = re.match('mem\[(\d+)\] = (\d+)', lines[i]).groups()
        pos = int(pos)
        val = int(val)
        all_pos = transform('{0:b}'.format(pos), mask)
        num_xes = count_xes(mask)
        print(f"{mask} contains {num_xes} x's and {len(all_pos)} == {pow(2,num_xes)}")
        for ap in all_pos:
            memory[ap] = val
        i += 1


total = 0
for wtf, wtf2 in memory.items():
    total += wtf2

print(total)