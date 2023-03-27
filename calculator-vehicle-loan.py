### Vehicle Loan Calculator
### by Andrew Kramer
#

"""

This program calculates the monthly payment for a vehicle loan.

"""
### PSEUDOCODE
"""

Define the main function:

- Prompt user to enter vehicle price
- Input vehicle price
- Calculate sales tax with the following equation
- Multiply vehicle price by TAX_RATE of 7% = 0.07
- Display sales tax
- Prompt user to enter trade-in value
- Input trade-in value
- Prompt user to enter cash down
- Input cash down
- Calculate amount financed with the following equation
- Vehicle price plus sales tax minus trade-in value minus cash down
- Display amount financed
- Calculate monthly payment with the following equation
- Amount financed divided by TERM_MONTHS (constant for months)
- Display monthly payment

"""


def main():

# sales tax percent constant

    TAX_RATE = 0.07

# payment term months constant

    TERM_MONTHS = 72

# user is prompted to input vehicle price

    vehicle_Price = float(input('Enter vehicle price: '))

# calculate sales tax

    sales_Tax = (vehicle_Price * TAX_RATE)

# display sales tax

    print(f'Sales tax: ${sales_Tax:,.2f}')

# user is prompted to input trade-in value

    trade_Value = float(input('Enter trade-in value: '))

# user is prompted to input cash down

    cash_Down = float(input('Enter cash down: '))

# calculate amount financed

    amount_Financed = vehicle_Price + sales_Tax - trade_Value - cash_Down

# display amount financed

    print(f'Amount financed: ${amount_Financed:,.2f}')

# calculate monthly payment

    monthly_Payment = (amount_Financed / TERM_MONTHS)

# display monthly payment

    print(f'Monthly payment: ${monthly_Payment:,.2f}') 

main()
