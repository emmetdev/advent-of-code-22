day1_file = open("input.txt", "r")
elves = day1_file.read().split("\n\n")

highest_calorie = 0
for elf_data in elves:
    this_elf_calorie_count = sum([int(x) for x in elf_data.split("\n") if x])
    highest_calorie = this_elf_calorie_count if this_elf_calorie_count > highest_calorie else highest_calorie
print(highest_calorie)
day1_file.close()
