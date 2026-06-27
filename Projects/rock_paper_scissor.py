##########   Welcome To Rock Paper Scissor Game   ##########

import random


print("Welcome to Rock Paper Scissor Game!")

print("===================================")



choices = ["rock", "paper", "scissors"]


user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): \n"))


if user_choice < 1 or user_choice > 3:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose: {choices[user_choice]}")


computer_choice = random.randint(1, 3)


print(f"You chose: {choices[user_choice - 1]}")


print(f"Computer chose: {choices[computer_choice - 1]}")


if user_choice == computer_choice:
    print("It's a tie!")

    
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
        (user_choice == 3 and computer_choice == 2):
    print("You win!")
    
else:
    print("Computer wins!")
    
    
    
print("Thanks for playing Rock Paper Scissor Game!")

print("Have a great day!")