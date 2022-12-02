ROCK = 1
PAPER = 2
SCISSOR = 3
WIN = 6
DRAW = 3
LOSE = 0

def _get_score_by_result_chall1(a:str, b:str):
    my_score = 0
    elve_score = 0
    if ("A" in a):
        elve_score += ROCK
        if "X" in b:
            my_score += ROCK
            elve_score += DRAW
            my_score += DRAW
        elif "Y" in b:
            my_score += PAPER
            elve_score += LOSE
            my_score += WIN
        elif "Z" in b:
            my_score += SCISSOR
            elve_score += WIN
            my_score += LOSE
    elif ("B" in a):
        elve_score += PAPER
        if "X" in b:
            my_score += ROCK
            elve_score += WIN
            my_score += LOSE
        elif "Y" in b:
            my_score += PAPER
            elve_score += DRAW
            my_score += DRAW
        elif "Z" in b:
            my_score += SCISSOR
            elve_score += LOSE
            my_score += WIN
    elif ("C" in a):
        elve_score += SCISSOR
        if "X" in b:
            my_score += ROCK
            elve_score += LOSE
            my_score += WIN
        elif "Y" in b:
            my_score += PAPER
            elve_score += WIN
            my_score += LOSE
        elif "Z" in b:
            my_score += SCISSOR
            elve_score += DRAW
            my_score += DRAW
    list_score = [elve_score,my_score]
    return list_score

def _get_score_by_result_chall2(a:str, b:str):

    my_score = 0
    elve_score = 0
    #I need to lose
    if "X" in b:
        my_score += LOSE
        elve_score += WIN
        # Elve Rock - me scissor
        if ("A" in a):
            elve_score += ROCK
            my_score += SCISSOR
        # Elve Paper - me Rock
        elif ("B" in a):
            elve_score += PAPER
            my_score += ROCK
        # Elve scissor - me paper
        elif ("C" in a):
            elve_score += SCISSOR
            my_score += PAPER
    #I need to draw
    elif "Y" in b:
        my_score += DRAW
        elve_score += DRAW
        # Elve Rock - me ROCK
        if ("A" in a):
            elve_score += ROCK
            my_score += ROCK
        # Elve Paper - me PAPER
        elif ("B" in a):
            elve_score += PAPER
            my_score += PAPER
        # Elve scissor - me SCISSOR
        elif ("C" in a):
            elve_score += SCISSOR
            my_score += SCISSOR
    #I need to win
    elif "Z" in b:
        my_score += WIN
        elve_score += LOSE
        # Elve Rock - me Paper
        if ("A" in a):
            elve_score += ROCK
            my_score += PAPER
        # Elve Paper - me scissor
        elif ("B" in a):
            elve_score += PAPER
            my_score += SCISSOR
        # Elve scissor - me Rock
        elif ("C" in a):
            elve_score += SCISSOR
            my_score += ROCK
    list_score = [elve_score,my_score]
    return list_score


f = open('AdventCode_2022\Day_2\day2-input.txt', "r")
my_score_chall1 = 0
my_score_chall2 = 0
elve_score_chall1 = 0
elve_score_chall2 = 0
for line in f.readlines():
    coups = line.split(" ")
    print(coups)
    coups_score  = _get_score_by_result_chall1(coups[0], coups[1])
    elve_score_chall1 += coups_score[0]
    my_score_chall1 += coups_score[1]
    coups_score  = _get_score_by_result_chall2(coups[0], coups[1])
    elve_score_chall2 += coups_score[0]
    my_score_chall2 += coups_score[1]

print(f"my score with chall1 will be : {my_score_chall1}")
print(f"elve score with chall1 will be : {elve_score_chall1}")
print("-----------------------------------------")
print(f"my score with chall1 will be : {my_score_chall2}")
print(f"elve score with chall1 will be : {elve_score_chall2}")