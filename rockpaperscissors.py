print ("Welcome to Rock Paper Scissors!")
print ("You will be playing against the computer.")

name= input("What is your name? ")
print ("Hello " + name + "!")
print ("Let's start the game!")
import random
while True:
    print("Please enter 'yes' to play or 'no' to exit.")
    play = input().lower()
    if play == 'yes':
        break
    elif play == 'no':
        print("Goodbye " + name + "!")
        exit()
    else:
        print("Invalid input, please try again.")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Please choose rock, paper, or scissors: ").lower()

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations " + name + ", you win!")
else:
    print("Sorry " + name + ", you lose.")

print("Thank you for playing with me " + name + "!")
exit()
print("Do you want to play again?")
replay=input(" (yes/no)")
if replay == "yes":
    print("Let's play again!")
else:
    print("Goodbye " + name + "!")
    exit()