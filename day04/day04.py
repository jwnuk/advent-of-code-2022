sections = open("input.txt")

pairs = []

for line in sections:
    pairs.append(line[0:len(line)-1].split(","))

repeating_assignments = []
overlapping_assignments = []

for pair in pairs:
    pair[0] = pair[0].split("-")
    pair[1] = pair[1].split("-")
    
    min1 = int(pair[0][0])
    min2 = int(pair[1][0])
    max1 = int(pair[0][1])
    max2 = int(pair[1][1])

    if (min1 <= min2) and (max1 >= max2):
        repeating_assignments.append(pair)
    elif (min2 <= min1) and (max2 >= max1):
        repeating_assignments.append(pair)

    if (min1 >= min2) and (min1 <= max2):
        overlapping_assignments.append(pair)
    elif (min2 >= min1) and (min2 <= max1):
        overlapping_assignments.append(pair)

print("Number of assignments that fully contains the other from pair: ", len(repeating_assignments))
print("Number of overlapping pairs of assignments: ", len(overlapping_assignments))