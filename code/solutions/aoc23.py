from code.utils import parse_input
import re
cup_nums = parse_input(23, '\n', sample=False)[0]
cup_nums = [int(c) for c in cup_nums]

# part one solution
# moves = 100
# num_followers = 3
#
# current_value = cup_nums[0]
#
# def find_index(val):
#     try:
#         return cup_nums.index(val)
#     except:
#         return None
#
#
# for m in range(moves):
#     followers = []
#     for f in range(num_followers):
#         followers.append(cup_nums.pop( (find_index(current_value)+1) % len(cup_nums)))
#
#     dest_val = current_value - 1
#     dest_i = find_index(dest_val)
#     end = False
#     while not end and dest_i is None:
#         dest_val -= 1
#         dest_i = find_index(dest_val)
#         if dest_val <= 0:
#             dest_val = max(cup_nums)
#             dest_i = find_index(dest_val)
#             end = True
#
#     insert_index = (dest_i + 1) % len(cup_nums)
#     while followers:
#         cup_nums.insert(insert_index, followers.pop(-1))
#
#     current_value = cup_nums[ (find_index(current_value)+1) % len(cup_nums)]
#
# print(cup_nums)
# index1 = find_index(1)
#
# final_order = cup_nums[(index1+1 % len(cup_nums)):] + cup_nums[:index1]
# ans = ''.join([str(n) for n in final_order])
# print(ans)

# WOW SO DUMB
def print_all(start_num):
    print_queue = [start_num]
    print_val = cache[start_num].next_val

    while print_val != start_num:
        print_queue.append(print_val)
        print_val = cache[print_val].next_val

    print(','.join([str(n) for n in print_queue]))


class LinkedListNode:
    def __init__(self, val, next_val=None, prev_val=None):
        self.val = val
        self.next_val = next_val
        self.prev_val = prev_val

cache = {}
head_val = prev_val = None
for n in cup_nums + list(range(10, 1000001)):
    cache[n] = LinkedListNode(val=n, prev_val=prev_val)
    if not head_val:
        head_val = n
    if prev_val:
        cache[prev_val].next_val = n
    prev_val = n

cache[prev_val].next_val = head_val
cache[head_val].prev_val = prev_val


moves = 10000000
num_followers = 3

curr_val = head_val


def get_dest(curr_val):
    dest_val = curr_val - 1
    if dest_val == 0:
        dest_val = len(cache)

    f1_val = cache[curr_val].next_val
    f2_val = cache[f1_val].next_val
    f3_val = cache[f2_val].next_val

    while dest_val in (f1_val, f2_val, f3_val):
        dest_val = dest_val - 1
        if dest_val == 0:
            dest_val = len(cache)

    return dest_val


def move_followers(curr_val, dest_val):
    f1_val = cache[curr_val].next_val
    f2_val = cache[f1_val].next_val
    f3_val = cache[f2_val].next_val
    new_curr_next_val = cache[f3_val].next_val

    # "pop"
    cache[curr_val].next_val = new_curr_next_val
    cache[new_curr_next_val].prev_val = curr_val

    # "insert"
    old_dest_next_val = cache[dest_val].next_val
    cache[dest_val].next_val = f1_val
    cache[f1_val].prev_val = dest_val

    cache[f3_val].next_val = old_dest_next_val
    cache[old_dest_next_val].prev_val = f3_val


for m in range(moves):
    dest_val = get_dest(curr_val)
    move_followers(curr_val, dest_val)
    curr_val = cache[curr_val].next_val


# part one
# print_all(1)

# part two
first = cache[1].next_val
second = cache[first].next_val
print(f'{first} * {second} = {first*second}')