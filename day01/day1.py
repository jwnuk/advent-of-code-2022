input = open("input.txt")

top1 = 0
top2 = 0
top3 = 0
elf = 0

for i in input:
    if len(i) > 1:
        elf += int(i)
    else:
        if elf > top1:
            top3 = top2
            top2 = top1
            top1 = elf
        elif elf > top2:
            top3 = top2
            top2 = elf
        elif elf > top3:
            top3 = elf
        elf = 0

print(top1)
print(top2)
print(top3)
print(top1 + top2 + top3)