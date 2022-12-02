def _get_highest(list_of_int: list):
    list_of_int.sort(reverse=True)
    return list_of_int[0]
def _get_3_highest(list_of_int: list):
    list_of_int.sort(reverse=True)
    return list_of_int[0]+list_of_int[1]+list_of_int[2]

f = open('C:/Users/localhost/OneDrive/Documents/Project/Adventcode/day1-input.txt', "r")

elves_calories = []

calories = 0
for line in f.readlines():
    try:
        calories += int(line)
    except:
        elves_calories.append(calories)
        calories = 0

print(elves_calories)

print(_get_3_highest(elves_calories))
