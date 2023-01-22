instructions = []

with open("input.txt") as program:
    for line in program:
        instructions.append(line.rstrip())

X = 1
cycles = [[1, 1]]
# cycle = [X value during cycle, X value after cycle]

for i in instructions:
    X_during = X
    X_after = X
    cycles.append([X_during, X_after])

    if i[:4] == "addx":
        X_after = X + int(i[5:])
        cycles.append([X_during, X_after])
        X = X_after

sum_of_strenghts = 0

for ix, cycle in enumerate(cycles):
    if ix == 20 or (ix - 20) % 40 == 0:
        sum_of_strenghts += cycle[0] * ix

print("Sum of signal strenghts:", sum_of_strenghts)