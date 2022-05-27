import random

'''Rock paper scissors game'''
# Rock blunts scissors, so rock wins
# Scissors cut paper, so scissors win
# Paper covers rock, paper wins
# If players choose same option, a tie results and they play another round
# Maximum number of rounds is 5


name = input('Enter your name: ')
options = ['Rock', 'Paper', 'Scissors']

computerScore = 0
playerScore = 0
numberOfRounds = 0

gameOn = True

print(f'Welcome to the game {name.title()}')

while gameOn:
    computerOption = random.choice(options)
    playerOption = input(f'Enter your choice {name.title()}: ').title()

    print(f'{name.title()} option: {playerOption}')
    print(f'Computer option: {computerOption}')

    numberOfRounds += 1

    if computerOption == playerOption:
        print('Tie')

    elif (computerOption == 'Rock' and playerOption == 'Scissors') or (computerOption == 'Scissors' and playerOption == 'Paper') or (computerOption == 'Paper' and playerOption == 'Rock'):
        print('Computer wins')
        computerScore += 1

    elif (playerOption == 'Rock' and computerOption == 'Scissors') or (playerOption == 'Scissors' and computerOption == 'Paper') or (playerOption == 'Paper' and computerOption == 'Rock'):
        print(f'You win {name.title()}')
        playerScore += 1

    else:
        print('Select a valid option to play this game')

    print('')
    print(f'Round number {numberOfRounds}')

    print('')

    print(f'Player score {playerScore}')
    print(f'Computer score {computerScore}')

    if numberOfRounds == 5:
        gameOn = False
        break

if computerScore == playerScore:
    print('You have tied')
elif playerScore > computerScore:
    print(f'Congratulations {name.title()}, you won!')
else:
    print('Awh man! You lost my nigga. Try again next time')

