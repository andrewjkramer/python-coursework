### Seconds to Minutes Converter
### by Andrew Kramer
#

"""

This program asks the user to enter a time in seconds, converts the time to minutes and seconds, and displays the result.

"""
### PSEUDOCODE
"""

Define the main function:

- Prompt user to enter time as seconds
- Input time as total seconds

- Convert total seconds into minutes and seconds with the following equation
    Divide total seconds by 60 to establish minutes
    Calculate remainder of total seconds divided by 60 to establish seconds

- Display result with entered total seconds and calculated time with minutes and seconds in this format - xxx seconds is xx minutes, xx seconds

"""


def main():

# conversion formula constant

    TIME_FORMULA = 60

 # user is prompted to input seconds

    total_Seconds = int(input('Enter the time period in seconds: '))

# establish x_Minutes variable by dividing seconds by formula and that result by the formula once again

    x_Minutes = (total_Seconds // TIME_FORMULA ) % TIME_FORMULA

# establish seconds by calculating remainder of total_seconds

    x_Seconds = total_Seconds % TIME_FORMULA

# display calculated result

    print(f'{total_Seconds} seconds is {x_Minutes} minutes, {x_Seconds} seconds.') 

main()
