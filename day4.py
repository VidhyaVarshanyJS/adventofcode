pairs = [line.strip() for line in open("day4.txt")]

fully_contained_pairs = 0
not_fully_contained_pairs = 0

for pair in pairs:
    pair_of_elves = pair.split(',', 2)
    
    elf1 = pair_of_elves[0].split('-')
    elf2 = pair_of_elves[1].split('-')

    nelf1 = list(range(int(elf1[0]), int(elf1[1])+1))
    nelf2 = list(range(int(elf2[0]), int(elf2[1])+1))

    if all(elem in nelf1 for elem in nelf2) or all(elem in nelf2 for elem in nelf1):
        
        fully_contained_pairs += 1

    if any(elem in nelf1 for elem in nelf2) or any(elem in nelf2 for elem in nelf1):

        not_fully_contained_pairs += 1


print("Puzzle 1", fully_contained_pairs)

print("Puzzle 2", not_fully_contained_pairs)
