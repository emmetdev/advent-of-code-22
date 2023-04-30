day1_file = open("input.txt", "r")
elves = day1_file.read().split("\n\n")

calorie_totals = []
for elf_data in elves:
    calorie_totals.append(sum([int(x) for x in elf_data.split("\n") if x]))
print(sum(sorted(calorie_totals)[-3:]))
day1_file.close()
