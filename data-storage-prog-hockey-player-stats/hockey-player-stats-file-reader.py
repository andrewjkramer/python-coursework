### Hockey Player Stats File Reader
### by Andrew Kramer
#

"""

This program reads the player stats from the lightningStats.txt file
and displays a table with each player's name, goals, assists, and total points.

It displays the top scorer with their total points under the table.

"""
### PSEUDOCODE
"""

Define the main function:

- Open the lightningStats.txt file in read mode, wherein the data will be read from.

- Establish a points variable set to 0 to use to assign a player's total points, to later determine the top scorer.

- Print the table column headings: PLAYER GOALS ASSISTS TOTAL
- Format the headings with spacing and alignment.

- Read the first line of the lightning_stats file and assign the value to the player_name variable.

- Establish a while loop to read each following line until a line registers as blank when read.
- Read the next line, convert it to an integer, and assign it to the goals variable.
- Read the next line, convert it to an integer, and assign it to the assists variable.
- Calculate the player's total points by adding their goals and assists, # and assign the sum to the points variable.
- Remove the new line escape character from the player_name variable so all the data displays on the same line.
- Display the player's name and their stats variable with spacing and alignment format to match the column headings.

- Use an if statement to determine if that player's point total are greater than what is currently assigned as a value to the total_points variable. If they are, assign that value to total_points, and assign the player's name to the top_scorer variable.

- Read the next player's name and continue the loop.

- Close the file when the loop completes.

- Once all player's stats have been displayed, display the top scorer and their points.

"""


# Define the main function of the program.

def main():

    # Open file lightningStats.txt in read 'r' mode
    # and assign to lightning_stats variable.

    lightning_stats = open('lightningStats.txt', 'r')

    # Variable to determine the top scorer's total points.

    total_points = 0

    # Print the table column headings.

    print(f'{"PLAYER":<10}{"GOALS":^6}{"ASSISTS":^8}{"TOTAL":^6}')

    # Read the first line of lightning_stats file and assign the value
    # to the player_name variable.

    player_name = lightning_stats.readline()

    # Establish a while loop to read the next line until a line
    # registers as blank when read.

    while player_name != '':

        # Read the line after the player's name line, convert it to an integer,
        # and assign the value to the goals variable.

        goals = int(lightning_stats.readline())

        # Read the line after the goal's line, convert it to an integer,
        # and assign the value to the assists variable.

        assists = int(lightning_stats.readline())

        # Calculate the player's total points by adding the goals and assists variables,
        # and assign the sum to the points variable.

        points = goals + assists

        # Remove the new line escape character from the player's name so the data falls onto one line.

        player_name = player_name.rstrip('\n')

        # Displays the player's name and their stats on one line aligned with the column headings.

        print(f'{player_name:<10}{goals:^6}{assists:^8}{points:^6}')

        # Use an if statement to calculate if the player's points are the highest yet,
        # and if so, assign the total_points variable to that value.

        if points > total_points:

            # Assign the player's points to the total_points variable.

            total_points = points

            # Assign the associated player's name to the top_scorer variable.

            top_scorer = player_name

        # Read the next line and add it to the player_name variable as the loop continues.

        player_name = lightning_stats.readline()

    # Close the file.

    lightning_stats.close()

    # Display the top scorer with their total points.

    print(f'{top_scorer} is the top scorer with {total_points} points.')

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
