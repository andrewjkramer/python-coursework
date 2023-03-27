### State Capitals Dictionary Creator
### by Andrew Kramer
#

"""

# This program creates a dictionary to add and display the capital cities of states & then does some funky math LOL

"""
### PSEUDOCODE
"""

Define the main function:

- Create a dictionary with 4 states and their capital cities.

- Display the quantity of states(keys) currently in the dictionary.

- Ask the user to input a state abbrev. to add more states(keys) to the dictionary.

- If the state(key) is already in the dictionary, report as such, and ask for another abbrev. entry for the state(key)

- Assign their input to the key variable.

- Establish a while loop to continue adding states and capital cities unless the user presses enter.

- Ask the user to input the state capital of the previously entered state and assign the capital to the value variable.

- Ask the user to input a state abbrev. to add more states(keys) to the dictionary.
- If the state(key) is already in the dictionary, report as such with it's capital city, and ask for another abbrev. entry for the state(key)

- To check if the state(key) is already in the dictionary, use IF IN and IF NOT IN clauses and take appropriate action - report the already existing state & it's capital, and ask for new input / or add the current input to the dictionary if it doesn't already exist.

- Upon exiting the loop, report the quantity of states(keys) currently in the dictionary.
- Use a for loop to display the states and their capital cities.

- Display a message that it's time for math!

- Use a dictionary comprehension to get the cubes of only odd numbers from the range of 1-10.
- Use a for loop to display the numbers and their cubes.

############################################################

- Realize you forgot to include this within the while loop: 

- If the state entered is already in the dictionary, report its capital.

- Use the get function to get more caffeine so you can figure out that devious while loop!

"""


# Define the main function of the program.

def main():

    # Create a dictionary with 4 states and their capital cities.

    statecapitals = {'FL': 'Tallahassee', 'TX': 'Austin', 'CA': 'Sacramento', 'MI': 'Lansing'}

    # Use the len function to determine the quantity of keys in the
    # dictionary and assign to a variable named count.

    count = len(statecapitals)

    # Display the quantity of keys in the dictionary by using the
    # variable named count.

    print(f'{count} states are in the dictionary.')

    # Line break.

    print()

    # Display a message.

    print("Let's add a few more.")

    # Line break.

    print()

    # Ask the user to enter a state to add to the dictionary or
    # press enter to "quit," assign the state abbrev. to the variable named key.

    key = input('Enter state abbrev. or Enter to quit: ')

    # Line break.

    print()
    
    # Establish while loop to continue data entry unless
    # the user presses enter for the key variable input.

    while key != '':

        # Establish if in clause if the state(key) is in already in the dictionary named statecapitals.

        if key in statecapitals:

            # Display the key-value pair that already exists in the dictionary named statecapitals.

            print(f'Already have {key}, capital is {statecapitals[key]}.')

            # Line break.

            print()

            # Ask the user to enter a state to add to the dictionary or
            # press enter to "quit," assign the state abbrev. to the variable named key.

            key = input('Enter state abbrev. or Enter to quit: ')

            # Line Break.

            print()

        # Establish if not in clause if the state(key) is not in the dictionary named statecapitals.

        if key not in statecapitals and key != '': 

            # Ask the user to input the state capital of the state assigned # to the key variable and assign the capital to the variable named value.

            value = input(f'Enter state capital of {key}: ')

            # Line break.

            print()

            # Add the key and its value to the dictionary named statecapitals.

            statecapitals[key] = value

            # Continue the while loop by asking for the next state abbrev.
            # or bypass it and end the loop if the user presses enter.

            key = input('Enter state abbrev. or Enter to quit: ')

            # Line break.

            print()

    # Use the len function to determine the quantity of keys in the
    # dictionary and assign to a variable named count.

    count = len(statecapitals)

    # Display the quantity of keys in the dictionary by using the
    # variable named count.

    print(f'Got {count} states now. Here they are...')

    # Line break.

    print()

    # Establish for loop to print the dictionary named statecapitals

    for key, value in statecapitals.items():

        # Display the capital cities of each state. The state is
        # assigned to the key "variable" and the capital city is 
        # assigned to the value "variable" elements within the
        # statecapitals dictionary.

        print(f'The capital of {key} is {value}')

        # Line break.

        print()

    # Time for math! Just because... LOL

    print('Some cubes made with a dictionary comprehension...')

    # Line break.

    print()

    # Let the computer do the thinking for you.. use dictionary 
    # comprehension to make a list with only odd numbers in the range 
    # of 1-10 or 1-9... found a formula to stick in there to retrieve 
    # only odd numbers thanks to Google!

    cubes = {x:x**3 for x in range(1,10) if x % 2 != 0}

    # Establish for loop to print the new dictionary named cubes.

    for x in cubes:

        # Display the key-value pairs of the dictionary named cubes.

        print(f'{x} cubed is {cubes[x]}')

        # Line break.

        print()

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
