monkeys = []

with open("input.txt") as notes:
    for line in notes:
        if line.startswith("Monkey"):
            monkey = {"Monkey": int(line[7])}
        elif line.lstrip().startswith("Starting items"):
            items = line.strip("\n")[line.find(":")+2:].split(", ")
            for ix, i in enumerate(items):
                items[ix] = int(i)
            monkey["Items"] = items
        elif line.lstrip().startswith("Operation"):
            monkey["Operation"] = line.strip("\n")[line.find("d")+2:].split()
        elif line.lstrip().startswith("Test"):
            monkey["Test"] = line.strip("\n")[8:].split()
        elif line.lstrip().startswith("If true"):
            monkey["T"] = int(line.strip("\n")[-1])
        elif line.lstrip().startswith("If false"):
            monkey["F"] = int(line.strip("\n")[-1])
            monkey["Inspected"] = 0
            monkeys.append(monkey)

for round in range(20):
    for m in monkeys:
        items = m["Items"]
        for i in range(len(items)):
            item = items[0]
            increase = m["Operation"][1]
            if increase == "old":
                increase = item
            else:
                increase = int(increase)
            if m["Operation"][0] == "+":
                item += increase
            elif m["Operation"][0] == "*":
                item *= increase
            item //= 3
            if item % int(m["Test"][-1]) == 0:
                new_owner = m["T"]
            else:
                new_owner = m["F"]
            items.pop(0)
            monkeys[new_owner]["Items"].append(item)
            m["Inspected"] += 1

inspected_items = []

for monkey in monkeys:
    inspected_items.append(monkey["Inspected"])

inspected_items.sort()
print("Monkey business: ", inspected_items[-1] * inspected_items[-2])
