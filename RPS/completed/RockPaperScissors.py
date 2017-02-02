user1_answer = input("Player 1, do you want to choose rock, paper or scissors?")
user2_answer = input("Player 2, do you want to choose rock, paper or scissors?")

if user1_answer == user2_answer:
    print("It's a tie! The scores weren't changed.")
elif user1_answer == 'rock':
    if user2_answer == 'scissors':
        print("Player 1 wins this round!")
    else:
        print("Player 2 wins this round!")
elif user1_answer == 'scissors':
    if user2_answer == 'paper':
        print("Player 1 win this round!")
    else:
        print("Player 2 wins this round!")
elif user1_answer == 'paper':
    if user2_answer == 'rock':
        print("Player 1 wins this round!")
    else:
        print("Player 2 win this round!")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")