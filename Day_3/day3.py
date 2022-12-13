
f = open('AdventCode_2022\Day_3\day3-input.txt', "r")
### part 1 of the chall
total = 0
for line in f.readlines():
    if len(line) != 0:
        part1 = line[0:int((len(line)-1)/2)]
        part2 = line[int((len(line)-1)/2):len(line)]
        for char in part1:
            if char in part2:
                print(f"We detected this char : {char} in both part: {part1} & {part2}")
                char_value = ord(char)-38 if ord(char)<91 else ord(char)-96
                print(f"this char : {char} has the code {char_value}")
                total += char_value
                break
print(f"Total value for part 1 of chal is : {total}")
line1 = ""
line2 = ""
total2 = 0
f = open('AdventCode_2022\Day_3\day3-input.txt', "r")
## Part 2 of the chall
for line in f.readlines():
    if len(line1) == 0  and len(line) != 0 :
        line1 = line
    elif len(line1) != 0 and len(line2) == 0 and len(line) != 0 :
        line2 = line
    else: 
        for char in line: 
            if char in line1 and char in line2:
                print(f"We detected this char : {char} in three line : {line1} & {line2} & {line}")
                char_value = ord(char)-38 if ord(char)<91 else ord(char)-96
                print(f"this char : {char} has the code {char_value}")
                total2 += char_value
                break
        line1 = ""
        line2 = ""
print(f"Total value for part 2 of chal is : {total2}")