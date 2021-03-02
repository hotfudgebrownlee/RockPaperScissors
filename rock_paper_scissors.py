from io import StringIO
import sys
import random

"""Play Rock Paper Scissors. Two computers are pitted against each other.
At the beginning level, it will pick one at random if it loses.
At the intermediate level, it will try to beat you if it loses.
At the advanced level, it will try to beat you even if it wins."""

# Clear out results sheet to make room for new results.
results = open("rps_results", "a+")
results.truncate(0)
results.write('bot vs bot, winner, win score, lose score\n')
results.close()

# Create an empty list to store the score.
winners = []

def call_lvl(player1lvl, player2lvl):
    """This function is designed to call whatever strategies the users choose
    and call the corresponding functions. It also provides some randomization
    so as to make gameplay between the bots more realistic."""

    # take the two levels of gameplay and store them to be called as functions.
    p1 = player1lvl.lower()
    p2 = player2lvl.lower()

    try:
        print()
        # start the game with two randomly selected rock, paper, scissors options.
        player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
        player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
        # find the winner and print the results.
        winner = round_winner(player_2, player_1)
        # print(f'Player 1: {player_1} // Player 2: {player_2} // {winner}')
        # update and print the scoreboard.
        # in_the_lead()
        # store the last plays so the bots can use them for decision-making next round.
        last_pl1 = player_1
        last_pl2 = player_2
        # set a dummy variable to count rounds.
        rounds = 1
        # create a loop to iterate through 100 games.
        while(last_pl2 != 'Q'):
            if last_pl2 == 'Q':
                break
            if rounds == 100:
                last_pl2 = 'Q'
            else:
                # call the proper functions based on which levels the user passes in.
                pl1 = f'{p1}_player_1'
                pl2 = f'{p2}_player_2'
                newfunc = globals().copy()
                newfunc.update(locals())
                pl1_func = newfunc.get(pl1)
                pl2_func = newfunc.get(pl2)
                # choose a random number within a list.
                num_in_list = [5,8,13][random.randint(0,2)]
                remainder = rounds % num_in_list
                # if rounds played is divisible by this random number, randomize both choices.
                # This simulates fatigue if the same options are picked too many times.
                if remainder == 0:
                    player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
                    player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
                # if not, call the strategy functions and let the bots 
                # play according to their preferred strategy options.
                else:
                    player_1 = pl1_func(last_pl2, last_pl1, winners[-1])
                    player_2 = pl2_func(last_pl1, last_pl2, winners[-1])
                # find the winner and print scoreboard results.
                winner = round_winner(player_2, player_1)                
                # print(f'Player 1: {player_1} // Player 2: {player_2} // {winner}')
                # in_the_lead()
                # track the rounds played.
                rounds += 1
                # store the last game's data for decision-making next round.
                last_pl2 = player_2
                last_pl1 = player_1
        
        # once 100 games have been played, call a function to give the final score.
        if last_pl2 == 'Q':
            endgame(player1lvl, player2lvl)

    except IndexError:
        print('Goodbye!')

def beginner_player_1(player_2, play_1, last_win):
    """At the beginner level, the computer will do one of three things:
    -If it wins, it will retain its winning choice.
    -If it is a tie game, it will retain its choice.
    -If it loses, it will randomly choose a new option."""
    if (last_win == 'pl2'):
        player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
    
    return player_1

def beginner_player_2(player_1, play_2, last_win):
    """At the beginner level, the computer will do one of three things:
    -If it wins, it will retain its winning choice.
    -If it is a tie game, it will retain its choice.
    -If it loses, it will randomly choose a new option."""
    if (last_win == 'pl1'):
        player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    elif (last_win == 'none'):
        if player_1 == 'ROCK':
            player_2 = 'ROCK'
        elif player_1 == 'PAPER':
            player_2 = 'PAPER'
        elif player_1 == 'SCISSORS':
            player_2 = 'SCISSORS'
    elif (last_win == 'pl2'):
        if player_1 == 'ROCK':
            player_2 = 'PAPER'
        elif player_1 == 'PAPER':
            player_2 = 'SCISSORS'
        elif player_1 == 'SCISSORS':
            player_2 = 'ROCK'
    
    return player_2

