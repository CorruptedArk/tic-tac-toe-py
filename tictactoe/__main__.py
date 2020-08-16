#!/usr/bin/env python3

"""This is the main module. It handles the overarching functionality of the program."""
# tic-tac-toe-py is a simple terminal tic tac toe game written in Python
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

#   tic-tac-toe-py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   tic-tac-toe-py is distributed in the hope that it will be fun,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List
from enum import Enum, auto
import random
import numpy

BOARD_SIZE = 3
SPACE = ' '
ESC = chr(27) 
X = 'X'
O = 'O'



MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

ABOUT = f"""tic-tac-toe-py {VERSION} - Fork me at <https://github.com/CorruptedArk/tic-tac-toe-py>

tic-tac-toe-py is a simple terminal tic tac toe game written in Python
  Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

  tic-tac-toe-py is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  tic-tac-toe-py is distributed in the hope that it will be fun,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def get_version() -> str:
    """Returns the formatted version string"""
    return VERSION

def print_about() -> None:
    """Prints out about and license information"""
    wipe_screen()
    print(ABOUT)

class GameEndStates(Enum):
    """A class that enumerates the possible game end states"""
    WIN = auto()
    LOSS = auto()
    TIE = auto()

def wipe_screen() -> None:
    """Clears all text from the terminal"""
    print(ESC + "[H" + ESC + "[J", end="")

def print_win() -> None:
    """Tells a player that they have won the game"""
    print('You win!')

def print_loss() -> None:
    """Tells a player that they have lost the game. You have also lost the game."""
    print('You lose!')

def print_tie() -> None:
    """Tells a player that they have tied the game"""
    print('You tie!')

def print_board(board: List[List[str]]) -> None:
    """Prints out the current state of the board with nice formatting"""

    for i, _row in enumerate(board):
        if i > 0:
            print(f'\n  {(2 * len(board[i]) + 1) * "-"}\n', end='')
        else:
            print('\n  ', end='')
            for j in range(len(board[i])):
                print(f' {j + 1}', end='')
            print()

        for j, _element in enumerate(board[i]):
            if j == 0:
                print(f' {i + 1} {board[i][j]}', end='')
            else:
                print(f'|{board[i][j]}', end='')
    print('\n')


def play_opponent_turn(board: List[List[str]], opponent_symbol: str) -> None:
    """Plays a move for the computer. Currently picks a random empty space on the board."""
    space_found = False
    while not space_found:
        row = random.randint(0, BOARD_SIZE)
        column = random.randint(0, BOARD_SIZE)
        
        if board[row][column] == SPACE:
            board[row][column] = opponent_symbol
            space_found = True

def has_empty_spaces(board: List[List[str]]) -> bool:
    """Returns True if there is at least one empty space in the board, returns False otherwise"""
    has_space = False
    for row in board:
        if SPACE in row:
            has_space = True
            break
    return has_space

def symbol_won(board: List[List[str]], symbol: str) -> bool:
    """Returns True if the player represented by symbol has won the game and False otherwise"""
    #Check rows
    for row in board:
        all_elements_are_symbol = True
        for element in row:
            if element != symbol:
                all_elements_are_symbol = False
                break
        if all_elements_are_symbol:
            return True

    #Check columns
    transpose_board = numpy.transpose(board)
    for row in transpose_board:
        all_elements_are_symbol = True
        for element in row:
            if element != symbol:
                all_elements_are_symbol = False
                break
        if all_elements_are_symbol:
            return True

    #Check diagonals    
    all_elements_are_symbol = True
    for i in range(BOARD_SIZE):
        if board[i][i] != symbol:
            all_elements_are_symbol = False
            break
    if all_elements_are_symbol:
        return True

    all_elements_are_symbol = True
    for i in range(BOARD_SIZE):
        if board[i][-i - 1] != symbol:
            all_elements_are_symbol = False
            break
    if all_elements_are_symbol:
        return True

    return False

def main():
    """The main function. It controls the overall loop of the game"""
    still_playing = True
    while still_playing:
        board = [[SPACE for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        
        wipe_screen()
        player_symbol = input('Pick your symbol, X or O (X is default): ')
        
        player_symbol = player_symbol.capitalize()

        opponent_symbol = ''
        
        if player_symbol == O:
            opponent_symbol = X
        else:
            player_symbol = X
            opponent_symbol = O

        if player_symbol == O:
            play_opponent_turn(board, opponent_symbol)
        
        game_state = GameEndStates.TIE
        game_over = False
        while not game_over:
            wipe_screen()
            print(f'You are playing as {player_symbol}')
            print_board(board)
            
            valid_move = False
            
            row = -1
            column = -1

            while not valid_move:
                row = input('Enter the row for your move: ')
                column = input('Enter the column for your move: ')
                
                inputs_are_ints = False

                try:
                    row = int(row)
                    column = int(column)
                    inputs_are_ints = True
                except ValueError:
                    inputs_are_ints = False
        
                if(inputs_are_ints):
                    row -= 1
                    column -= 1
                
                valid_move = inputs_are_ints and row in range(len(board)) and column in range(len(board[row])) and board[row][column] == SPACE 

                if valid_move:
                    board[row][column] = player_symbol
                else:
                    print('\nInvalid move, please try again')
           

            if symbol_won(board, player_symbol):
                game_over = True
                game_state = GameEndStates.WIN      
                break
            if not has_empty_spaces(board):
                game_over = True
                game_state = GameEndStates.TIE
                break

            print_board(board)

            play_opponent_turn(board, opponent_symbol)
            
            if symbol_won(board, opponent_symbol):
                game_over = True
                game_state = GameEndStates.LOSS
                break
            if not has_empty_spaces(board):
                game_over = True
                game_state = GameEndStates.TIE
                break
        
        switcher = {
            GameEndStates.WIN: print_win,
            GameEndStates.LOSS: print_loss,
            GameEndStates.TIE: print_tie
        }

        wipe_screen()
        switcher.get(game_state)()
        print_board(board)
        continue_prompt = input('Play again? (y/N):').capitalize()
        still_playing = continue_prompt == 'Y'


if __name__ == '__main__':
    main()
