# Guido-s-Gorgeous-Lasagna

Writing some code to help cook a gorgeous lasagna. There are five tasks, all related to cooking your recipe.

1. Define expected bake time in minutes

Define an EXPECTED_BAKE_TIME constant that returns how many minutes the lasagna should bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes:

    >>> import lasagna
    >>> lasagna.EXPECTED_BAKE_TIME
    40

2. Calculate remaining bake time in minutes

Implement the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

    >>> from lasagna import bake_time_remaining
    >>> bake_time_remaining(30)
    10

3. Calculate preparation time in minutes

Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

    >>> from lasagna import preparation_time_in_minutes
    >>> preparation_time_in_minutes(2)
    4

4. Calculate total elapsed cooking time (prep + bake) in minutes

Implement the elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) function that has two parameters: number_of_layers (the number of layers added to the lasagna) and elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

    >>> from lasagna import elapsed_time_in_minutes
    >>> elapsed_time_in_minutes(3, 20)
    26

5. Update the recipe with notes

Go back through the recipe, adding "notes" in the form of function docstrings.
