### Table of Squares and Cubes Generator
### by Andrew Kramer
#

"""

This is a program that uses a for loop to process integers from 5 to 50 in increments of 5.

It displays the square and cube of each integer in a table.

"""
### PSEUDOCODE
"""

Define the main function:

- Display column headings: INTS, SQUARES, CUBES

- Establish the range of numbers that will be processed to display their squares and cubes.

- Use numbers 5 through 50, and increment them by 5.

- Process the numbers using the range in a for loop.

- Display the integers and their square and cube results into the table.

- Make sure the table headings and related values are lined up neatly, and use commas for any value over 1000.

"""


def main():

# Display column headings.

    print(f'{"INTS":^7}{"SQUARES":>8}{"CUBES":>12}')

# Process integers 5 to 50 in increments of 5 with range function
# and display the results.

    for num in range(5,51,5):                       # Establish the number range to process.
        
        square = num**2                             # Square formula
        
        cube = num**3                               # Cube formula
        
        print(f'{num:^7}{square:>8,}{cube:>12,}')   # Display the results into the table.
 
main()
