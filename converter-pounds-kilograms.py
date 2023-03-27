### Pounds to Kilograms Converter
### by Andrew Kramer
#

"""

This program asks the user to enter a weight in pounds, converts the weight to kilograms, and displays the result.

"""
### PSEUDOCODE
"""

Define the main function:

- Prompt user to enter pounds
- Input pounds
- Convert pounds into kilograms with the following equation
- Multiply pounds by 0.45359237 ( POUNDS_TO_KILOGRAMS )
- Display result with entered pounds and calculated kilograms

"""


def main():

    POUNDS_TO_KILOGRAMS = 0.45359237                          # conversion formula constant

    x_Pounds = float(input('Enter the pounds: '))              # user is prompted to input pounds
    x_Kilograms = (x_Pounds) * POUNDS_TO_KILOGRAMS            # x_Kilograms variable established with conversion formula

    print(f'{x_Pounds} pounds is {x_Kilograms:.3f} kilograms') # display calculated result

main()
