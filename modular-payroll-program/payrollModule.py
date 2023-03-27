### Payroll Module
### by Andrew Kramer
#

"""

- This module includes functions that perform
- processes for calculating employee pay.

- This module can also run as a standalone program to test
- the conversion formulas within the functions.

- Functions include:

    pay   |   calculates pay with or without overtime rate

"""


# Define pay function. 

def pay(rate, hours):

    # Establish if statement if the employee has more than 40 hours.

    if hours > 40:

        # Calculate the pay for the overtime hours and add it to the base hourly pay.

        calculated_pay = (hours - 40) * (rate * 1.5) + (40 * rate)

    # Establish else statement if the employee has 40 hours or less.

    else:

        # Calculate the pay at the normal pay rate.

        calculated_pay = rate * hours

    # Return the calculated_pay variable value back to the program.

    return calculated_pay

# Define the main function of the program.
#
# Use the main function to test the internal
# formulas of the custom functions
# above without needing to import this
# module into a program.

def main():

    # Ask the user to input the pay rate.

    rate = float(input('Enter hourly rate: '))

    # Ask the user to input the hours.

    hours = int(input('Enter hours: '))

    # Establish if statement if the employee has more than 40 hours.

    if hours > 40:

        # Calculate the pay for the overtime hours and add it to the base hourly pay.

        calculated_pay = (hours - 40) * (rate * 1.5) + (40 * rate)

        # Print the result.

        print(calculated_pay)

    # Establish else statement if the employee has 40 hours or less.

    else:

        # Calculate the pay at the normal pay rate.

        calculated_pay = rate * hours

        # Print the result.

        print(calculated_pay)

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
