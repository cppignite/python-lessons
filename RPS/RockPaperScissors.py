import sys

user1 = raw_input("What's your name?")
user2 = raw_input("And your name?")


user1_score = 0
user2_score = 0

turn_num = 0

def compare(u1, u2):
    global user1_score
    global user2_score

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
    user1_answer = raw_input("%s, do yo want to choose rock, paper or scissors?" % user1)
    user2_answer = raw_input("%s, do you want to choose rock, paper or scissors?" % user2)

    print(compare(user1_answer, user2_answer))

if user1_score > user2_score:
    print ("Congratulations %s, you won this game!" % user1)
    print ("The scores were: %s: %s and %s: %s ." % (user1, user1_score, user2, user2_score))
elif user2_score > user1_score:
    print ("Congratulations %s, you won this game!" % user2)
    print ("The scores were: %s: %s and %s: %s ." % (user1, user1_score, user2, user2_score))
else:
    print ("Wow you two tied this game!")
    print ("The scores were: %s: %s and %s: %s ." % (user1, user1_score, user2, user2_score))