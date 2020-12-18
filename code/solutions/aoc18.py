from code.utils import parse_input
import re
input = parse_input(18, '\n', sample=False)


def multiply(n1, n2, op):
    if op == '*':
        return int(n1) * int(n2)
    else:
        import ipdb
        ipdb.set_trace()


def long_comp(line):
    things = line.split(' ')
    res = int(things[0])
    things = things[1:]

    while len(things) > 0:
        op = things.pop(0)
        num = things.pop(0)
        res = multiply(res, num, op)

    return res


def strict_replace(n1, n2, line):
    line = line.split(' ')
    i = 0
    while i <= (len(line) - 3):
        if line[i] == n1 and line[i+1] == '+' and line[i+2] == n2:
            line.pop(i)
            line.pop(i)
            line.pop(i)
            line = line[:i] + [str(int(n1) + int(n2))] + line[i:]
        i += 1

    return ' '.join(line)


def calc_expression(line):
    paren_match = re.search('(\d+ \+ \d+)', line)
    while paren_match:
        match = paren_match.groups()[0]
        [n1, n2] = re.match('(\d+) \+ (\d+)', match).groups()
        line = strict_replace(n1, n2, line)
        paren_match = re.search('(\d+ \+ \d+)', line)

    return long_comp(line)


total = 0
for line in input:
    print(f'line: {line}')
    paren_match = re.search('\(([^\(\)]+)\)', line)
    while paren_match:
        match = paren_match.groups()[0]
        line = line.replace('(' + match + ')', str(calc_expression(match)))
        paren_match = re.search('\(([^\(\)]+)\)', line)

    final = calc_expression(line)
    print(f'final: {final}')
    total += final
    print(f'total: {total}')
    print('-----')

print(f'total is: {total}')


# Instead of all of the above, I should've just done this instead
def better1(line):
    line = line.split(' ')
    i = 0
    while i <= (len(line) - 3):
        n1 = line.pop(i)
        op = line.pop(i)
        n2 = line.pop(i)
        repl = int(n1) * int(n2) if op == '*' else int(n1) + int(n2)
        line = line[:i] + [str(repl)] + line[i:]

    return int(line[0])


def better2(line):
    line = line.split(' ')
    i = 0
    while i <= (len(line) - 3):
        if line[i+1] == '+':
            n1 = line.pop(i)
            line.pop(i)
            n2 = line.pop(i)
            repl = int(n1) + int(n2)
            line = line[:i] + [str(repl)] + line[i:]
        else:
            i += 1

    j = 0
    while j <= (len(line) - 3):
        m1 = line.pop(j)
        line.pop(j)
        m2 = line.pop(j)
        repl = int(m1) * int(m2)
        line = line[:j] + [str(repl)] + line[j:]

    return int(line[0])
