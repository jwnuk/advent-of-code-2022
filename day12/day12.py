import string
import sys

heights = []
alphabet = list(string.ascii_lowercase)
alphabet_dict = {}

for ix, letter in enumerate(alphabet):
    alphabet_dict[letter] = ix

alphabet_dict["S"] = 0
alphabet_dict["E"] = 25

with open("input.txt") as input:
    for line in input:
        heights.append(list(line.strip()))

start, end = [], []

for ix, line in enumerate(heights):
    for jx, height in enumerate(line):
        if height == "S":
            start.append([ix, jx])
        elif height == "E":
            end = [ix, jx]
        heights[ix][jx] = alphabet_dict[height]


def get_neighbours(point=list, heights=list):
    neighbours = []
    i, j = point[0], point[1]
    current_h = heights[i][j]
    if j+1 < len(heights[i]):
        neighbour_h = heights[i][j+1]
        if current_h - neighbour_h <= 1:
            neighbours.append([i, j+1])

    if j-1 >= 0:
        neighbour_h = heights[i][j-1]
        if current_h - neighbour_h <= 1:
            neighbours.append([i, j-1])

    if i+1 < len(heights):
        neighbour_h = heights[i+1][j]
        if current_h - neighbour_h <= 1:
            neighbours.append([i+1, j])

    if i-1 >= 0:
        neighbour_h = heights[i-1][j]
        if current_h - neighbour_h <= 1:
            neighbours.append([i-1, j])

    return neighbours

def move(heights):
    positions_to_check = [(end, 0, [end])]
    visited = {str(positions_to_check[0][0]) + ";" + str(positions_to_check[0][1]): 0}
    best = 9999

    while len(positions_to_check) > 0:
        current_coordinates, dist, path = positions_to_check.pop()
        
        if current_coordinates in start and best > dist:
            best = dist
            continue
            
        neighbours = get_neighbours(current_coordinates, heights)

        for n in neighbours:
            key = str(n[0]) + ";" + str(n[1])
            if key in visited.keys():
                if visited[key] <= dist:
                    continue

            visited[key] = dist
            new_path = []
            new_path.extend(path)
            new_path.append(n)
            positions_to_check.append((n, dist+1, new_path))

    return best

shortest_path = move(heights)
print("Path complete, total steps, part 1:", shortest_path)

# part 2

for ix, line in enumerate(heights):
    for jx, height in enumerate(line):
        if height == 0:
            start.append([ix, jx])

shortest_path = move(heights)
print("Path complete, total steps, part 2:", shortest_path)