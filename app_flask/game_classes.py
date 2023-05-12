"""
Classes of the game.
"""

from collections import deque
from random import randint
from .constants import MAX_ROLLS_IN_MEMORY, MAX_DICE_SIDES, MAX_DICES_NUMBER


class Dice:
    """
    Form for dices
    :param name: name is number of dice
    :param sides: number of dice sides
    """

    def __init__(self, name, sides):
        self.name: name = name
        self.sides: int = sides

    def __repr__(self):
        return f'Dice {self.name}, {self.sides} sides'

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, sides) -> None:
        """
        checking if sides are in an interval
        :param side: sides
        :return: None
        """
        if not (1 <= sides <= MAX_DICE_SIDES):
            raise ValueError(f'Value must be between 1 and {MAX_DICE_SIDES}')
        self.__sides = sides


class Game:
    """
    Game class - rolls the dices, keeps info in Memory.
    """
    def __init__(self):
        self.dices: list[int] = []
        self.result: deque = deque([])

    def __repr__(self):
        return f'{self.dices}'

    def start_new_game(self):
        """
        Starts new game
        """
        self.dices = []
        self.result = deque([])

    def __append_result(self, value: dict) -> None:
        """
        Appends results in memory
        :param value: dices and result of rolled dice
        :return: None
        """
        if len(self.result) == MAX_ROLLS_IN_MEMORY:
            self.result.popleft()
        self.result.append(value)

    def add_dice(self, dice) -> None:
        """
        Add dice in game.
        :param dice:
        :return: None
        """
        if len(self.dices) == MAX_DICES_NUMBER:
            raise ValueError(f"It can't be added more than {MAX_DICES_NUMBER} dices")
        return self.dices.append(dice)

    def roll_the_dices(self) -> None:
        """
        Roll the dices
        :return: None
        """
        roll_result = {}
        for dice in self.dices:
            roll_result[dice.name] = randint(1, dice.sides)
        roll_result['total'] = sum(roll_result.values())
        self.__append_result(value=roll_result)
