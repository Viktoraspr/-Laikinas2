"""
There are forms, which are used to take data from UI.
"""

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from .constants import MAX_DICE_SIDES, MAX_DICES_NUMBER


class DicesNumber(FlaskForm):
    """
    Form for dices
    :param dices_number: how many dices will be used in the game
    :param submit: submit button in form
    """
    dices_number = IntegerField(f'Dices number: (between 1 - {MAX_DICES_NUMBER})', validators=[DataRequired(),
                                                                             NumberRange(min=1, max=MAX_DICES_NUMBER)])
    submit = SubmitField('Submit')


class DiceSides(FlaskForm):
    """
    Form for sides of dice
    :param dice_sides: how many dices the dice has
    :param submit: submit button in form
    """
    dice_sides = IntegerField(f'Dice sides: from 1 till {MAX_DICE_SIDES}', validators=[DataRequired(),
                                                                         NumberRange(min=1, max=MAX_DICE_SIDES)])
    submit = SubmitField('Submit')
