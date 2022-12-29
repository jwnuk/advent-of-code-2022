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
