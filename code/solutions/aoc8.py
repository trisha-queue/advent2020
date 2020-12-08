from code.utils import parse_input
import re

instructions = parse_input(8, '\n')

### part one
total = 0
visited = set()
i = 0

while i >= 0 and i < len(instructions):
    if i in visited:
        print(total)
        raise Exception('the end')
    else:
        visited.add(i)

    if instructions[i].startswith('nop'):
        i += 1
    elif instructions[i].startswith('acc'):
        operator = instructions[i].split(' ')[1][0]
        num = int(instructions[i].split(' ')[1][1:])
        if operator == '+':
            total += num
        elif operator == '-':
            total -= num
        i += 1
    elif instructions[i].startswith('jmp'):
        # lol copypasta
        operator = instructions[i].split(' ')[1][0]
        num = int(instructions[i].split(' ')[1][1:])
        if operator == '+':
            i += num
        elif operator == '-':
            i -= num


### part two
for j in range(len(instructions)):
    if not (instructions[j].startswith('nop') or instructions[j].startswith('jmp')):
        continue

    if instructions[j].startswith('nop'):
        new_instruction = 'jmp'
    else:
        new_instruction = 'nop'
    rest_of_instruction = instructions[j].split(' ')[1]

    new_instructions = instructions[:j] + [f'{new_instruction} {rest_of_instruction}'] + instructions[j+1:]

    # oh hey this looks familiar
    i = 0
    visited = set()
    total = 0
    while i >= 0 and i < len(new_instructions):
        if i in visited:
            break
        else:
            visited.add(i)

        if new_instructions[i].startswith('nop'):
            i += 1
        elif new_instructions[i].startswith('acc'):
            operator = new_instructions[i].split(' ')[1][0]
            num = int(new_instructions[i].split(' ')[1][1:])
            if operator == '+':
                total += num
            elif operator == '-':
                total -= num
            i += 1
        elif new_instructions[i].startswith('jmp'):
            operator = new_instructions[i].split(' ')[1][0]
            num = int(new_instructions[i].split(' ')[1][1:])
            if operator == '+':
                i += num
            elif operator == '-':
                i -= num

    if i == len(new_instructions):
        print(total)
        raise Exception('the end')