# --- Day 2: Rock Paper Scissors ---
# Opponent Elf
# A Y -
# B X -
# C Z -

# X = 1
# Y = 2
# Z = 3

# make the input as a list first , split each pair (for example[A Y,] if Y add score + A Y combo  outcome come 6 else 3
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# win case

# C X   --> +6
# B Z
# A Y
# if not the above combo it is lose case --> 0

# tie case
# A X
# B Y --> 3
# C Z
#Score + Outcome ( )
lines = ''.join(list(open("day2.txt")))
game = lines.split('\n')
score = {'X': 1, 'Y': 2, 'Z': 3}
# outcome = {tuple(['C X', 'B Z', 'A Y']): 6, tuple(['A X', 'B Y', 'C Z']):  3}
outcome = {'C X': 6, 'B Z': 6, 'A Y': 6, 'A X': 3,
           'B Y': 3, 'C Z': 3, 'C Y': 0, 'A Z': 0, 'B X': 0}

game1 = list()

final_score = list()


for i in game:
    for key, value in score.items():
        if key in i:
            # newElement = i.replace(key, value)
            game1.append(value)
# print(game1)

game2 = list()
for i in game:
    for key, value in outcome.items():
        if key in i:
            game2.append(value)
# print(game2)

final_score = game1 + game2
print(sum(final_score))
# for ele in game:

#     # Increase the value of key
#     # if exists
#     if ele in outcome:
#         continue
#     else:

#         # Insert the new key:value
#         # pair
#         outcome[ele] = 0

# print(outcome)

# Puzzle 2
score2 = {'X': 0, 'Y': 3, 'Z': 6}

strategy = list()
for i in game:
    for key, value in score2.items():
        if key in i:
            strategy.append(value+1)

print(strategy)

f = strategy 
print(sum(f))
