crates_input = open("input.txt")

crates, moves = [], []

for line in crates_input:
    if len(line) == 1:
        break
    else:
        crates.append(line)
    
for line in crates_input:
    if len(line) == 1:
        continue
    else:
        moves.append(line)

n_stacks = crates[len(crates)-1]
stacks_dict = {}

for char in n_stacks:
    if char.isnumeric():
        stacks_dict.update({int(char): []})

for n in stacks_dict.keys():
    for line in crates:
        if line[(n-1)*4] == "[":
            stacks_dict[n].append(line[(n-1)*4+1])
    stacks_dict[n].reverse()

def move_items(move=list, stacks=dict):
    stack = int(move[3])
    new_stack = int(move[5])

    for i in range(int(move[1])):
        item = stacks[stack].pop(-1)
        stacks[new_stack].append(item)

    return stacks

for ix, line in enumerate(moves):
    move = moves[ix].strip("\n").split(" ")
    stacks_dict = move_items(move, stacks_dict)

top_items = str("")

for stack in stacks_dict.values():
    top_items += stack[-1]

print("Items on top of the stacks: ", top_items)