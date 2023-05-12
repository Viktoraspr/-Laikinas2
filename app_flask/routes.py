"""
Routes files.
"""

from app_flask import app
from flask import render_template, redirect, url_for, request

from .forms import DicesNumber, DiceSides
from .game_classes import Dice, Game
from .constants import MAX_ROLLS_IN_MEMORY

game = Game()


@app.route("/")
@app.route("/home")
def home():
    """
    Home page of site.
    :return: render template object
    """
    game.start_new_game()
    return render_template('home.html')


@app.route("/settings", methods=['GET', 'POST'])
def settings():
    """
    Settings page: we add dices in the game
    :return: render template object
    """
    dices_number = DicesNumber()
    if dices_number.validate_on_submit():
        return redirect(url_for('settings_sides', dices=dices_number.dices_number.data))
    return render_template('settings.html', dice_number=dices_number)


@app.route("/add_sizes/<int:dices>", methods=['GET', 'POST'])
def settings_sides(dices):
    """
    Settings page: adding parameters to dices
    :param dices: number of dices in the game
    :return: render template object
    """
    dice_sides = DiceSides()
    if request.method == 'POST':
        game.add_dice(Dice(len(game.dices) + 1, dice_sides.dice_sides.data))
        if len(game.dices) == dices:
            return redirect(url_for('roll_the_dices'))
        else:
            return redirect(url_for('settings_sides', dices=dices))
    return render_template('setting_sides.html', number=dices, dice_sides=dice_sides, all_dices=game.dices)


@app.route("/rolls_dices", methods=['GET', 'POST'])
def roll_the_dices():
    """
    The roll of game is starting
    :return: render template object
    """
    if request.method == 'POST':
        game.roll_the_dices()
        return redirect(url_for('roll_the_dices'))
    return render_template('roll_the_dices.html', game=game, MAX_ROLLS_IN_MEMORY=MAX_ROLLS_IN_MEMORY)
