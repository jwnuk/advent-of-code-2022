trees_input = open("input.txt")

trees_map = []

for line in trees_input:
    trees_map.append(line.strip("\n"))

n_rows = len(trees_map)
n_cols = len(trees_map[0])
visible_trees = 0
tree_height = 0

for nr in range(n_rows):

    # print(trees_map[nr])

    for nc in range(n_cols):
        if (nr == 0) or (nr == n_rows-1):
            visible_trees += 1
        elif ((nc == 0) or (nc == n_cols-1)) and (nr != 0) and (nr != n_rows-1):
            visible_trees += 1
        else:
            tree_height = trees_map[nr][nc]
            visible_left, visible_right, visible_top, visible_bottom = 0, 0, 0, 0

            for tree_left in trees_map[nr][:nc]:
                if tree_left >= tree_height:
                    visible_left = 0
                    break
                else:
                    visible_left = 1

            for tree_right in trees_map[nr][nc+1:]:
                if visible_left == 1:
                    break
                elif tree_right >= tree_height:
                    visible_right = 0
                    break
                else:
                    visible_right = 1

            for top in range(nr):
                if (visible_left == 1) or (visible_right == 1):
                    break
                elif trees_map[top][nc] >= tree_height:
                    visible_top = 0
                    break
                else:
                    visible_top = 1

            for bottom in range(nr+1, n_rows):
                if (visible_left == 1) or (visible_right == 1) or (visible_top == 1):
                    break
                elif trees_map[bottom][nc] >= tree_height:
                    visible_bottom = 0
                    break
                else:
                    visible_bottom = 1
            
            visible = max(visible_left, visible_right, visible_top, visible_bottom)
            visible_trees += visible
            # print("tree = ", tree_height)
            # print("left, right, top, bottom = ", visible_left, visible_right, visible_top, visible_bottom)


print("Number of visible trees: ", visible_trees)