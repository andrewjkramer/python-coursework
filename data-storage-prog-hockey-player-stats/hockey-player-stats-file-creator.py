### Hockey Player Stats File Creator
### by Andrew Kramer
#

"""

This program asks the user to enter a hockey player's name, their amount of goals and assists, and saves the data to a file.

"""
### PSEUDOCODE
"""

Define the main function:

- Open the lightningStats.txt file in write or append mode, wherein the data will be saved.

- Establish a priming input variable to control the while loop:
- Ask the user for the player's name and assign it to the player_name variable.
- If the user presses Enter to quit, display a message asking them to exit the program.
- Otherwise continue to the while loop.

- While the player_name input is not equal to '' aka Enter:
- Ask the user for the player's total goals and assign it to the goals variable.
- Ask the user for the player's total assists and assign it to the assists variable.
- Write the player's name to the lightning_stats file.
- Write the player's goals to the lightning_stats file.
- Write the player's assists to the lightning_stats file.
- Continue the loop by asking the player to press Enter or enter another player's name and assign it to the player_name variable.

- When the user has pressed Enter to indicate they are done:
- Close the file.

"""


# Define the main function of the program.

def main():

    # Open file lightningStats.txt in write 'w' or append 'a' mode
    # and assign to lightning_stats variable.

    lightning_stats = open('lightningStats.txt', 'w')

    # Priming input for the while loop, using the name variable.
    # Ask the user to input the players's name.

    player_name = input('Input player name or Enter to quit: ')

    # If statement if the user inputs Enter to quit upon first entry.

    if player_name == '':

        # For loop so the user has to input Enter 100 times
        # since we don't know about the exit or quit functions yet :-)

        for count in range(100):

            # Line break

            print()

            # Display message to user to exit the program.

            print('Please exit the program.')

            # Keep pressing enter... :-)

            input()

    # While loop to allow for continuous player data entry unless the user inputs Enter.

    while player_name != '':

        # Ask the user to input the player's total of goals.

        goals = int(input(f'Enter goals scored by {player_name}: '))

        # Ask the user to input the player's total of assists.

        assists = int(input('Enter assists score by this player: '))

        # Write the player's name to the lightning_stats.txt

        lightning_stats.write(f'{player_name}\n')

        # Write the player's goals total to lightning_stats.txt

        lightning_stats.write(f'{goals}\n')

        # Write the player's assists total to the lightning_stats.txt

        lightning_stats.write(f'{assists}\n')

        # Continuation input variable for the while loop.

        player_name = input('Input player name or Enter to quit: ')

    # Close the file.

    lightning_stats.close()

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
