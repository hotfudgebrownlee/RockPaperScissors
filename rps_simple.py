from io import StringIO
import sys
import random

"""Play Rock Paper Scissors. Two computers are pitted against each other.
At the beginning level, it will pick one at random.
At the intermediate level, it will choose an option based on your previous choice.
At the advanced level, it will choose an option based on learning of previous choices."""

winners = []

def call_lvl(player1lvl, player2lvl):
    p1 = player1lvl.lower()
    p2 = player2lvl.lower()
    try:
        print()
        player_1 = ('rock').upper()
        player_2 = user_player_2(None, None)
        winner = round_winner(player_2, player_1)
        print(f'Player 1: {player_1} // Player 2: {player_2} // {winner}')
        in_the_lead()
        i = 0
        last_pl1 = player_1
        last_pl2 = player_2

        while(last_pl2 != 'Q'):
            if last_pl2 == 'Q':
                break
            else:
                pl1 = f'{p1}_player_1'
                pl2 = f'{p2}_player_2'
                newfunc = globals().copy()
                newfunc.update(locals())
                pl1_func = newfunc.get(pl1)
                pl2_func = newfunc.get(pl2)
                player_1 = pl1_func(last_pl2, winners[-1])
                player_2 = pl2_func(last_pl1, winners[-1])
                winner = round_winner(player_2, player_1)                
                print(f'Player 1: {player_1} // Player 2: {player_2} // {winner}')
                in_the_lead()
                last_pl2 = player_2
                last_pl1 = player_1
                
                

        if last_pl2 == 'Q':
            endgame(player1lvl, player2lvl)

    except IndexError:
        print('Goodbye!')

def user_player_2(player_1, last_win):
    choice = input('Rock, Paper, Scissors, SHOOT! ').upper()
    if choice.startswith('R'):
        player_2 = 'ROCK'
    elif choice.startswith('P'):
        player_2 = 'PAPER'
    elif choice.startswith('S'):
        player_2 = 'SCISSORS'
    elif choice.startswith('Q'):
        player_2 = 'Q'
    else:
        player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()

    return player_2

def beginner_player_1(player_2, last_win):
    if (last_win == 'pl2'):
        player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
        print('I will choose randomly because I lost.\n')
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'
        print('I will choose the same option because we tied.\n')
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
        print('I will choose the same option because I won.\n')
    
    return player_1

def intermediate_player_1(player_2, last_win):
    if (last_win == 'pl2'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
        print('I will choose what beats your last option because you won.\n')
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'
        print('I will choose the same option because we tied.\n')
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
        print('I will choose the same option because I won.\n')

    return player_1

def advanced_player_1(player_2, last_win):
    if (last_win == 'pl2'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
        print('I will choose what beats your last option because you won.\n')
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
        print('I will choose what beats your last option because we tied.\n')
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'
        print('I will assume you try to beat my last option, and pick what beats that.\n')

    return player_1

def round_winner(pl2, pl1):
    point = ''
    if pl2 == pl1:
        point = 'Tie game.'
        winners.append('none')
    elif pl2 == 'ROCK':
        if pl1 == 'PAPER':
            winners.append('pl1')
            point = 'Point- Player 1!'
        elif pl1 == 'SCISSORS':
            winners.append('pl2')
            point = 'Point- Player 2!'
    elif pl2 == 'PAPER':
        if pl1 == 'SCISSORS':
            winners.append('pl1')
            point = 'Point- Player 1!'
        elif pl1 == 'ROCK':
            winners.append('pl2')
            point = 'Point- Player 2!'
    elif pl2 == 'SCISSORS':
        if pl1 == 'ROCK':
            winners.append('pl1')
            point = 'Point- Player 1!'
        elif pl1 == 'PAPER':
            winners.append('pl2')
            point = 'Point- Player 2!'
    return point

def in_the_lead():
    if(winners.count('pl1') > winners.count('pl2')):
        scoreboard = ['Player 1', winners.count('pl1'), winners.count('pl2')]
    elif(winners.count('pl2') > winners.count('pl1')):
        scoreboard = ['Player 2', winners.count('pl2'), winners.count('pl1')]
    elif(winners.count('pl2') == winners.count('pl1')):
        scoreboard = ['No one', winners.count('pl2'), winners.count('pl1')]
        
    print(f'{scoreboard[0]} is winning. Score: {scoreboard[1]} / {scoreboard[2]}')

def endgame(player1lvl, player2lvl):
    print(f'Player 1: {player1lvl} vs Player 2: {player2lvl}')
    print(f'Games Played: {len(winners)}')
    print(winners)
    
    if(winners.count('pl1') > winners.count('pl2')):
        scoreboard = ['Player 1', winners.count('pl1'), winners.count('pl2')]
    elif(winners.count('pl2') > winners.count('pl1')):
        scoreboard = ['Player 2', winners.count('pl2'), winners.count('pl1')]
    elif(winners.count('pl2') == winners.count('pl1')):
        scoreboard = ['No one', winners.count('pl2'), winners.count('pl1')]
        
    print(f'{scoreboard[0]} won! Score: {scoreboard[1]} / {scoreboard[2]}')
    print()

    winners.clear()

def main():
    choice = input("Player One: Beginner, Intermediate, or Advanced level? ").upper()
    if choice.startswith('B'):
        player_one = 'Beginner'
    elif choice.startswith('I'):
        player_one = 'Intermediate'
    elif choice.startswith('A'):
        player_one = 'Advanced'
    else:
        print("Not a valid option.")
        main()
    option = input("Player Two: Beginner, Intermediate, or Advanced level? ").upper()
    if option.startswith('U'):
        player_two = 'User'
    else:
        print("Not a valid option.")
        main()
    call_lvl(player_one, player_two)

main()