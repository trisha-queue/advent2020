from code.utils import parse_input
import re
nums = parse_input(15, '\n', sample=False)
nums = [int(n) for n in nums[0].split(',')]

max_turn = 2020  # 30000000
last_spoken = {}
spoken_once = set()
spoken_multi = set()
last_num = None


def add_or_remove_from_spoken_once(num):
    if num not in spoken_once and num not in spoken_multi:
        spoken_once.add(num)
    elif num in spoken_once:
        spoken_once.remove(num)
        spoken_multi.add(num)


def add_to_spoken(num, index):
    if num not in last_spoken:
        last_spoken[num] = [index]
    else:
        before = last_spoken[num]
        last_spoken[num] = [before[-1], index]


def get_diff(num):
    if num not in last_spoken:
        return None
    else:
        return last_spoken[num][1] - last_spoken[num][0]


for i in range(1, max_turn + 1):
    if i <= len(nums):
        i_num = nums[i-1]
    elif last_num in spoken_once:
        add_or_remove_from_spoken_once(last_num)
        i_num = 0
    else:
        i_num = get_diff(last_num)

    add_to_spoken(i_num, i)
    add_or_remove_from_spoken_once(i_num)
    last_num = i_num


print(last_num)