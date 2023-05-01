
score = {'X': {'A': 4, 'B': 1, 'C': 7},
         'Y': {'A': 8, 'B': 5, 'C': 2},
         'Z': {'A': 3, 'B': 9, 'C': 6}}

day2_file = open("input.txt", "r")
rounds = day2_file.read().split("\n")

total_score = 0
for game in rounds[:-1]:
    total_score = total_score + score[game[2]][game[0]]
print(total_score)
