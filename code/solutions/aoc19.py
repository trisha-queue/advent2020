from code.utils import parse_input
import re
input = parse_input(19, '\n\n', sample=False)
rules = input[0].split('\n')
lines = input[1].split('\n')

meta_rules = {}
straight_rules = {}
cache = {}

def parse_rules(rules):
    for rule in rules:
        index, logic = rule.split(': ')
        if "\"" in logic:
            straight_rules[index] = logic[1]
        else:
            options = logic.split(" | ")
            for op in options:
                op = op.split(" ")
                if index not in meta_rules:
                    meta_rules[index] = []
                meta_rules[index].append(op)


def add_to_cache(rule_num, matched):
    if rule_num not in cache:
        cache[rule_num] = {matched}
    else:
        cache[rule_num].add(matched)


def match_return_remainder(line, rule_num, verbose=False):
    if rule_num in cache:
        for mop in cache[rule_num]:
            if line.startswith(mop):
                return True, mop, line[len(mop):]

    if line == '':
        return True, '', line

    if rule_num in meta_rules:
        for option in meta_rules[rule_num]:
            option_copy = line
            matched = ''
            for part in option:
                is_match, submatch, remainder = match_return_remainder(
                    option_copy, part, verbose=verbose)
                if not is_match:
                    break
                else:
                    matched += submatch
                    option_copy = remainder

            if is_match:
                add_to_cache(rule_num, matched)
                return True, matched, remainder
        return False, '', line
    elif rule_num in straight_rules:
        if line[0] == straight_rules[rule_num]:
            add_to_cache(rule_num, line[0])
            return True, line[0], line[1:]
        else:
            return False, '', line


# part one
parse_rules(rules)
match0 = 0
for line in lines:

    is_match, matched, remainder = match_return_remainder(line, '0')
    if is_match and remainder == '':
        match0 += 1

print(match0)


# part two
match1 = 0
for line in lines:
    remaining = line
    keep_going = True
    num42s = 0
    while remaining and keep_going:
        start_len = len(remaining)
        for mop in cache['42']:
            if remaining.startswith(mop):
                num42s += 1
                remaining = remaining[len(mop):]
        if len(remaining) == start_len:
            keep_going = False

    keep_going = True
    num31s = 0
    while remaining and keep_going:
        start_len = len(remaining)
        for mop in cache['31']:
            if remaining.startswith(mop):
                num31s += 1
                remaining = remaining[len(mop):]
        if len(remaining) == start_len:
            keep_going = False

    if not remaining and num42s >= 1 and num31s >= 1 and num42s - num31s >= 1:
        match1 += 1

print(match1)
