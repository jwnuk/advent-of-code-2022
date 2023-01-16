sequence = open("input.txt")

moves = []

for move in sequence:
    moves.append(move.strip("\n").split(" "))

start_point = "X1000Y1000"
tail_positions = [start_point]
H_position, T_position = [1000, 1000], [1000, 1000]

def update_position(position=list, direction=str):
    if direction == "R":
        position[0] += 1
    elif direction == "L":
        position[0] -= 1
    elif direction == "U":
        position[1] += 1
    elif direction == "D":
        position[1] -= 1

    return position

def check_T_H_dist(H_position=list, T_position=list):
    x_dist = H_position[0] - T_position[0]
    y_dist = H_position[1] - T_position[1]

    return [x_dist, y_dist]

def new_T_position(position=list):
    new_position = "X" + str(position[0]) + "Y" + str(position[1])

    return new_position

for move in moves:
    steps = int(move[1])

    for n in range(steps):
        # update head position
        H_position = update_position(H_position, move[0])
        # check distance between H and T and update T position if necessary
        distances = check_T_H_dist(H_position, T_position)
       
        if abs(distances[0]) > 1:
            T_position = update_position(T_position, move[0])

            if distances[1] > 0:
                T_position = update_position(T_position, "U")
            elif distances[1] < 0:
                T_position = update_position(T_position, "D")

            tail_positions.append(new_T_position(T_position))

        elif abs(distances[1]) > 1:
            T_position = update_position(T_position, move[0])

            if distances[0] > 0:
                T_position = update_position(T_position, "R")
            elif distances[0] < 0:
                T_position = update_position(T_position, "L")
            
            tail_positions.append(new_T_position(T_position))

print("Positions visited by tail at least once:", len(set(tail_positions)))