def intermediate_player_1(player_2, play_1, last_win):
    """At the intermediate level, the computer will do one of three things:
    -If it wins, it will retain its winning choice.
    -If it is a tie game, it will retain its choice.
    -If it loses, it will try to beat the winner's last choice."""
    if (last_win == 'pl2'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'
    elif (last_win == 'none'):
        if player_2 == 'ROCK':
            player_1 = 'ROCK'
        elif player_2 == 'PAPER':
            player_1 = 'PAPER'
        elif player_2 == 'SCISSORS':
            player_1 = 'SCISSORS'
    elif (last_win == 'pl1'):
        if player_2 == 'ROCK':
            player_1 = 'PAPER'
        elif player_2 == 'PAPER':
            player_1 = 'SCISSORS'
        elif player_2 == 'SCISSORS':
            player_1 = 'ROCK'

    return player_1

def intermediate_player_2(player_1, play_2, last_win):
    """At the intermediate level, the computer will do one of three things:
    -If it wins, it will retain its winning choice.
    -If it is a tie game, it will retain its choice.
    -If it loses, it will try to beat the winner's last choice."""
    if (last_win == 'pl1'):
        if player_1 == 'ROCK':
            player_2 = 'PAPER'
        elif player_1 == 'PAPER':
            player_2 = 'SCISSORS'
        elif player_1 == 'SCISSORS':
            player_2 = 'ROCK'
    elif (last_win == 'none'):
        if player_1 == 'ROCK':
            player_2 = 'ROCK'
        elif player_1 == 'PAPER':
            player_2 = 'PAPER'
        elif player_1 == 'SCISSORS':
            player_2 = 'SCISSORS'
    elif (last_win == 'pl2'):
        if player_1 == 'ROCK':
            player_2 = 'PAPER'
        elif player_1 == 'PAPER':
            player_2 = 'SCISSORS'
        elif player_1 == 'SCISSORS':
            player_2 = 'ROCK'
    return player_2

def advanced_player_1(player_2, play_1, last_win):
    """At the advanced level, the computer will do one of three things:
    -If it wins, it will assume the loser tries to beat its most recent choice.
    As a result, it will play whatever beats the choice it assumes the user will make.
    In other words, it will play the loser's last choice.
    -If it is a tie game, it will try to beat the last (tied) choice.
    -If it loses, it will try to beat the winner's last choice."""
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

def advanced_player_2(player_1, play_2, last_win):
    """At the advanced level, the computer will do one of three things:
    -If it wins, it will assume the loser tries to beat its most recent choice.
    As a result, it will play whatever beats the choice it assumes the user will make.
    In other words, it will play the loser's last choice.
    -If it is a tie game, it will try to beat the last (tied) choice.
    -If it loses, it will try to beat the winner's last choice."""
    if (last_win == 'pl1'):
        if player_1 == 'ROCK':
            player_2 = 'PAPER'
        elif player_1 == 'PAPER':
            player_2 = 'SCISSORS'
        elif player_1 == 'SCISSORS':
            player_2 = 'ROCK'
    elif (last_win == 'none'):
        if player_1 == 'ROCK':
            player_2 = 'PAPER'
        elif player_1 == 'PAPER':
            player_2 = 'SCISSORS'
        elif player_1 == 'SCISSORS':
            player_2 = 'ROCK'
    elif (last_win == 'pl2'):
        if player_1 == 'ROCK':
            player_2 = 'ROCK'
        elif player_1 == 'PAPER':
            player_2 = 'PAPER'
        elif player_1 == 'SCISSORS':
            player_2 = 'SCISSORS'
    return player_2

def random_player_1(player_2, play_1, last_win):
    """At the random level, the computer picks randomly 
    every time using the python random library."""
    player_1 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    return player_1

def random_player_2(player_1, play_2, last_win):
    """At the random level, the computer picks randomly
    every time using the python random library."""
    player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    return player_2

def human_player_1(player_2, play_1, last_win):
    """At the human level, the computer picks "randomly"
    every time using the python random library, but if the
    previous option was the same as the new one, it changes
    to become a different option. For example, if the last
    choice was rock, it will not pick rock."""
    player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
    if player_2 == play_1:
        while player_2 == play_1:
            player_2 = ['rock', 'paper', 'scissors'][random.randint(0,2)].upper()
        return player_2
    elif player_2 != play_1:
        return player_2

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

def round_winner(pl2, pl1):
    """Determine the winner of the round."""
    point = ''
    # if the two choices are equal, it's a tie.
    if pl2 == pl1:
        point = 'Tie game.'
        winners.append('none')
    # if not, the logic of rock,paper,scissors is implemented.
    # rock crushes scissors,
    # scissors cut paper,
    # and paper covers rock.
    elif pl2 == 'ROCK':
        if pl1 == 'PAPER':
            # adds winner to scoreboard list.
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
    # checks the scoreboard and prints who is in the lead.
    if(winners.count('pl1') > winners.count('pl2')):
        scoreboard = ['Player 1', winners.count('pl1'), winners.count('pl2')]
    elif(winners.count('pl2') > winners.count('pl1')):
        scoreboard = ['Player 2', winners.count('pl2'), winners.count('pl1')]
    elif(winners.count('pl2') == winners.count('pl1')):
        scoreboard = ['No one', winners.count('pl2'), winners.count('pl1')]
        
    print(f'{scoreboard[0]} is winning. Score: {scoreboard[1]} / {scoreboard[2]}')
    print()

def endgame(player1lvl, player2lvl):
    # prints the game results: 
    # -bot levels 
    # -number of games played 
    # -scoreboard list
    print(f'Player 1: {player1lvl} vs Player 2: {player2lvl}')
    print(f'Games Played: {len(winners)}')
    print(winners)
    
    if(winners.count('pl1') > winners.count('pl2')):
        scoreboard = [f'{player1lvl}', winners.count('pl1'), winners.count('pl2')]
    elif(winners.count('pl2') > winners.count('pl1')):
        scoreboard = [f'{player2lvl}', winners.count('pl2'), winners.count('pl1')]
    elif(winners.count('pl2') == winners.count('pl1')):
        scoreboard = ['No one', winners.count('pl2'), winners.count('pl1')]
        
    print(f'{scoreboard[0]} won! Score: {scoreboard[1]} / {scoreboard[2]}')
    print()

    # writes the game's resultset into a file for further insight.
    results = open("rps_results", "a+")
    results.write(f'{player1lvl} vs {player2lvl}, {scoreboard[0]}, {scoreboard[1]}, {scoreboard[2]}\n')
    results.close()
    results.close()

    winners.clear()

def choose_bots():
    """asks the player to choose two different bot levels
    and passes them in to the call_lvl function."""
    choice = input("Player One: Beginner, Intermediate, or Advanced level? ").upper()
    if choice.startswith('B'):
        player_one = 'Beginner'
    elif choice.startswith('I'):
        player_one = 'Intermediate'
    elif choice.startswith('A'):
        player_one = 'Advanced'
    elif choice.startswith('R'):
        player_one = 'Random'
    elif choice.startswith('H'):
        player_one = 'Human'
    else:
        print("Not a valid option.")
        choose_bots()
    option = input("Player Two: Beginner, Intermediate, or Advanced level? ").upper()
    if option.startswith('B'):
        player_two = 'Beginner'
    elif option.startswith('I'):
        player_two = 'Intermediate'
    elif option.startswith('A'):
        player_two = 'Advanced'
    elif option.startswith('R'):
        player_two = 'Random'
    elif choice.startswith('H'):
        player_two = 'Human'
    else:
        print("Not a valid option.")
        choose_bots()
    call_lvl(player_one, player_two)

def main():
    """Simulates several games at various levels."""
    
    bot_ops = ["beginner\nbeginner", "beginner\nintermediate", \
        "beginner\nadvanced", "beginner\nrandom", "intermediate\nrandom", \
        "intermediate\nintermediate", "intermediate\nadvanced", \
        "advanced\nadvanced", "advanced\nrandom", "random\nrandom", \
        "human\nbeginner", "human\nintermediate", "human\nadvanced", \
        "human\nrandom", "human\nhuman"]

    for option in bot_ops:
        for i in range(1000):
            with StringIO(option) as game:
                stdin = sys.stdin
                sys.stdin = game
                choose_bots()
                sys.stdin = stdin

main()


