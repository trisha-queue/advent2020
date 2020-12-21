from code.utils import parse_input
import re
foods = parse_input(21, '\n', sample=False)

all_allergens = {}
all_ingredients = []
set_ingredients = set()

for i in range(len(foods)):
    food = foods[i]
    [ingredients, allergens] = food.split(' (contains ')

    ingredients = ingredients.split(' ')
    all_ingredients.append(ingredients)
    for ing in ingredients:
        set_ingredients.add(ing)

    allergens = allergens[:-1].split(', ')
    for allergen in allergens:
        if allergen not in all_allergens:
            all_allergens[allergen] = []
        all_allergens[allergen].append(i)


def intersect(indices):
    inter = set(all_ingredients[indices[0]])
    for i in indices[1:]:
        inter = inter.intersection(set(all_ingredients[i]))

    return inter

# part one
all_possible = set()
for a, eyes in all_allergens.items():
    poss = intersect(eyes)
    print(f'{a} could be {poss}')
    all_possible.update(poss)


not_possible = set()
for ing in set_ingredients:
    if ing not in all_possible:
        not_possible.add(ing)


count = 0
for food in all_ingredients:
    for whatever in food:
        if whatever in not_possible:
            count += 1

print(count)


# part two, manual
# using the output from L36, I manually sorted, eliminated and then entered the answer!

# part two, coded after the fact!
possible = {}
for a, eyes in all_allergens.items():
    poss = intersect(eyes)
    possible[a] = poss

final = {}

one_possibility_allergens = list(filter(lambda k: len(possible[k]) == 1, possible.keys()))
while one_possibility_allergens:
    ok = one_possibility_allergens.pop(0)
    ans = list(possible.pop(ok))[0]
    final[ok] = ans
    for k in possible.keys():
        if ans in possible[k]:
            possible[k].remove(ans)

    one_possibility_allergens = list(filter(lambda k: len(possible[k]) == 1, possible.keys()))

print(','.join(final[f] for f in sorted(final.keys())))
