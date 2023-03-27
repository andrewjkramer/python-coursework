### Coffee Shop Order Processor
### by Andrew Kramer
#

"""

This program calculates the cost to order pounds of coffee.

"""
### PSEUDOCODE
"""

Define the main function:

- Establish the TAX_RATE constant of .07

- Ask the user to enter how many pounds of coffee they are ordering.

- Calculate the price per pound based off the internal price guide (1-10 pounds, 10-20, 20-30, 30-40).

- Display resulting sub_total price.

- Calculate and display the tax: sub_total * TAX_RATE

- Calculate and display the shipping fee:
    1.00 per pound, but shipping is free if sub_total over 150.00.

- Calculate and display the grand total:
    sub_total + tax + shipping 

"""


def main():

    # Establish TAX_RATE constant.

    TAX_RATE = .07

    # Prompt the user to enter the quantity of pounds.

    pounds = int(input('How many pounds are you ordering? '))

    # Line break

    print()

    # Use the internal price guide with if statements to
    # set the price per pound dependant upon how many pounds

    if pounds >= 40:

        sub_total = pounds * 7.50

    if pounds >= 20 and pounds <= 39:

        sub_total = pounds * 8.75

    if pounds >= 10 and pounds <= 19:

        sub_total = pounds * 10.00

    if pounds >= 1 and pounds <= 9:

        sub_total = pounds * 12.00

    # Display the sub_total

    print(f'Cost of coffee ${sub_total:.2f}')

    # Line break

    print()

    # Calculate the sales tax.

    tax = sub_total * TAX_RATE

    # Display the sales tax.

    print(f'7% sales tax ${tax:.2f}')

    # Line break

    print()

    # Calculate the shipping cost.
    # 1.00 per pound, but if sub_total is over 150.00
    # shipping is free.

    if sub_total <= 150.00:

        shipping = pounds * 1.00

    else:

        shipping = pounds * 0.00

    # Display the shipping fee.

    print(f'Shipping fee ${shipping:.2f}')

    # Line break

    print()

    # Calculate the grand total.

    total = sub_total + tax + shipping

    # Display the grand total.

    print(f'Total payable ${total:.2f}')

main()
