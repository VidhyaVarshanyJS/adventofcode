# --- Day 3: Rucksack Reorganization ---

lines = ''.join(list(open("day3.txt")))
rucks = lines.split('\n')

# Puzzle 1
comp1 = list()
comp2 = list()

common_item = list()
common_item2 = list()

for item in rucks:
    c1 = item[:len(item)//2]
    comp1.append(c1)
    c2 = item[len(item)//2:]
    comp2.append(c2)

# finding out the common letters
for item1, item2 in zip(comp1, comp2):
    common = set(item1) & set(item2)
    for i in common:
        common_item.append(i)


def priorvalue(alphas):
    priority = list()
    for letter in alphas:
        if letter.islower():
            value = ord(letter) - ord('A') - 31
            priority.append(value)
        else:
            value = ord(letter) - ord('a') + 59
            priority.append(value)
    return sum(priority)


print("Puzzle 1", priorvalue(common_item))


# Puzzle 2

groups = [rucks[i:i+3] for i in range(0, len(rucks), 3)]
for sublist in groups:
    common = set(sublist[0]) & set(sublist[1]) & set(sublist[2])
    for i in common:
        common_item2.append(i)

print("Puzzle 2", priorvalue(common_item2))
