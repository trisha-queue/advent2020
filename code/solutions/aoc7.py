from code.utils import parse_input
import re

bags = parse_input(7, '\n')

### part one
bag_map = {}
bag_count_map = {}
for bag in bags:
    [bag_type, raw_sub] = re.match('(.*)bags contain (.*).', bag).groups()
    bag_type = bag_type.strip()
    raw_sub = raw_sub.split(', ')
    sub_bags = []

    set_sub_bags = set()
    for raw in raw_sub:
        if raw == 'no other bags':
            sub_bags.append([0, None])
        else:
            validated = re.match('(\d+) (.*) bags?', raw).groups()
            sub_bags.append(list(validated))
            set_sub_bags.add(validated[1])

    bag_map[bag_type] = list(set_sub_bags)
    bag_count_map[bag_type] = sub_bags


def contains_gold(bag):
    if bag not in bag_map:
        return False
    if 'shiny gold' in bag_map[bag]:
        return True
    else:
        for sub_bag in bag_map[bag]:
            if contains_gold(sub_bag):
                return True

    return False

count = 0
for bag_type in bag_map.keys():
    if contains_gold(bag_type):
        count += 1

print(count)


### part two
def return_sub_count(bag):
    sub_bag_counts = bag_count_map[bag]
    if len(sub_bag_counts) == 0:
        return 0

    sum = 0
    for [bag_count, sub_bag_type] in sub_bag_counts:
        if not sub_bag_type:
            continue
        bag_count = int(bag_count)
        sub_bag_bag_count = return_sub_count(sub_bag_type)
        sum += bag_count * (1 + sub_bag_bag_count)

    return sum

print(return_sub_count('shiny gold'))