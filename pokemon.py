# coding: utf-8

import re


class Player:
    '''
    Player class that defines current player position (x, y) and track each
    place where a Pokemon was cought as (x, y) coordinates as well. There are
    four public methods to move the player to each direction and catch new
    Pokemons and two public methods to retrieve player name and total quantity
    of Pokemons caught.
    '''

    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__pokemons = [(0, 0)]

    def move_north(self):
        self.__y += 1
        self.__add_pokemon()

    def move_south(self):
        self.__y -= 1
        self.__add_pokemon()

    def move_west(self):
        self.__x -= 1
        self.__add_pokemon()

    def move_east(self):
        self.__x += 1
        self.__add_pokemon()

    def __add_pokemon(self):
        '''
        Private method to register a new Pokemon caught if it wasn't already
        registered.
        '''
        current_pos = (self.__x, self.__y)
        if(current_pos not in self.__pokemons):
            self.__pokemons.append(current_pos)

    def get_name(self):
        return self.__name

    def get_total_pokemons(self):
        return len(self.__pokemons)


def get_moves_string():
    '''
    Method to manually get the move list from user through a single string of
    characters that represents the four directions: N, S, E and W. Only these
    letters are accepted.
    '''
    moves_string = input('Please type the move string (N, S, E, W). '
                         'For example: NNSSEWEW\n').upper()
    pattern = r'^[NSEW]+$'
    if bool(re.search(pattern, moves_string)):
        return moves_string
    else:
        print("There are invalid characters. Please try again...\n\n")
        return get_moves_string()


def make_moves(player, move_string):
    '''
    Method to make the player movement in batch accordingly the string of moves
    passed.
    '''
    for move in move_string:
        if move == 'N':
            player.move_north()
        elif move == 'S':
            player.move_south()
        elif move == 'W':
            player.move_west()
        elif move == 'E':
            player.move_east()


def print_results(player, moves_string):
    '''
    Method to display the results
    '''
    print('%s Moves: %s\nPokemon Count: %s'
          % (player.get_name(), moves_string, player.get_total_pokemons()))


if __name__ == "__main__":

    ash = Player('Ash')
    moves_string = get_moves_string()
    make_moves(ash, moves_string)
    print_results(ash, moves_string)
