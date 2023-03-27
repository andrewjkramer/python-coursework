### Payroll Processor
### by Andrew Kramer
#

"""

This program asks the user to enter an employee's name, pay rate, and hours worked in a week. It then calculates their pay, including potential overtime pay, and displays it.

After data for three employee's is entered/processed/displayed, it displays the total sum of all three employee's pay.

"""
### PSEUDOCODE
"""

- Import payrollModule module as payroll for pay calculation functions.

Define the main function:

- Establish accumulator variable.
- Establish for loop with a range of 3 to allow entry and processing of data for 3 employees.

- Within the for loop, call the pay function within the payroll module to process the data and receive the calculated value back from the function.

- Print each data result for each employee
- Print the sum of all employees' pay.


"""


# Import payrollModule module as payroll.

import payrollModule as payroll

# Define the main function of the program.

def main():

    # Establish accumulator variable to add each employee's pay
    # to calculate the total payroll for the week.

    total_payroll = 0.00

    # Establish for range to allow entry for the data of the 3 employees.

    for employees in range(3):

        # Ask the user to enter the employee's name and assign it to the name variable.

        name = input('Enter employee name: ')

        # Ask the user to enter the employee's hourly pay rate and assign it to the hourly_rate variable.

        hourly_rate = float(input(f'Enter hourly rate for {name}: '))

        # Ask the user to enter the employee's quantity of hours for the week and assign it to the week_hours variable.

        week_hours = int(input(f'Enter hours for {name} this week: '))

        # Call the pay function within the payroll module to calculate the pay
        # by passing it the hourly_rate and week_hours arguments and then
        # assigning the returned value to the emp_pay variable.

        emp_pay = payroll.pay(hourly_rate, week_hours)

        # Print the calculated pay for the employee.

        print(f'Pay for {name} is ${emp_pay:.2f}')

        # Use the accumulator variable to keep a running total.

        total_payroll = total_payroll + emp_pay

    # Print the running total for the week.

    print(f'Total payroll for the week is ${total_payroll:,.2f}')

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
