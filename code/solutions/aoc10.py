from code.utils import parse_input

nums = parse_input(10, '\n', sample=False)
nums = [int(num) for num in nums]
# ## part one
nums = sorted(nums)
nums.append(nums[-1]+3)
nums = [0] + nums
print(nums)
print('----')

diffs = {}
prev = 0

for i in range(1, len(nums)):
    diff = nums[i] - nums[prev]
    if diff not in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] += 1
    prev = i

print(diffs)


# part two
cached = {}


def num_ways(num_array):
    if len(num_array) == 1:
        return 1

    ways = 0
    for index in [1, 2, 3]:
        if len(num_array) >= (index + 1):
            if num_array[index] - num_array[0] <= 3:
                if num_array[index] in cached:
                    ways += cached[num_array[index]]
                else:
                    ans = num_ways(num_array[index:])
                    ways += ans
                    cached[num_array[index]] = ans
    return ways

print(num_ways(nums))