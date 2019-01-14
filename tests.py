# coding: utf-8

import unittest
from pokemon import Player, make_moves


class TestMoveMethods(unittest.TestCase):

    __test_data = [
        {
            'player': Player('Player 1'),
            'moves': 'E',
            'expected': 2
        },
        {
            'player': Player('Player 2'),
            'moves': 'NESW',
            'expected': 4
        },
        {
            'player': Player('Player 3'),
            'moves': 'NSNSNSNSNS',
            'expected': 2
        },
        {
            'player': Player('Player 4'),
            'moves': 'NNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEE'
                     'SSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWW',
            'expected': 80
        },
        {
            'player': Player('Player 5'),
            'moves': 'NSNSNSNSNSNSNSNSNSNSNSNSNSNSNSNSNSNSNSNS'
                     'WSWSWSWSWSWSWSWSWSWSWSWSWSWSWSWSWSWSWSWS',
            'expected': 42
        },
        {
            'player': Player('Player 6'),
            'moves': 'NNNNEESSWWSSEENN',
            'expected': 13
        }
    ]

    def test_moves(self):
        '''
        Test each player movement from test data and checks the expected
        Pokemon caught
        '''

        for player in self.__test_data:
            make_moves(player['player'], player['moves'])
            self.assertEqual(player['player'].get_total_pokemons(),
                             player['expected'])


if __name__ == "__main__":
    unittest.main()
