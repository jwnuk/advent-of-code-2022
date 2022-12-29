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

r1_letters = []
r2_letters = []

for item in rucksack_1:
    letters = set()

    for letter in item:
        letters.add(letter)
    
    r1_letters.append(list(letters))

for item in rucksack_2:
    letters = set()

    for letter in item:
        letters.add(letter)
    
    r2_letters.append(list(letters))

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