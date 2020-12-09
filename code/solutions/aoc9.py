from code.utils import parse_input

nums = parse_input(9, '\n', sample=False)
nums = [int(num) for num in nums]
print('----')
# ## part one
n = 25

possible_sums = {}
for i in range(len(nums)-(n)-1):
    j = i + 1
    while j < (i + n):
        sum = nums[i] + nums[j]
        if sum not in possible_sums:
            possible_sums[sum] = [[i, j]]
        else:
            possible_sums[sum].append([i, j])
        j += 1

print(possible_sums)

for x in range(n, len(nums)):
    if nums[x] not in possible_sums:
        raise Exception(nums[x])

    possible = False
    for [start, end] in possible_sums[nums[x]]:
        if start >= (x - n) and start < x and end >= (x - n) and end < x:
            possible = True

    if not possible:
        import ipdb
        ipdb.set_trace()
        raise Exception(nums[x])

# part two
total = 400480901
start = end = curr_total = 0
start_over = False

while end < len(nums):
    if curr_total < total:
        curr_total += nums[end]
        end += 1
    elif curr_total == total:
        sequence = nums[start:end]
        print(min(sequence))
        print(max(sequence))
        print(min(sequence) + max(sequence))
        raise Exception('the end')
    else:
        while curr_total > total or not start_over:
            curr_total -= nums[start]
            start += 1
            if start == end:
                start_over = True