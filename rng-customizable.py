### Customizable Random Number Generator
### by Andrew Kramer
#

"""

This program asks a user how many random numbers they would like 
to generate. They also provide a low and high range to generate 
numbers within. The program displays however many random numbers 
and also calculates the sum of all of them and displays it.

"""
### PSEUDOCODE
"""

- Import the random module to generate random numbers.

Define the main function:

- Ask the user how many numbers they want to generate - assign to quantity variable
- Ask the user for the lowest number for the generator range - assign to low_num variable
- Ask the user for the highest number for the generator range - assign to high_num variable

- Call the rando_gen function, pass the variables as arguments
    rando_gen returns sum - assign to total_num variable
    rando_gen returns quantity - assign to quan variable
- Print the quan variable and the sum of the random numbers.

Define the rando_gen function:

- Establish an accumulator to keep a running sum of the random numbers - assign to total variable
- Establish a for loop that will run as many times as the entered quantity - aka quan

- Use the randint function to generate the random numbers within the chosen range set with local variable low,high.

- Print each random number on the same line.

- Upon completion of the range, return the running total value aka total and the quantity of numbers to the main function.

"""


# Import the random module.

import random

# Define the main function of the program.

def main():

    # Ask the user how many random numbers they want to generate
    # and assign to the quantity variable.

    quantity = int(input('How many random #s are desired? '))

    # Ask the user for the lowest number to generate the numbers between
    # and assign it to the low_num variable.

    low_num = int(input('Enter the lowest random #? '))

    # Ask the user for the highest number to generate the numbers between
    # and assign it to the high_num variable.

    high_num = int(input('Enter the highest random #? '))

    # Call the rando_gen function and pass the arguments of quantity,low_num,high_num
    # and assign the returned results to the total_num and quan variables.

    total_num, quan = rando_gen(quantity,low_num,high_num)

    # Line break so the next print function does not print next to the random numbers.

    print()

    # Display the entered quantity of numbers as well as their sum.

    print(f'The sum of those {quan} #s is {total_num}')

# Define the rando_gen function of the program. It uses the quantity, low_num, high_num
# variables as parameters named quan,low,high.

def rando_gen(quan,low,high):

    # Establish an accumulator variable for the for loop.

    total = 0

    # Establish a for loop with a range of the quan local variable. 

    for num in range(quan):

            # Call the randint function with a range established with
            # the local low,high variables and assign the generated int
            # to the rando_num local variable.

            rando_num = (random.randint(low,high))

            # Use the accumulator variable to keep a running total.

            total = total + rando_num

            # Print each randomly generated int on a single line.

            print(rando_num,'', end='')

    # Return the total sum of all the randomly generated ints back to the main function.

    return total, quan

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
