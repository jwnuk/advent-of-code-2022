cmd = open("input.txt")

cmd_list = []

for line in cmd:
    cmd_list.append(line.strip("\n"))

slash = {}
current_dir = slash

for line in cmd_list:
    
    if line[0:4] == "$ cd":
        if line[5:7] == "..":
            current_dir = current_dir["parent"]
        else:
            if line[5] == "/":
               current_dir = slash
            else:
                current_dir = current_dir[line[5:]]
            
    if line[0:4] == "$ ls":
        pass
    if line[0:3] == "dir":
        dir_name = line[4:]
        new_dir = {
            "parent": current_dir
        }
        current_dir[dir_name] = new_dir
    if line[0].isnumeric():
        file = line.split(" ")
        current_dir[file[1]] = int(file[0])

def get_sizes(sizes_dict=dict, directory=dict, path=""):
    
    size = 0

    for key, value in directory.items():
        if key == "parent":
            continue
        elif type(value) == int:
            size += value
        else:
            size += get_sizes(sizes_dict, value, path + "/" + key)
    
    sizes_dict[path] = size
    
    return size

sizes_dict = {}
slash_size = get_sizes(sizes_dict, slash)

total_sizes = 0

for size in sizes_dict.values():
    if size <= 100000:
        total_sizes += size

print("Total sizes: ", total_sizes)