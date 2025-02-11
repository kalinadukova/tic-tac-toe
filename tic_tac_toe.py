from typing import Type

def initialize_board():
    size = 3
    for row in range(size):
        coordinates.append([])
        for column in range(size):
            coordinates[row].append('-')

    print(coordinates)
    return size

def enter_coordinates(size, type):
    print('Enter ' + type + ' coordinate:')
    get_coordinate(size, type)

def get_coordinate(size, type):
    print('Enter the row coordinate: ')
    coordinate_row = int(input())
    while (coordinate_row <= 0) or (coordinate_row > board_size):
        print('Error, please enter a valid coordinate!')
        print('Enter the row coordinate: ')
        coordinate_row = int(input())

    print('Enter the column coordinate: ')
    coordinate_column = int(input())
    while (coordinate_column <= 0) or (coordinate_column> board_size):
        print('Error, please enter a valid coordinate!')
        print('Enter the column coordinate: ')
        coordinate_column = int(input())

    is_coordinate_available = check_is_coordinate_available(coordinate_row, coordinate_column)

    if not is_coordinate_available:
        print('Error, please enter a valid coordinate!')
        get_coordinate(size, type)
    else:
        coordinates[coordinate_row - 1][coordinate_column - 1] = type

def check_is_coordinate_available(coordinate_row, coordinate_column,):
    is_coordinate_available = True

    if (coordinates[coordinate_row- 1][coordinate_column - 1] != '-'):
        is_coordinate_available = False

    return is_coordinate_available

def play_game(available_moves):
    print('Welcome to Tic Tac Toe!')
    while available_moves > 0:
        if available_moves % 2 == 1:
            type = 'x'
        else:
            type = 'o'
        available_moves -= 1
        enter_coordinates(available_moves, type)
        print_board(coordinates)


def print_board(coordinates):
    for row in coordinates:
        print('')
        for column in row:
            print(column, end=' ')
    print('')

# def check_if_winner_exists():

coordinates = []
board_size = initialize_board()
available_coordinates = board_size*board_size
print('Available coordinates: 1 -', available_coordinates)
play_game(available_coordinates)