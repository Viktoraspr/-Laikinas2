"""
Unit tests for Dice and Game classes
"""

import unittest
from collections import deque

from .game_classes import Dice, Game, MAX_ROLLS_IN_MEMORY


class TestDice(unittest.TestCase):

    def test_sides(self):
        dice = Dice(name=1, sides=1)
        self.assertEqual(dice.sides, 1)
        self.assertEqual(dice.name, 1)
        with self.assertRaises(ValueError):
            dice.sides = 1008
        with self.assertRaises(ValueError):
            dice= Dice(5, 1008)


class TestGame(unittest.TestCase):

    def test_sides(self):
        game = Game()
        game.dices = [Dice(1, 20), Dice(2, 40)]
        for _ in range(10000):
            game.roll_the_dices()
        self.assertEqual(len(game.result), MAX_ROLLS_IN_MEMORY)
        self.assertEqual(len(game.dices), 2)
        self.assertNotEqual(len(game.dices), 1)
        game.start_new_game()
        self.assertEqual(game.dices, [])
        self.assertEqual(game.result, deque([]))
