### Random Number Generator List Manipulator
### by Andrew Kramer
#

"""

This program does crazy things with RNG and lists.

"""
### PSEUDOCODE
"""

Define the main function:

- Create an empty list named num_list.

- Establish a for loop to generate 12 random numbers
- Add each generated number to the num_list list.

- Display each number on a single line.

- Display the 4th element within the num_list list.
- Display the 9th element within the num_list list.
- Display the smallest element within the num_list list.

- Call the change_list function, passing the num_list list argument assign the returned value to to the new_list list variable.

Define the change_list function:

- Slice the middle 6 elements from the argument list and assign them to a new list named c_list.

- Sort the c_list list.

- Display the quantity of elements of the c_list list.

- Return the value to the main function new_list list variable.

- Display the new_list list as a sorted list.

"""


# Define the random module as r.

import random as r

# Define the main function of the program.

def main():

    # Create an empty list named num_list.

    num_list = []

    # Display pre-text.

    print('Here is the list of random integers...')

    # Line break.

    print()

    # Establish for loop to generate 12 random numbers.

    for index in range(12):

        # Establish num variable using randint function
        # to generate numbers between 50 & 100.

        num = r.randint(50,100)

        # Add each generated number to the num_list list.

        num_list.append(num)

    # Establish list_size variable to setup for loop range value.

    list_size = len(num_list)

    # Establish for loop to display the num_list list.

    for index in range(list_size):

        # Display the num_list list elements on a single line
        # and separated by a single space.

        print(num_list[index], end = ' ')

    # Line break.

    print()

    # Line break.

    print()

    # Display the element at the 4th index in the num_list list.

    print(f'The 4th element in the list is {num_list[3]}.')

    # Line break.

    print()

    # Display the element at the 9th index within the num_list list.

    print(f'The element at index 9 is {num_list[9]}.')

    # Line break.

    print()

    # Display the smallest value element in num_list list.

    print(f'The smallest element in the list is {min(num_list)}.')

    # Line break.

    print()

    # Call the change_list function, passing the num_list list as
    # an argument, and have the returned value assigned to the
    # new_list variable.

    new_list = change_list(num_list)

    # Line break.

    print()

    # Display pre-text.

    print('change_list returned this sorted list...')

    # Line break.

    print()

    # Establish for loop to display the new_list list.

    for index in range(len(new_list)):

        # Display the new_list elements on one line,
        # separated by single spaces.

        print(new_list[index], end = ' ')

# Define the change_list function and pass the num_list list to it as
# an argument

def change_list(num_list):

    # Slice the middle 6 elements from the unsorted list.

    c_list = num_list[3:9]

    # Sort the list in ascending order.

    c_list.sort()

    # Display the quantity of elements within the list.

    print(f'The size of the list is now {len(c_list)}.')

    # Return the c_list value to the main function.

    return c_list

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
