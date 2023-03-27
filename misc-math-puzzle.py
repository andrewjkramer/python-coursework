### Math Puzzle
### by Andrew Kramer
#

"""

This program asks a user to solve the following math question:

Enter an odd multiple of 29 that is less than 300 and greater than 150.

It lets them know if they were correct and displays the factor of that multiple.

"""
### PSEUDOCODE
"""

Define the main function:

- Ask the user to enter their answer for the math question (stated above in program info)

- Verify the answer: 203 or 261

- If the answer matches, inform the user with a message and calculate and display the factor for the multiple they entered.

- To calculate the factor use the following equation:
    Multiple divided by 29 (use // for the division to
    get whole number result.

- If the answer does not match, inform the user with an alternate message.

"""


def main():

    # Ask the user to enter a correct answer for the question.

    multiple = int(input('Enter an odd multiple of 29 that is ' +
              'less than 300 and greater than 150: '))

    # Line break

    print()

    # Verify the answer against the two possible answers.

    if multiple == 203 or multiple == 261:

        # Calculate the factor of the multiple by dividing
        # the multiple by 29.

        factor = multiple // 29

        # Display if the user answered correctly.

        print('Good input.')

        # Line break

        print()

        # Display the calculated factor.
        
        print(f'The other factor of {multiple} is {factor}.')

    # If the user answered incorrectly, let them know.

    else:

        # Display if the user answered incorrectly.

        print('Bad input.')

main()
