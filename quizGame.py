guesses = []
correctGuesses = 0
questionNumber = 1
guessNumber = 1

def newGame():
    
    global questionNumber

    print("(-----------------------------------------------------------------------)")
    print("Welcome to the game! Please choose the correct answer for each question")

    for key in questions:
        print(key)
        for i in options[questionNumber - 1]:
            print(i)
        questionNumber += 1
        a = input("Choose your answer A/B: " )
        guesses.append(a)

    print(guesses)


def checkAnswer():

    global correctGuesses
    
    global guessNumber
       
    for value in questions.values():
        if value == guesses[guessNumber - 1]:
            correctGuesses += 1
        guessNumber += 1
        
    return correctGuesses


def checkScore():

    totalQuestions = len(questions)

    finalScore = correctGuesses/totalQuestions*100
    print(str(finalScore) + " / 100")


def playAgain():
    b = input("Do you wanna play again?" )
    if b == "Yes":
        return True
    else:
        return False




questions = {

    "Who is Jorge?: ": "A",

    "How old is Jorge?: ": "B",

    "Who's Jorge's Dog?: ": "A",

    "How old is Jorge's Dog?: ": "B"

}

options = [
    ["A. A dude", "B. A girl"],
    ["A. 21", "B. 22"],
    ["A. Guara", "B. Ara"],
    ["A. 9", "B. 8"]

]

newGame()
checkAnswer()
checkScore()

while playAgain():
    newGame()
    checkAnswer()
    checkScore()

#Habría que arreglar las variables de los índices