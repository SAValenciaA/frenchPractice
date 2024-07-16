import os
from translations import translationsList, printScore, evaluateUser
from random import shuffle, sample
from datetime import datetime as dt

# Directory of this file
PWD = os.path.dirname(os.path.realpath(__file__))

GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[33m"
WHITE = "\033[0m"

def recordScore(score, correctResponses, total, lvl):

    file = open(f'{PWD}/data/{score}', "a")

    date = dt.today().strftime("%Y-%m-%d %H:%M:%S")
    qualification = int((correctResponses/total) * 100)

    file.write(f'{qualification}% | {lvl} | {date}\n')

def practice(lvl, mode):
    
    # Get translation list of the level
    translations = translationsList(lvl)
    # Shuffle it
    shuffle(translations)

    correctResponses = 0

    width = 0

    # For each translation
    # Test the user accordingly to the mode of practice
    # if the answer is correct, sum one to the counter
    for translation in translations:
        # Get width of the terminal
        width = os.get_terminal_size()[0]
        correctResponses += evaluateUser(translation, mode, width)

    # Open past scores record
    if mode == "TRANSLATE TO ENGLISH":
        scores = "scores_translate_from"
    elif mode == "TRANSLATE TO FRENCH":
        scores = "scores_translate_to"

    # Save practice
    recordScore(scores, correctResponses, len(translations), lvl)

    # Print past records
    printScore(str(lvl),scores,width)


