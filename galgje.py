import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def printHangman(wrongGuesses):
    file = open("galgje"+ str(wrongGuesses) + ".txt" , "r")
    print(''.join(file.readlines()))


def reset():
    global guessWordsList
    global word
    global guessedList
    guessedList =  []
    global guessWordsList
    global guessWordList
    guessWordsList = open("galgjeWoordenlijst.txt", "r").readlines()
    guessWordList = list(random.choice(guessWordsList))
    global wrongGuesses
    wrongGuesses = 0
    global lost
    lost = 0


def introduction():
    clearConsole()
    global name
    print("Welcome to hangman!\n")
    name = input("Whats your name? ")
    clearConsole()
    print("Why hello "+ name + "\n\nThere are only three rules: \nYou can only guess a-z. So only letters in the alphabet, no weird characters or numbers, you can only guess wrong 8 times and guessing QQ wil exit the game.\n")
    played=("true")
    print("The word you're gonna guess is "+ str(len(guessWordList)) + " letters long")
    hangman()


def hangman():
    global lost
    global wrongGuesses
    global name
    global guessWord
    print("Start guessing "+name+"!\n\n")
    done = False
    while done == False and wrongGuesses < 7 :
        guessedLetter = input("Enter your guess: ")
        clearConsole()
        if guessedLetter == "QQ":
            quit()
        if len(guessedLetter)==1 and guessedLetter.isalpha()==True:
            if guessedLetter in guessedList:
                print("You already guessed this letter.")
            elif guessedLetter not in guessedList and guessedLetter  not in guessWordList:
                wrongGuesses += 1
                guessedList.append(guessedLetter)
                print(guessedLetter + " is wrong, you need to guess the rest of: ", end ='')
                done = lettersLeftPrinter()
            elif guessedLetter not in guessedList and guessedLetter in guessWordList:
                guessedList.append(guessedLetter)
                print("Thats correct, you need to guess the rest of: ", end ='')
                done = lettersLeftPrinter()
        elif len(guessedLetter)>1 and guessedLetter.isalpha()==True:
            guessedList.append(guessedLetter)
            if guessedLetter == ''.join(guessWordList):
                print("The word was: " + ''.join(guessWordList))
                done = True
            else:
                print("No haste no waste. Just try again untill you get it right..... or when you die.")
                print("You need to guess the rest of: ", end ='')
                done = lettersLeftPrinter()
                wrongGuesses +=1
        else:
            print(guessedLetter+" is not a viable input. It's very simple: you can only use characters that are in the alphabet.")
    if done == True:
        print("Congrats! You won the game.")
    else:
        print("You lost. The word was: " + '_'.join(guessWordList))
    retry()

def lettersLeftPrinter():
    done = handleResult(guessWordList, guessedList)
    if not done:
        printHangman(wrongGuesses)
    return done

def handleResult(guessWord, guessedLettersList):
    guessWordList = list(guessWord)
    done = True
    result = ""
    for letter in guessWordList:
        if letter in guessedLettersList:
            result += letter
        else:
            result += "_"
            done = False
    print(result)
    return done

def retry():
    global name
    again = input("Do you want to go again? y/n:  ")
    if again == "y":
        print("\nYou chose to try again. Good choice if you ask me.")
        sameName = input("Do you want to use the same name as last time?\ny/n:  ")
        if sameName == "y":
            clearConsole()
            print("Okay, lets get started "+name+"!")
        elif sameName == "n":
            name = input("Whats your name? ")
            clearConsole()
        print("The word you're gonna guess is "+ str(len(guessWordList)) + " letters long")
        reset()
        hangman()
    elif again == "n":
        print("Goodbye.")
        reset()


reset()
introduction()
