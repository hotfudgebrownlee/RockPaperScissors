from io import StringIO
import sys
import random

last_pl2 = 'ROCK'
last_pl1 = 'SCISSORS'
winners = ['pl2']

def human_player_2(player_1, play_2, last_win):
    """At the human level, the computer picks "randomly"
    every time using the python random library, but if the
    previous option was the same as the new one, it changes
    to become a different option. For example, if the last
    choice was rock, it will not pick rock."""
    player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    if player_1 == play_2:
        while player_1 == play_2:
            player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
        return player_1
    elif player_1 != play_2:
        return player_1

def advanced_player_1(player_2, play_1, last_win):
    if (last_win == 'pl2'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'

    return player_1

players = ['advanced', 'human']
for p1 in players:
    pl1 = f'{p1}_player_1'
    newfunc = globals().copy()
    newfunc.update(locals())
    pl1_func = newfunc.get(pl1)
    play = pl1_func(last_pl2, last_pl1, winners[-1])
    print(play)


