guide = open("input.txt")

"""
1, A, X == rock
2, B, Y == paper
3, C, Z == scissors

win     lose
A < Y   A > Z
B < Z   B > X
C < X   C > Y

0 if you lost
3 if the round was a draw
6 if you won
"""

wins = 0
ties = 0
loses = 0

rocks = 0
papers = 0
scissors = 0

for i in guide:
    if i[2] == "X":
        rocks += 1
    elif i[2] == "Y":
        papers += 2
    elif i[2] == "Z":
        scissors += 3

    if (i[0:3] == "A Y") or (i[0:3] == "B Z") or (i[0:3] == "C X"):
        wins += 6
    elif (i[0:3] == "A X") or (i[0:3] == "B Y") or (i[0:3] == "C Z"):
        ties += 3
    else:
        loses -= 6

print("score = ", rocks + papers + scissors + wins + ties)


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
"""
1, A == rock
2, B == paper
3, C == scissors

X == lose
Y == draw
Z == win

rock    paper   scissors
A Y     A Z     A X
B X     B Y     B Z
C Z     C X     C Y
"""

guide_2 = open("input.txt")

wins_2 = 0
ties_2 = 0
loses_2 = 0

rocks_2 = 0
papers_2 = 0
scissors_2 = 0

for j in guide_2:
    if j[2] == "X":
        loses_2 -= 6
    elif j[2] == "Y":
        ties_2 += 3
    elif j[2] == "Z":
        wins_2 += 6

    if (j[0:3] == "A Y") or (j[0:3] == "B X") or (j[0:3] == "C Z"):
        rocks_2 += 1
    elif (j[0:3] == "A Z") or (j[0:3] == "B Y") or (j[0:3] == "C X"):
        papers_2 += 2
    elif (j[0:3] == "A X") or (j[0:3] == "B Z") or (j[0:3] == "C Y"):
        scissors_2 += 3

print("score_2 = ", rocks_2 + papers_2 + scissors_2 + wins_2 + ties_2)