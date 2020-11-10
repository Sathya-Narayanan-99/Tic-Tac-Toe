import random
from os import system, name
from time import sleep


# Displays the welcome Message
def welcome_msg():
    print("\nWelcome to TicTacToe!")


# Gets the player's choice of game mode and returns it
def game_mode():
    print("\n1. Do you want to play against the computer")
    print("\n", "\t" * 2, '(or)')
    print("\n2. Do you want to play against another player(2 players)")
    accecptable_choice = range(1, 3)
    choice = ''
    while choice not in accecptable_choice:
        choice = input("\nChoose your game mode : ")
        if choice.isdigit():
            choice = int(choice)
        if choice not in accecptable_choice:
            print("Sorry! It's not a valid input.")
        else:
            return choice


# Takes the player's information and returns a list of player's name
def player_details(mode):
    if mode == 1:
        player_1 = input("\nEnter your name : ")
        player_2 = "Computer"
        return [player_1, player_2]
    else:
        player_1 = input("\nPlayer 1, enter your name : ")
        player_2 = input("\nPlayer 2, enter your name : ")
        return [player_1, player_2]


# Clears the display screen
def clear():
    if name == 'nt':
        _ = system('cls')


# Displays the board
def display_board(gamelist):
    clear()
    print('\n' * 10)
    print('\t', gamelist[7], "||", gamelist[8], "||", gamelist[9])
    print("-" * 30)
    print('\t', gamelist[4], "||", gamelist[5], "||", gamelist[6])
    print("-" * 30)
    print('\t', gamelist[1], "||", gamelist[2], "||", gamelist[3])
    print('\n' * 10)


# Updates the board with user option
def place_marker(board, marker, position):
    board[position] = marker
    return board


# Conditon to check if the player has won
def isWin(board):
    if board[1] == board[2] == board[3] != ' ':
        return True
    elif board[4] == board[5] == board[6] != ' ':
        return True
    elif board[7] == board[8] == board[9] != ' ':
        return True
    elif board[7] == board[8] == board[9] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    elif board[3] == board[6] == board[9] != ' ':
        return True
    elif board[1] == board[5] == board[9] != ' ':
        return True
    elif board[3] == board[5] == board[7] != ' ':
        return True
    else:
        return False


def isWinPossible(board, marker, position):
    board[position] = marker
    result = isWin(board)
    board[position] = ' '
    return result


# Condition to check if the position is free
def isSpacefree(board, position):
    return board[position] == ' '


# Condition to check if the board is full
def isFull(board):
    for pos in board:
        if pos == ' ':
            return False
    return True


# Gets the player's choice of position
def player_choice(board, player, marker):
    accepltable_range = range(1, 10)
    position = ''  # Initially set to empty string so that the while loop is executed
    spacefree = True  # Initially the position is assumed to be free since user hasn't selected a position

    while position not in accepltable_range and spacefree == True:
        position = input(f"\n{player} '{marker}', enter your positon (0 to 9) : ")

        if position.isdigit():
            position = int(position)

        if position in accepltable_range:
            if isSpacefree(board, position):
                return position
            else:
                position = ''
                print("\nThe position is not empty!")
        else:
            print("\nSorry! It's not a valid input.")


def computer_choice(board, computer_marker, player_marker):
    # Scanning for all available positions
    available_positions = []
    for pos in range(1, 10):
        if isSpacefree(board, pos):
            available_positions.append(pos)

    for pos in available_positions:
        # Checking is computer has a win possibility
        if isWinPossible(board, computer_marker, pos):
            return pos
        # Checking if player has a win possibility
        elif isWinPossible(board, player_marker, pos):
            return pos
    # Return a random position if no win is possible
    return random.choice(available_positions)


# Condition to check if the player want's to replay
def isReplay():
    replay = ''  # Initailly set to empty string so that the while loop can be executed
    acceptable_choice = ['y', 'n']
    while replay not in acceptable_choice:
        replay = input("\nDo you want to continue playing (Y or N) : ")
        replay.lower()
        if replay in acceptable_choice:
            return replay == 'y'
        print("Sorry, its not a valid input!")


