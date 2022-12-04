lines = ''.join(list(open("day1.txt")))
pairs = lines.split('\n\n')

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
elf = list()
for pair in pairs:
    data = pair.split('\n')
    elf.append(data)

elf = [[int(i) for i in lst]for lst in elf]  # Parent list

# Making the sum in the list of list and finding out the maximum calories

cal_list = [sum(lst) for lst in elf]

# find the maximum of the calories in the list
print("1. The Maximum of the calories list", max(cal_list))

# - Puzzle one completed

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?


# Note: To find the top three element try to use the sorting technique
top_three_sum = sorted(cal_list, reverse=True)[:3]
print("2. The total calories carried by the Elves are ", sum(top_three_sum))
