import random

def name_to_number(name):
    if name== "rock":
        number=0
    elif name== "Spock" or "spock":
        number=1
    elif name== "paper":
        number=2
    elif name== "lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        number="Name does not match options"
    return number

def number_to_name(number):
    if number==0:
        name="rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        name="number does not match options"
    return name

def rpsls(player_choice):
    print('\nPlayer chooses',player_choice)
    player_number=int(name_to_number(player_choice))
    computer_number=random.randrange(0,5)
    print('Computer chooses',number_to_name(computer_number))
    compute=(player_number-computer_number)%5
    if compute==1 or compute== 2:
        print("Player wins!")
    elif compute== 3 or compute== 4:
        print('Computer wins!')
    elif compute== 0:
        print('Player and computer tie!')
    else:
        print('error!')

rpsls(input("Enter your choice:"))
