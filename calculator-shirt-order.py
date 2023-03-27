### Shirt Order Processor
### by Andrew Kramer
#

"""

This program asks a user how many shirts they would like to order
and calculates discounts, shipping, and the grand total.

"""
### PSEUDOCODE
"""

Define the main function:

- Establish SHIRT_PRICE constant of 14.95

- Ask the user how many shirts they would like to order.

- Use if statements to calculate if the quantity is # eligible for discounts.

    12 or more shirts = 40% off
    8-11 shirts = 30% off
    4-7 shirts = 20% off

- Use if statement to calculate if shipping is eligible for discounts.

    12 or more shirts = 0.00 per shirt
    1-11 shirts = 1.00 per shirt

- Display shipping.
- Calculate grand total.
- Display grand total.

"""


def main():

    # Establish SHIRT_PRICE constant.

    SHIRT_PRICE = 14.95

    # Prompt the user for quantity of shirts.

    quantity = int(input('How many Orinoco shirts would you like to order? '))

    # Line break

    print()

    # Establish if statements based on quantity discounts.
    # Establish discount variable.
    # Establish sale price variable.

    if quantity >= 12:

        # 40 percent discount for 12 or more shirts.

        discount = SHIRT_PRICE * quantity * 0.4

        sale_price = SHIRT_PRICE * quantity - discount

    if quantity >= 8 and quantity <=11:

        # 30 percent discount for between 8 and 11 shirts.

        discount = SHIRT_PRICE * quantity * 0.3

        sale_price = SHIRT_PRICE * quantity - discount

    if quantity >= 4 and quantity <=7:

        # 20 percent discount for between 4 and 7 shirts.

        discount = SHIRT_PRICE * quantity * 0.2

        sale_price = SHIRT_PRICE * quantity - discount

    # No discount if ordering less than 3 or less shirts.

    if quantity >= 1 and quantity <=3:

        sale_price = SHIRT_PRICE * quantity

    # Display sub-total.

    print(f'Sub-total: ${sale_price:,.2f}')

    # Calculate shipping.

    if quantity <= 11:

        # Shipping cost is 1.00 per shirt if ordering 11 or less shirts.

        shipping = quantity * 1.00

    else:

        # Shipping is 0.00 free per shirt if ordering 12 or more shirts.

        shipping = 0.00

    # Display shipping cost.

    print(f'Shipping charges: ${shipping:,.2f}')

    # Calculate grand total.

    total = sale_price + shipping

    # Display grand total.

    print(f'Total: ${total:,.2f}')

main()
