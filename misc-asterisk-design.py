### Asterisk Design Generator
### by Andrew Kramer
#

"""

This program prints a design of asterisks based upon a quantity of rows the user enters.

"""
### PSEUDOCODE
"""

Define the main function:

- Ask the user for the amount of rows

- Establish a for loop using the amount of rows

- Use a for row range with the amount of rows

- Use a nested loop for column range with a formula to print the design from the highest quantity of asterisks per row to the least.

- The formula is:
    the entered row quantity - the current row.

- End the program when all of the rows are printed.

"""

def main():

    # Ask user how many rows should be designed.

    row_quantity = int(input(f'How many rows? '))

    # Establish for loop using entered row quantity.

    for row in range(row_quantity):

        # Establish nested for loop for columns and formula.

        for column in range(row_quantity - row):

            # Print the design

            print('*', end='')

        # Create a new line for each row

        print()

main()
