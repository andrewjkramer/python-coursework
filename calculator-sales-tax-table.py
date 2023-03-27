### Sales Tax Calculator with Table
### by Andrew Kramer
#

"""

This program calculates the subtotal, sales tax, and total cost
of items, based off a quantity of items ranging from 1 to 10, and displays the totals as a table.

"""
### PSEUDOCODE
"""

Define the main function:

- The TAX_RATE is 7% - use this as a constant.

- Ask the user for the price of the item.
- If the item is greater than or equal to 100.00, the price must be entered again as it must be less than or equal to 99.99.

- Before establishing a while loop, print column headings:
    QUANTITY | SUBTOTAL | SALES TAX | TOTAL

- The column headings must be underlined and centered within a field width of 12.

- Establish a while loop that calculates each category up to a quantity total of 10.

- Quantity will add + 1 each loop.

- The formulas for each other category are as follows:
    subtotal = item_price * quantity
    sales_tax = subtotal * TAX_RATE
    total = subtotal + sales_tax

- Print each resulting number into its respective column.

"""


def main():

    # Establish TAX_RATE constant.

    TAX_RATE = .07

    # Prompt user to enter price.

    item_price = float(input('Item price? '))

    # Check if price is greater than or equal to 100.00

    if item_price >= 100.00:

        # If price is greater than or equal to 100.00
        # ask user to input correct price less than 100.00

        item_price = float(input('Enter a price less than 100.00: '))

    # Display column headings.

    print(f'{"QUANTITY":^12}{"SUBTOTAL":^12}{"SALES TAX":^12}{"TOTAL":^12}')

    # Display horizontal column dividers.

    print(f'{"--------":^12}{"--------":^12}{"---------":^12}{"-----":^12}')

    # Establish quantity variable.
    #
    # I put it right before the while loop
    # where it's easier to locate in relation
    # to the loop code.

    quantity = 0

    # Establish while loop which starts with quantity 0
    # then immediately adds 1 with each iteration
    # and ends once the quantity is less than or equal to 9.
    # 9 is actually 10 in computer speak.

    while quantity <= 9:

        # Use augmented assignment operator to loop from 1 through 10

        quantity += 1

        # Calculate subtotal.

        subtotal = item_price * quantity

        # Calculate sales tax.

        sales_tax = subtotal * TAX_RATE

        # Calculate total.

        total = subtotal + sales_tax

        # Print subtotal, sales tax, and total
        # under the previously printed column headings.

        print(f'{quantity:^12}{subtotal:^12.2f}{sales_tax:^12.2f}{total:^12.2f}')

main()
