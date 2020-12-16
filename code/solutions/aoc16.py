from code.utils import parse_input
import re
input = parse_input(16, '\n\n', sample=False)
rules = input[0]
mine = input[1]
nearby = input[2]

# part one
def parse_rules(input):
    input = input.split('\n')
    rules = {}
    for rule in input:
        [name, ranges] = rule.split(': ')
        [r1, r2] = ranges.split(' or ')
        r1 = [int(n) for n in r1.split('-')]
        r2 = [int(n) for n in r2.split('-')]
        rules[name] = [r1, r2]

    return rules


def parse_nearby(input):
    input = input.split('\n')
    input = input[1:]

    tickets = []
    for line in input:
        tickets.append([int(n) for n in line.split(',')])

    return tickets


def is_invalid(n, rules):
    for rule in rules.values():
        [r1, r2] = rule
        if (r1[0] <= n <= r1[1]) or (r2[0] <= n <= r2[1]):
            return False

    return True


def return_invalid_sum(rules, tickets):
    sum = 0
    for ticket in tickets:
        for num in ticket:
            if is_invalid(num, rules):
                sum += num

    return sum

r = parse_rules(rules)
near = parse_nearby(nearby)

# print(return_invalid_sum(r, near))



# part two
def get_field_possibilities(n, rules):
    posses = []
    for name, rule in rules.items():
        [r1, r2] = rule
        if (r1[0] <= n <= r1[1]) or (r2[0] <= n <= r2[1]):
            posses.append(name)

    return posses


def get_ticket_possibilities(ticket, rules):
    for num in ticket:
        if is_invalid(num, rules):
            return None

    fields = {}
    for i in range(len(ticket)):
        names = get_field_possibilities(ticket[i], rules)
        for name in names:
            if name not in fields:
                fields[name] = [i]
            else:
                fields[name].append(i)

    return fields


def determine_fields(rules, tickets):
    ticket_posses = {rn: {} for rn in rules.keys()}
    valid_tickets = 0

    for ticket_id in range(len(tickets)):
        p = get_ticket_possibilities(tickets[ticket_id], rules)
        if not p:
            continue

        valid_tickets += 1
        for field_name, poss_field_ids in p.items():
            for pfi in poss_field_ids:
                if pfi not in ticket_posses[field_name]:
                    ticket_posses[field_name][pfi] = []
                ticket_posses[field_name][pfi].append(ticket_id)

    all_could_bes = []
    for name, data in ticket_posses.items():
        could_be = []
        for i, pi in data.items():
            if len(pi) == valid_tickets:
                could_be.append(i)
        # for the problem, I just printed the following and did the rest manually
        # print(f"{name} could be {could_be}")

        # everything below this line is added after the fact, for fun
        all_could_bes.append([name, could_be])

    all_could_bes = sorted(all_could_bes, key=lambda x: len(x[1]))
    for i in range(len(all_could_bes)):
        final_pos = all_could_bes[i][1][0]

        for rest in range(i+1, len(all_could_bes)):
            print(f"popping {final_pos} from {all_could_bes[rest][1]}")
            all_could_bes[rest][1].remove(final_pos)

    return all_could_bes


positions = determine_fields(r, near)

mine = mine.split('\n')[1]
mine = mine.split(',')
mine = [int(m) for m in mine]

product = 1
for field_name, final_position in positions:
    final_position = final_position[0]
    if field_name.startswith('departure'):
        product *= mine[final_position]

print(product)