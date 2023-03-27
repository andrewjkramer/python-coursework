### Advanced Random Number Generator List Manipulator
### by Andrew Kramer
#

"""

This program generates 50 random numbers and stores them in a list, among other things...

This program destroys your brain, hahaha!

"""
### PSEUDOCODE
"""

- Import the random module as r.

Define the main function:

- Create an empty list named x_list.

- Establish a for loop to generate 50 random numbers.
- Add each generated number to the x_list list.

- Sort the x_list list in ascending order and display each number on a single line.

- Display the 5th to 10th elements within the x_list list - use slice.
- Display the final 5 elements within the x_list list - use slice.

- Call the custom sev function, passing the x_list list as an argument, assigned the returned value to the sevens_list list variable.

Define the sev function:

- Create an empty list  named sev_list.

- Establish a for loop to isolate only the numbers that end in 7 from within the passed argument x_list list.

- Append the numbers that end in 7 to the sev_list list.

- Return the sev_list list value to the main function.

Define the main function post sev_list value return:

- Sev_list value is returned to main and assigned to sevens_list list variable.

- Display the quantity of elements within the sevens_list list.

- Establish if & else clauses regarding number 207:
- If 207 is in the sevens_list list, display message stating this.
- Else, add 207 to the list, display message stating this.

- Establish if & else clauses regarding number 247:
- If 247 is in the sevens_list list, display message stating this, and report its index value.
- Else, add 247 to the list, display message stating this.

- Display the numbers within the sevens_list list on a single line.

- Establish an accumulator variable and for loop to add the numbers within the sevens_list and report their sum in a message.

"""

# Import the random module as r.

import random as r

# Define the main function of the program.

def main():

    # Create an empty list named x_list

    x_list = []

    # Display pre-text
    
    print('Here is the complete list of 50 elements, sorted low to high...')

    # Line break.

    print()

    # Establish a for loop to generate 50 random numbers.

    for index in range(50):

        # Use the random function to generate numbers from 200 to 250
        # and add them to the x_list list.

        x_list.append(r.randint(200,250))

        # Sort the x_list list in ascending order.

        x_list.sort()

    # Establish a for loop to display the x_list list.

    for index in x_list:

        # Display the x_list list elements on a single line
        # and separated by a single space.

        print(index, end = ' ')

    # Line break.

    print()

    # Line break.

    print()

    # Display the numbers at the index values of 5-10 within the x_list list
    # by using a slice.

    print(f'Elements indexed 5 to 10 in the sorted list are', x_list[5:11])

    # Line break.

    print()

    # Display the numbers at the index values of the final 5 elements
    # within the x_list list by using a slice.

    print(f'The final 5 elements in the sorted list are', x_list[-5:])

    # Line break.

    print()

    # Call the sev function, passing the x_list list as an argument,
    # and have the returned value assigned to the sevens_list variable.

    sevens_list = sev(x_list)

    # Display the quantity of numbers that end with a 7 within the sevens_list list.

    print(f'Number of elements ending with 7:', len(sevens_list))

    # Line break.

    print()

    # Establish if clause to take course of action if 207 is already in the
    # sevens_list list.

    if 207 in sevens_list:

        # Display message if 207 was already present within the sevens_list list.

        print(f'207 was already in the "sevens" list, so nothing was added.')

        # Line break.

        print()

    # Establish else clause if 207 was not present within the sevens_list list.

    else:

        # Add 207 via insert to the front of the sevens_list list.

        sevens_list.insert(0,207)

        # Display message if 207 was not present, but that it was added to the
        # sevens_list list.

        print(f'207 was not found so it was added to the start of the "sevens" list.')

        # Line break.

        print()

    # Establish if clause to take course of action if 247 is already in the
    # sevens_list list.

    if 247 in sevens_list:

        # Display message if 247 was already present within the sevens_list list,
        # and include it's index location.

        print(f'247 was already in the "sevens" list, at index {sevens_list.index(247)}, so nothing was added.')

        # Line break.

        print()

    # Establish else clause if 247 was not present within the sevens_list list.

    else:

        # Add 247 via append to the end of the sevens_list list.

        sevens_list.append(247)

        # Display message if 247 was not present, but that it was added to the
        # sevens_list list.

        print(f'247 was not found so it was added to the end of the "sevens" list.')

        # Line break.

        print()

    # Display the index of the sevens_list list.

    print('Here are the elements in the "sevens" list...')

    # Line break.

    print()

    # Establish a for loop to display the sevens_list list.

    for index in sevens_list:

        # Display the sevens_list list elements on a single line
        # and separated by a single space.

        print(index, end = ' ')

    # Line break.

    print()

    # Establish an accumulator variable named total.

    total = 0

    # Establish a for loop to total the numbers within the sevens_list list.

    for num in sevens_list:

        # Add each number to the total for each iteration.

        total += num

    # Line break.

    print()

    # x

    print(f'The total of all elements in the "sevens" list is {total}')

    # Line break.

    print()

# Define the sev function and pass the x_list to it as
# an argument

def sev(x_list):

    # Create an empty list named sev_list.

    sev_list = []

    # Establish a for loop to iterate over the elements contained within the
    # x_list argument.

    for num in x_list:

        # Establish if clause to determine which elements within the x_list
        # argument end with the number 7.

        if num == 207 or num == 217 or num == 227 or num == 237 or num == 247:

            # Append only the numbers that end with the number 7 to the sev_list list.

            sev_list.append(num)

    # Return the sev_list value to the main function.

    return sev_list

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
