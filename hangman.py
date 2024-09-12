#Hangman Game
import random
import words
import stages
chosen=random.choice(words.wordsList)
guess=['-']*len(chosen)

print("Let's Play Hangman!!")

print("You have only 6 lives so try to guess the word within 6 attempts! Good luck!!")

print(" ".join(guess))

missmatch=0

while missmatch<6 and guess.count('-')!=0:
    guessed_letter=input("Guess a letter: ")
    if(guessed_letter not in chosen):
        print(f"{guessed_letter} is not in the Word")
        missmatch+=1
    else:
        for i in range(len(chosen)):
            if(chosen[i]==guessed_letter):
                guess[i]=guessed_letter
    print("Current Status of Word: "+" ".join(guess))
    print(stages.hangman_stages[missmatch])

if('-' in guess):
    print("Your Lifes Over!")
    print("You Lost!")
    print(f"The Word is: {chosen}")
else:
    print("You Won!!")