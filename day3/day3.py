import string

rucksacks = open("input.txt")

rucksack_1 = []
rucksack_2 = []

for r in rucksacks:
    
    half = int((len(r)-1)/2)
    length = int(len(r)-1)

    rucksack_1.append(r[0:half])
    rucksack_2.append(r[half:length])

letters_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letters_dict = {}

for ix, letter in enumerate(letters_list):
    letters_dict[letter] = ix+1

def get_distinct_letters(items_list):
    letters_list = []

    for item in items_list:
        letters = set()

        for letter in item:
            letters.add(letter)

        letters_list.append(list(letters))
    
    return letters_list

r1_letters = get_distinct_letters(rucksack_1)
r2_letters = get_distinct_letters(rucksack_2)

priorities_sum = 0

for ix, item in enumerate(r1_letters):
    
    for letter in item:
        if r2_letters[ix].count(letter) == 0:
            continue
        else:
            priority = letters_dict.get(letter)
            priorities_sum += priority
            break

print("Total priorities: ", priorities_sum)

# part two

elves = open("input.txt")
elves_list = []

for i in elves:
    elves_list.append(i)

elves_1, elves_2, elves_3 = [], [], []

for ix, item in enumerate(elves_list):
    if (ix + 1) % 3 == 1:
        elves_1.append(item[0:len(item)-1])
    elif (ix + 1) % 3 == 2:
        elves_2.append(item[0:len(item)-1])
    else:
        elves_3.append(item[0:len(item)-1])

e1_letters = get_distinct_letters(elves_1)
e2_letters = get_distinct_letters(elves_2)
e3_letters = get_distinct_letters(elves_3)

priorities_sum_2 = 0

for ix, item in enumerate(e1_letters):

    for letter in item:
        if e2_letters[ix].count(letter) == 0:
            continue
        elif e3_letters[ix].count(letter) == 0:
            continue
        else:
            priority = letters_dict.get(letter)
            priorities_sum_2 += priority
            break

print("Total priorities_2: ", priorities_sum_2)