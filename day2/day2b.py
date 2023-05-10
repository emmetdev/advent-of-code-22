from operator import itemgetter

score = {'R': {'A': 4, 'B': 1, 'C': 7},
         'P': {'A': 8, 'B': 5, 'C': 2},
         'S': {'A': 3, 'B': 9, 'C': 6}}

day2_file = open("input.txt", "r")
rounds = day2_file.read().split("\n")

total_score = 0
for game in rounds[:-1]:
    possible_outcomes = []
    possible_outcomes.append(['R', score['R'][game[0]]])
    possible_outcomes.append(['P', score['P'][game[0]]])
    possible_outcomes.append(['S', score['S'][game[0]]])
    possible_outcomes = sorted(possible_outcomes, key=itemgetter(1))

    if game[2] == "X":
        total_score = total_score + possible_outcomes[0][1]
    elif game[2] == "Y":
        total_score = total_score + possible_outcomes[1][1]
    elif game[2] == "Z":
        total_score = total_score + possible_outcomes[2][1]

print(total_score)
