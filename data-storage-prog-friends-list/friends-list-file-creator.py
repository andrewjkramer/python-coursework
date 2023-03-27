### Friends List File Creator
### by Andrew Kramer
#

"""

This program asks a user to enter their friends' names and ages.
It allows for unlimited data entry through the deployment of a
while loop. Once the user has entered all of their data, the loop
closes and saves the data to a file.

"""
### PSEUDOCODE
"""

Define the main function:

- Open the Friends.txt file in write or append mode, wherein the data will be saved.

- Establish a priming input variable to control the while loop:
- Ask the user for their friend's name and assign it to the name variable.
- If the user presses Enter to quit, display a message asking them to exit the program.
- Otherwise continue to the while loop.

- While the name input is not equal to '' aka Enter:
- Ask the user for their friend's age and assign it to the age variable.
- Write the friend's name to the friends.txt file.
- Write the friend's age to the friends.txt file.

- When the user has pressed Enter to indicate they are done:
- Close the file and display a message to the user
that the file was created.

"""


# Define the main function of the program.

def main():

    # Open file friends.txt in append mode and assign to friends_file variable.

    friends_file = open('friends.txt', 'w')

    # Priming input for the while loop, using the name variable.
    # Ask the user to input the friend's name.

    name = input('Enter the first name of the friend or Enter to quit: ')

    # If statement if the user inputs Enter to quit upon first entry.

    if name == '':

        # For loop so the user has to input Enter 100 times until it says 'File was created.',
        # since we don't know about the exit or quit functions yet :-)

        for count in range(100):

            # Line break

            print()

            # Display message to user to exit the program.

            print('Please exit the program.')

            # Keep pressing enter... :-)

            input()

    # While loop to allow for continuous friend data entry unless the user inputs Enter.

    while name != '':

        # Ask the user to input the friend's age.

        age = int(input('Enter the age (integer) of this friend: '))

        # Line break

        print()

        # Write the friend's name to friends.txt

        friends_file.write(f'{name}\n')

        # Write the friend's age to friends.txt

        friends_file.write(f'{age}\n')

        # Continuation input variable for the while loop.

        name = input('Enter the first name of the friend or Enter to quit: ')

    # Close the file.

    friends_file.close()

    # Line break

    print()

    # Display message to user that the file was successfully created/saved.

    print('File was created.')


# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
