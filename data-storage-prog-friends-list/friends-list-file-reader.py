### Friends List File Reader
### by Andrew Kramer
#

"""

This program reads the friends.txt file, displays the
name and age for each friend within the file, and
displays the average age for all of the friends.

"""
### PSEUDOCODE
"""

Define the main function:

- Open the friends.txt file in read mode.
- Assign the file to the friends_file variable.

- Read the first line of the file and assign it to the friend variable.

- Create an accumulator variable to keep a running total of the ages,
assign it to the ages_sum variable.
- Create a counter variable to keep count of the loop iterations,
assign it to the count variable.

- Create a while loop to read each data line until the next friend data line is blank.
- Read the line after the first line to get the age value, convert it to a float, and assign it to the age variable.
- Remove the new line escape character from the friend variable.
- Display the friends name and age.
- Use the count variable with each iteration
- Use the ages_sum variable with each iteration
- Read the next line which should be the next friend name and
continue the loop.

- Close the file when the loop completes.
- Use the ages_sum and count variables to calculate the average age:
- Average_age = ages_sum / count

- Display the average age of all the friends.

"""


# Define the main function of the program.

def main():

    # Open the friends.txt file in read mode to access the
    # friend data and assign it to the friends_file variable.

    friends_file = open('friends.txt', 'r')

    # Read the first line of friends_file and assign the value to
    # the friend variable.

    friend = friends_file.readline()

    # Establish an accumulator to add the ages and assign it to the
    # ages_sum variable.

    ages_sum = 0.0

    # Establish a counter variable and assign it to the count variable.

    count = 0

    # Establish a while loop to read the next line until a line
    # registers as blank when read.

    while friend != '':

        # Read the line after the friend name line, convert it to a float,
        # and assign the value to the age variable.

        age = int(friends_file.readline())

        # Remove the new line escape character from the friend variable.

        friend = friend.rstrip('\n')

        # Display the friends name and age.

        print(f'My friend {friend} is {age}.')

        # Line break

        print()

        # Add each iteration to the count counter variable.

        count += 1

        # Add the age variable number value to the sum accumulator variable.

        ages_sum += age

        # Read the next line and assign it to the friend variable.

        friend = friends_file.readline()

    # Close the file when the loop completes.

    friends_file.close()

    # Calculate the average age by dividing the ages_sum amount by
    # the count amount and assign the value to the average_age variable.

    average_age = ages_sum / count

    # Display the average age accurate to one decimal place.

    print(f'The average age of my friends is {average_age:.1f}')

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()

