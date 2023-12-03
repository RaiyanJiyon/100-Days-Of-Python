# Snake Water Gun

'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.'''


#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D


import random

print("If You choose Snake and Computer Choose Water, Then Snake Win.\n")
print("If You choose Snake and Computer Choose Gun, Then Gun Win.\n")
print("If You choose Water and Computer Choose Snake, Then Snake Win.\n")
print("If You choose Water and Computer Choose Gun, Then Water Win.\n")
print("If You choose Gun and Computer Choose Snake, Then Gun Win.\n")
print("If You choose Gun and Computer Choose Water, Then Water Win.\n")
print("If Both choose same thing, then it will be Draw.\n")
print("Now Lets Starts The Game.\n")

print("Enter SNAKE for 0\nEnter WATER for 1\nEnter GUN for 2 ")

rounds = 5
user_wins = 0
computer_wins = 0

for round in range(rounds):
    print(f"For Round {round + 1}: ")

    attempt = 0
    max_attempt = 3

    while attempt < max_attempt:
        try:
            user_input = int(input("Enter: "))
            if user_input in (0, 1, 2):
                break
            else:
                print("Invalid Input! Enter 0 for SNAKE, 1 for WATER, or 2 for GUN.")

        except ValueError as e:
            print("Wrong Input, Try Again..!")
            attempt += 1

    if attempt == max_attempt:
        print("To Many Wrong Attemps..! Sorry, Game Is Over.")
        break

    
    computer_input = random.randint(0, 3)

    if user_input == computer_input:
        print("Its a Draw.")

    elif user_input == 0 and computer_input == 1 or user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 1:
        print("You Win This Round.")
        user_wins += 1

    else:
        print("Computer Win This Rounds.")
        computer_wins += 1

if user_wins > computer_wins:
    print(f'You Win This Game by {user_wins} - {computer_wins}. Congo...!')

elif user_wins < computer_wins:
    print(f"You Lose This Game by {computer_wins} - {user_wins}. Better Luck Next Time.")
else:
    print(f"Game Draw by {user_wins} - {computer_wins}.")

print("Game Over.")         

