"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - numbers of layers added to the lasagna
    :return: int - remaining prep time (in minutes) derived from 'number_of_layers'.

    Function that takes the number of layers to be added to lasagna and gives how long it would take to prepare them.
    """
    return PREPARATION_TIME * number_of_layers

    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake) in minutes.

    :param number_of_layers: int - numbers of layers the lasagna has
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - the elapsed cooking time (in minutes) derived from the 'number_of_layers'and the 'elapsed_bake_time'

    
    Function that takes the number of layers the lasagna has and the actual minutes the lasagna has been in the oven as
    an argument and returns how much time has elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
