# manually loaded the input into a variable called "groups"
input = """<copy_paste"""
groups = input.split('\n\n')

### part one (copied into ipython)
total = 0
for group in groups:
    letter_set = set()        
    for letter in group:
        if letter.isalpha():
            letter_set.add(letter)
    print(f"len is {len(letter_set)} for {letter_set}")
    total += len(letter_set)                           
print(total) 

### part two (copied into ipython)
total = 0
for group in groups:
    people = group.split('\n')
    sets = []
    for person in people:
        person_set = set()
        for letter in person:
            person_set.add(letter)
        sets.append(person_set)
    total_union = sets[0]
    for union_add in sets[1:]:
        total_union = total_union.union(union_add)
    total += len(total_union)
print(total)