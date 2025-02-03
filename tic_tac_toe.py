from typing import Type

print('Welcome to Tic Tac Toe!')
print('Each player takes turn and must input coordinates and in the beginning the board size. The board size must be an odd number')

def initialize_board():
    print('Enter the board size:')
    size = int(input())
    return size

def get_coordinate(size):
    coordinate = int(input())
    while (type(coordinate) != Type[int]) and (coordinate > size):
        print('Error, please enter a valid coordinate!')
        print('Enter the first coordinate: ')
        coordinate = int(input())
    check_is_coordinate_available(coordinate)
    return coordinate


def enter_coordinates(size):
    print('Enter X coordinate: ')
    coordinate_x = get_coordinate(size)
    print('Enter O coordinate: ')
    coordinate_o = get_coordinate(size)

def check_is_coordinate_available(coordinate):
    coordinates.insert(coordinate - 1, coordinate)
    print(coordinates)

coordinates = []
board_size = initialize_board()
available_coordinates = board_size*board_size
print('Available coordinates:')
print(available_coordinates)
enter_coordinates(available_coordinates)