# manually loaded the input into a variable called "map"
seats = """<copy_paste"""
seats = seats.split('\n')

# common functions to the solutions
def getRow(input):
	start = 0
	end = 127
	for i in input:
		middle = (start + end) / 2
		if i == 'F':
			end = middle - .5
		elif i == 'B':
			start = middle + .5
	if end != start:
		print("-------------")
		print(f"{input} gave {start}, {end}")
		print("something went wrong row")
	
	return int(start)


def getSeat(input):
	start = 0
	end = 7
	for i in input:
		middle = (start + end) / 2
		if i == 'L':
			end = middle - .5
		elif i == 'R':
			start = middle + .5
	if end != start:
		print("something went wrong seat")
	
	return int(start)

### part one (copied into ipython)

### part two (copied into ipython)
max_seat_id = 0
allseats = {}
for input in seats:
	row_input = input[:7]
	seat_input = input[7:]

	row = getRow(row_input)
	seat = getSeat(seat_input)
	
	if row not in allseats:
		allseats[row] = []
	
	allseats[row].append(seat)

	seat_id = row*8 + seat
	if seat_id > max_seat_id:
		max_seat_id = seat_id

print(max_seat_id)

for allrow, allseats in allseats.items():
	if len(allseats) != 8:
		print(allrow)
		print(allseats)
# and then I manually verified what the seat was lol


# how I should've done part two
min_seat_id = 996
max_seat_id = 0
actual_sum = 0
for input in seats:
	row_input = input[:7]
	seat_input = input[7:]

	row = getRow(row_input)
	seat = getSeat(seat_input)

	seat_id = row*8 + seat
	actual_sum += seat_id

	if seat_id > max_seat_id:
		max_seat_id = seat_id
	
	if seat_id < min_seat_id:
		min_seat_id = seat_id

expected_sum = (min_seat_id + ((max_seat_id-min_seat_id)/2)) * (len(seats)+1)
print(expected_sum-actual_sum)