# The main Function
if __name__ == '__main__':

    game_on = True

    # The game loop
    while game_on:

        welcome_msg()
        sleep(1.5)
        mode = game_mode()

        # Game mode 2 (2 players)
        if mode == 2:

            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Initial board

            player_names = player_details(mode)
            moves_count = 0

            player_1_marker = 'X'
            player_2_marker = 'O'

            first_turn = random.randint(0, 1)  # Random selection of the first player

            display_board(board)

            # Assigning respective user as player1 and player2
            print(f"\n{player_names[first_turn]} is 'X' and goes first!")
            player_1 = player_names[first_turn]
            player_names.pop(first_turn)
            player_2 = player_names[0]

            winning = False  # Initially the winning condition is set False

            # Loop until there's a winner
            while not winning:

                # Player_1 turn
                moves_count += 1
                print("\nMove : ", moves_count)
                position = player_choice(board, player_1, player_1_marker)
                board = place_marker(board, player_1_marker, position)
                display_board(board)
                # Checking if player_1 has won the game
                if isWin(board):
                    print(f"\nCONGRATULATIONS {player_1}!!!,\nYou have won the game in {moves_count} moves!")
                    winning = True
                    break

                # Condition to check if the game is a draw
                if isFull(board):
                    print("It's a draw!")
                    break

                # Player_2 turn
                moves_count += 1
                print("\nMove : ", moves_count)
                position = player_choice(board, player_2, player_2_marker)
                board = place_marker(board, player_2_marker, position)
                display_board(board)
                # Checking if player_2 has won the game
                if isWin(board):
                    print(f"\nCONGRATULATIONS{player_2}!!!,\nYou have won the game in {moves_count} moves!")
                    winning = True

            # Replay or Quit after the game is over
            game_on = isReplay()
            clear()

        # Game mode 1 (1 player)
        else:

            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Initial board

            player_names = player_details(mode)  # List of player names
            moves_count = 0

            player_1_marker = 'X'
            player_2_marker = 'O'

            first_turn = random.randint(0, 1)  # Random selection of the first player

            display_board(board)

            # Assigning respective user as player1 and player2
            print(f"\n{player_names[first_turn]} is 'X' and goes first!")
            print('\n' * 5)
            sleep(2)
            player_1 = player_names[first_turn]
            player_names.pop(first_turn)
            player_2 = player_names[0]

            winning = False  # Initially the winning condition is set False

            # Loop until there's a winner
            while not winning:

                # Player_1 turn
                moves_count += 1
                print("\nMove : ", moves_count)

                # If Player_1 is the computer
                if player_1 == 'Computer':
                    position = computer_choice(board, player_1_marker, player_2_marker)

                # If player_1 is the player
                else:
                    position = player_choice(board, player_1, player_1_marker)
                board = place_marker(board, player_1_marker, position)
                display_board(board)
                # Checking if player_1 has won the game
                if isWin(board):
                    if player_1 == 'Computer':
                        print("Sorry, you lost to the computer")
                    else:
                        print(f"\nCONGRATULATIONS {player_1}!!!,\nYou have won the game in {moves_count} moves!")
                        winning = True
                    break

                # Condition to check if the game is a draw
                if isFull(board):
                    print("It's a draw!")
                    break

                # Player_2 turn
                moves_count += 1
                print("\nMove : ", moves_count)

                # If Player_2 is the computer
                if player_2 == 'Computer':
                    position = computer_choice(board, player_2_marker, player_1_marker)


                # If player_2 is the player
                else:
                    position = player_choice(board, player_2, player_2_marker)
                board = place_marker(board, player_2_marker, position)
                display_board(board)
                # Checking if player_2 has won the game
                if isWin(board):
                    if player_2 == 'Computer':
                        print("Sorry, you lost to the computer")

                    else:
                        print(f"\nCONGRATULATIONS {player_2}!!!,\nYou have won the game in {moves_count} moves!")
                        winning = True
                    break
            # Replay or Quit after the game is over
            game_on = isReplay()
            clear()
