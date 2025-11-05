#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
from tkinter import *
import random
import time

def click():
    while True:
#Start Timer
        start = time.perf_counter()

#Welcome Screen
        def level_choose():
            print(" ____________________")
            print("|                    |")                
            print("|  Welcome to 50/50  |")
            print("|   You Must Guess   |")
            print("|  The Right Answer  |")
            print("|   Choose a Level   |")
            print("|____________________|")
            print(" ")

    #Levels
            print("Level 1 = Easy")
            print("Level 2 = Challenging")
            print("Level 3 = Difficult")
            print("Level 4 = Impossible")
            print(" ")

            validIntegerLevel = False

            while validIntegerLevel == False:
                gameLevel = int(input("Level Choice = "))
                if gameLevel.isdigit():
                    if int(gameLevel) < 1 or int(gameLevel) > 4:
                        print("You Need To Enter 1, 2, 3, or 4 for the Level Number")
                        print(" ")
                    else:
                        validIntegerLevel = True
                else:
                    print("You To Enter A Valid Integer")
                    print(" ")
            
            global gameLevelChoice
            gameLevelChoice = int(gameLevel)

            print("You Selected Level - " + str(gameLevelChoice))
        level_choose()

        input("Press Any Key To Continue!")

        def set_level_parameters():
            global upperLimit
            global maxGuesses

            if gameLevelChoice == 1:
                upperLimit = 25
                maxGuesses = 3
            elif gameLevelChoice == 2:
                upperLimit = 50
                maxGuesses = 5

            elif gameLevelChoice == 3:
                upperLimit = 100
                maxGuesses = 10

            elif gameLevelChoice == 4:
                upperLimit = 1000
                maxGuesses = 2

            else:
                print(" ")
                print("You Need To Enter 1, 2, 3, or 4")
                gameLevelChoice = 1
                upperLimit = 10
                maxGuesses = 3
                print("Level Has Been Automically Set to Level 1")
                
            print("Pick A Number Between 0 - " + str(upperLimit))

            print("You Have " + str(maxGuesses) + " Guesses")
        set_level_parameters()

    #Generates Random Number
        def random_number_generator():
            global randomNbr
            randomNbr = random.randint(0, upperLimit)

            print("The Answer Is " + str(randomNbr))
        random_number_generator()

    #User Input / Guess Counter
        def user_guessses_number():
            nbrofGuesses = 0
            count = 1

            if (randomNbr % 2) == 0:
                print("The Number Is Even")
            else:
                print("The Number Is Odd")

            while nbrofGuesses < maxGuesses:
                print(" ")

                get_valid_user_guess()
            
                if int(userguess) < randomNbr:
                    print("Your Guess Was Too Low")
                    nbrofGuesses = nbrofGuesses + 1
                    count += 1

                elif int(userguess) > randomNbr:
                    print("Your Guess Was Too High")
                    nbrofGuesses = nbrofGuesses + 1
                    count += 1

                elif int(userguess) == randomNbr:
                    print(" ")
                    print("Congratulations, You Won The Game!!!\nIt Took You", count, "guessses")
                    nbrofGuesses = nbrofGuesses + 1
                    break

                elif int(userguess) != randomNbr:
                    print("The Right Answer Was " + str(randomNbr) + "!")
                    nbrofGuesses = nbrofGuesses + 1
                    break
            else:
                nbrofGuesses > maxGuesses
                print(" ")
                print("Sorry, You Have Used All of Your Guesses\nThe Right Answer Was " + str(randomNbr) + "!")
        user_guessses_number()

        def get_valid_user_guess():
            global userguess

            validIntegerGuess = False

            while validIntegerGuess == False:
                userguess = input("Enter a Number from 1 to " + str(upperLimit) + " : ")
                if userguess.isdigit():
                    if int(userguess) >= 1 and int(userguess) <= upperLimit:
                        validIntegerGuess = True
                    else:
                        print("You Need to Enter a Number between 1 and " + str(upperLimit))
                        print(" ")
                else:
                    print("You Need To Enter A Valid Integer")
                    print(" ")


    #End Timer
        finish = time.perf_counter()

        print(f'It Took You {round(finish-start, 1)} Second(s) To Finish The Game')
        print(" ")

    #Reset Option
        while True:
            answer = str(input("Would You Like To Play Again? (Y/N): "))
            if answer in ("Y", "N"):
                break
            print("Invalid Input")
        if answer == "Y":
            continue
        else:
            print("Thank You For Playing, GoodBye!")
            break

def load_frame2():
    exit()

#instantiate of a window
window = Tk()
window.geometry("1000x475")
window.title("50/50 The Game - Beta")

icon = PhotoImage(file = "5050.png")
bg = PhotoImage(file = "5050.png")

label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

label2 = Label ( window, text = "Welcome to 50/50",
                bg = "red",
                font =("Comic Sans", 30))
label2.pack(pady = 50)

#Create Frame
frame1 = Frame( window, bg = "red")
frame1.pack(pady = 20)

#Add Buttons
button1 = Button( frame1, text = "Exit",
                    font=("Comic Sans",15),
                    bg = "blue",
                    activeforeground = "black",
                    activebackground = "blue",
                    cursor = "hand2",
                    command = lambda:load_frame2(),
                    state = ACTIVE)
button1.pack(pady = 30)

button2 = Button( frame1,text = "Start",
                    command = click,
                    font = ("Comic Sams", 15),
                    bg = "green",
                    activeforeground = "white",
                    cursor = "hand2",
                    state = ACTIVE)
button2.pack(pady = 30)

button3 = Button( frame1, text = "Reset",
                    font = ("Comic Sans", 15),
                    bg = "Purple",
                    activeforeground = "black",
                    activebackground = "White",
                    cursor = "hand2",
                    state = ACTIVE)
button3.pack(pady = 30)

window.iconphoto(True, icon)
#Place window on screen, listen for events
window.mainloop()