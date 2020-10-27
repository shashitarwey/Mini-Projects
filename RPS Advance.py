from random import randint

player_wins = 0
computer_wins = 0
win_score = int(input("Enter winning score :"))


while player_wins < win_score and computer_wins < win_score: 
    print("\nPlayer Score: {}  Computer Score : {}".format(player_wins,computer_wins))
    print("\n...Rock...Paper...Scissors...")


    player = input("\nPlayer, make your move: ").lower()
    
    if player == "quit" or player == "q":
        break
    
    rand_num = randint(0,2)

    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'

    print('\ncomputer plays : {}'.format(computer))

    if player == computer:
        print("\nIt's a tie!")

    elif player == 'rock':
        if computer == 'scissors':
            print("\nPlayer wins!")
            player_wins += 1
        else:
            print('\ncomputer wins!')
            computer_wins += 1

    elif player == 'paper':
        if computer == 'rock':
            print("\nPlayer wins!")
            player_wins += 1
        else:
            print('\ncomputer wins!')
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'paper':
            print("\nPlayer wins!")
            player_wins += 1
        else:
            print('\ncomputer wins!')
            computer_wins += 1

    else:
        print("\nPlease enter a valid move!")

if player_wins > computer_wins:
    print("\nCONGRATS, YOU WON \U0001f600")
elif player_wins == computer_wins:
    print ("\nIT'S A TIE")
else:
    print ("\nOH NO, YOU LOSE \U0001F61E")

print("\nFINAL SCORES...  Player Score: {}  Computer Score : {}".format(player_wins,computer_wins))