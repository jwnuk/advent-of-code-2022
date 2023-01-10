trees_input = open("input.txt")

trees_map = []

for line in trees_input:
    trees_map.append(line.strip("\n"))

n_rows = len(trees_map)
n_cols = len(trees_map[0])
visible_trees = 0
tree_height = 0
scores = []

for nr in range(n_rows):

    # print(trees_map[nr])

    for nc in range(n_cols):
        if (nr == 0) or (nr == n_rows-1):
            visible_trees += 1
        elif ((nc == 0) or (nc == n_cols-1)) and (nr != 0) and (nr != n_rows-1):
            visible_trees += 1
        else:
            tree_height = int(trees_map[nr][nc])
            visible_left, visible_right, visible_top, visible_bottom = 0, 0, 0, 0

            d_left, d_right, d_top, d_bottom = 0, 0, 0, 0
            max_left, max_top = 0, 0

            for left in range(nc):
                tree_left = int(trees_map[nr][left])

                if tree_left >= tree_height:
                    visible_left = 0
                    break
                else:
                    visible_left = 1
# pt 2
            for left in range(nc):
                tree_left = int(trees_map[nr][left])

                if tree_left >= tree_height:
                    max_left = tree_left
                    d_left = nc - left
                
                else:
                    if left == 0:
                        max_left = tree_left
                        d_left = nc - left

            for right in range(nc+1, n_cols):
                tree_right = int(trees_map[nr][right])
                if visible_left == 1:
                    break
                elif tree_right >= tree_height:
                    visible_right = 0
                    break
                else:
                    visible_right = 1
# pt 2
            for right in range(nc+1, n_cols):
                tree_right = int(trees_map[nr][right])

                if tree_right >= tree_height:
                    d_right = right - nc
                    break
                else:
                    d_right = right - nc

            for top in range(nr):
                tree_top = int(trees_map[top][nc])
                if (visible_left == 1) or (visible_right == 1):
                    break
                elif tree_top >= tree_height:
                    visible_top = 0
                    break
                else:
                    visible_top = 1
# pt 2
            for top in range(nr):
                tree_top = int(trees_map[top][nc])

                if tree_top >= tree_height:
                    max_top = tree_top
                    d_top = nr - top

                else:
                    if top == 0:
                        max_top = tree_top
                        d_top = nr - top

            for bottom in range(nr+1, n_rows):
                tree_bottom = int(trees_map[bottom][nc])
                if (visible_left == 1) or (visible_right == 1) or (visible_top == 1):
                    break
                elif tree_bottom >= tree_height:
                    visible_bottom = 0
                    break
                else:
                    visible_bottom = 1
# pt 2
            for bottom in range(nr+1, n_rows):
                tree_bottom = int(trees_map[bottom][nc])

                if tree_bottom >= tree_height:
                    d_bottom = bottom - nr
                    break
                else:
                    d_bottom = bottom - nr

            visible = max(visible_left, visible_right, visible_top, visible_bottom)
            visible_trees += visible
            scores.append(d_left * d_right * d_top * d_bottom)
            # print("tree = ", tree_height)
            # print("left, right, top, bottom = ", d_left, d_right, d_top, d_bottom)
            # print("Product: ", d_left * d_right * d_top * d_bottom)

print("Number of visible trees: ", visible_trees)
print("Highest scenic score: ", max(scores))