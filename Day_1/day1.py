def _get_highest(list_of_int: list):
    list_of_int.sort(reverse=True)
    return list_of_int[0]
def _get_3_highest(list_of_int: list):
    list_of_int.sort(reverse=True)
    return list_of_int[0]+list_of_int[1]+list_of_int[2]

f = open('AdventCode_2022\Day_1\day1-input.txt', "r")

elves_calories = []

calories = 0
for line in f.readlines():
    try:
        calories += int(line)
    except:
        elves_calories.append(calories)
        calories = 0

print(f"Highest elve calories {_get_highest(elves_calories)}")

print(f"3 highest elves calories {_get_3_highest(elves_calories)}")
