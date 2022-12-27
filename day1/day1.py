input = open("input.txt")

max_e = 0
elf = 0

for i in input:
    if len(i) > 1:
        elf += int(i)
    else:
        if elf > max_e:
            max_e = elf
        elf = 0

print(max_e)