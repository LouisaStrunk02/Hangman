from HangmanStages import stages
from Words import word_list
import random

def printHangmanStages(stage):
    print(stages[stage])

def getRandomWord():
    word = random.choice(word_list).upper()

    return word

def getWordIndices(word, guess):
    indices = []

    for index, letter in enumerate(word):

        if letter == guess:
            indices.append(index)
    
    return indices

def fillLettersInWord(word_completion, word, guess):
    word_as_list = list(word_completion)
    indices = getWordIndices(word, guess)

    for index in indices:
        word_as_list[index] = guess

    word_completion = "".join(word_as_list)

    return word_completion

def play(word):
    remaining_tries = 7
    word_was_guessed = False
    hidden_letter = "_"
    word_completion = hidden_letter * len(word)
    listOfLetters = [0] * remaining_tries

    printHangmanStages(6)
    print(word_completion)

    while not word_was_guessed and remaining_tries > 0:
        guess = input("Buchstabe oder Wort eingeben: ").upper()

        if guess not in word:
            if guess in listOfLetters:
                print("Du hast " + guess + " schon einmal eingegeben.")
            else:
                listOfLetters[7 - remaining_tries] = guess
                print(f"Das gesuchte Wort enthält den Buchstaben " + guess + " nicht.")
                remaining_tries -= 1
        else:
            if guess == word:
                print(guess)
                word_was_guessed = True
                break
            else:
                print(f"Das gesuchte Wort enthält den Buchstaben " + guess + ".")
                word_completion = fillLettersInWord(word_completion, word, guess)
                word_was_guessed = hidden_letter not in word_completion

        stage = remaining_tries - 1
        printHangmanStages(stage)
        print(word_completion)

    if word_was_guessed:
        print("Super, du hast das Wort erraten!")
    elif remaining_tries == 0:
        print("Schade. Das gesuchte Wort war: " + word)

word = getRandomWord()
play(word)
