import string

alphabet_low_up = (list(string.ascii_lowercase) + list(string.ascii_uppercase))
priorities = (range(1, 53))
priority_ref = {alphabet_low_up[i]: priorities[i] for i in range(len(alphabet_low_up))}

day3_file = open("input.txt", "r")
rucksacks = day3_file.read().split("\n")
priority_count = 0

for rucksack in rucksacks:
    matching_char = ''.join(set(rucksack[:len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:]))
    priority_count+=priority_ref[matching_char]

print(priority_count)
