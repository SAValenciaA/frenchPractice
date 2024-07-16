import os
from random import shuffle, sample

# This code is just for copying the file into a dictionary

# File structure:
# word1 | translation1,translation2,translation3
# word2 | translation1,translation2,translation3
# ...

# Directory of this file
PWD = os.path.dirname(os.path.realpath(__file__))

GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[33m"
WHITE = "\033[0m"

fileLines = open(f'{PWD}/data/words').read().split("\n")

translations = [i.split(" | ") for i in fileLines]
translationsLevel = lambda lvl: translations[lvl*50:lvl*50 + 50]

translationsList = lambda lvl: [
    {
        "word": line[0].lower(),
        "answers": set(line[1].lower().split(","))
    } 
    for line in translationsLevel(lvl)
]

def printScore(lvl, score, width):
    os.system("clear")
    print(WHITE + "_"*width)
    file = open(f'{PWD}/data/{score}')
    lines = file.read().split("\n")
    top = 0
    maxTop = 10
    for line in reversed(lines):
        if lvl in line.split(" | "):
            print(line)
            top += 1
        if top == maxTop:
            break
    print(WHITE + "_"*width)

def evaluateUser(translation, mode, width):

    answers = translation["answers"]
    word = translation["word"]

    # Separator
    print(WHITE + ("_"*width))

    if mode == "TRANSLATE TO ENGLISH":

        print(f'Your clue is: {word}')
        isCorrectResponse = lambda response: response in answers
        validResponses = ", ".join(answers)
        printCorrection = lambda: print(f'It could have been: {validResponses}')
        
    elif mode == "TRANSLATE TO FRENCH":

        clue = list(answers)[0] if len(answers) == 1 else ", ".join(sample(list(answers),2))
        print(f'Your clue is: {clue}')
        isCorrectResponse = lambda response: response == word
        printCorrection = lambda: print(f'It should have been: {word}')

    response = input("Answer: ")

    if isCorrectResponse(response):
        print(GREEN + "Correct!")
        printCorrection()
        return 1
    else:
        print(RED + "False!")
        printCorrection()
        return 0

