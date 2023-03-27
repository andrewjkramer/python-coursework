### Point of Sale Terminal
### by Andrew Kramer
#

"""

This program is a simple POS terminal demo.

It asks the user for an item name, price, and quantity. It then presents the sub total for each respective item, and concludes with a grand running total.

"""
### PSEUDOCODE
"""

Define the main function:

- Allow for a total of 3 entries with a constant named MAX
- Establish a variable to work as a price accumulator.
- Ask the user for the item_name, unit_price, and quantity.

- For each item, calculate the sub_total with the formula:
    sub_total = unit_price * quantity

- For each itea, print the formula result.
- After printing the result, ask for the next item.
- After printing the last (3) item, print the grand_total of all three items.

"""


def main():

    # Establish the maximum amount of entries.

    MAX = 3

    # Initialize an accumulator variable.

    grand_total = 0.0

    # Establish accumulator.

    for counter in range(MAX):

        # Ask the user for the name of the item.

        item_name = input('Enter item name ' )

        # Ask the user for the price of the item.

        unit_price = float(input(f'Enter unit price of {item_name} '))

        # Ask the user for the quantity of the item.

        quantity = int(input(f'Enter quantity of {item_name} '))

        # Calculate the sub_total.

        sub_total = unit_price * quantity

        # Print the quantity, item name, and total for the current item.

        print(f'{quantity} {item_name} @ ${unit_price:.2f}, total ${sub_total:.2f}')
        
        # Add the accumulator variable into the for loop to accumulate the grand_total.

        grand_total = grand_total + sub_total

    # Print the grand total.

    print(f'Total of these three items is ${grand_total:.2f}')

main()
