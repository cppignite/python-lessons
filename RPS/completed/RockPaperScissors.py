import sys
import os

user1_score = 0
user2_score = 0

turn_num = 0


def compare(u1, u2):
    if u1 == u2:
        return("It's a tie! The scores weren't changed.")
    elif u1 == 'rock':
        if u2 == 'scissors':
            user1_score += 1
            return("Rock wins this round!")
        else:
            user2_score += 1
            return("Paper wins this round!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            user1_score += 1
            return("Scissors win this round!")
        else:
            user2_score += 1
            return("Rock wins this round!")
    elif u1 == 'paper':
        if u2 == 'rock':
            user1_score += 1
            return("Paper wins this round!")
        else:
            user2_score += 1
            return("Scissors win this round!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

for turn in range(1,4):
    os.system('clear')
    user1_answer = input("Player 1, do you want to choose rock, paper or scissors?")
    os.system('clear')
    user2_answer = input("Player 2, do you want to choose rock, paper or scissors?")
    print(compare(user1_answer, user2_answer))

if user1_score > user2_score:
    print ("Congratulations Player 1, you won this game!")
elif user2_score > user1_score:
    print ("Congratulations Player 2, you won this game!")
else:
    print ("Wow you two tied this game!")