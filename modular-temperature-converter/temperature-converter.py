### Temperature Converter
### by Andrew Kramer
#

"""

This program asks the user to enter a temperature, which temperature scale the temperature uses, converts the temperature from the scale into the opposite scale, and displays the result.

"""
### PSEUDOCODE
"""
Import TempConvModule module as temps for temperature conversion functions.

Define the main function:

- Ask the user to enter a temperature the input to a temp variable.
- Ask the user which temperature scale the inputted temperature uses
and assign it to temp_scale variable.

- If the temperature scale is Fahrenheit, call the f_to_c value-returning function and print the original F temperature with the returned C temperature conversion value.

- Else if the temperature scale is Celsius, call the c_to_f void function which prints the original C temperature with the F temperature conversion value.

"""


# Import TempConvModule module as temps.

import TempConvModule as temps

# Define the main function of the program.

def main():

    # Ask the user to input a temperature and assign it to the temp variable.

    temp = int(input('Enter a temperature: '))

    # Ask the user if the inputted temperature uses Fahrenheit or Celsius and
    # assign it to the temp_scale variable.

    temp_scale = input('Was that input Fahrenheit (f) or Celsius (c)? ')

    # Establish if statement if the temp_scale is equal to Fahrenheit

    if (temp_scale == 'Fahrenheit'
        or temp_scale == 'fahrenheit'
        or temp_scale == 'F'
        or temp_scale == 'f'):

        # Call f_to_c function passing the temp variable as an argument,
        # and assign the returned value to temp_converted variable.

        temp_converted = temps.f_to_c(temp)

        # Print the original temperature entered with the converted temperature.

        print(f'{temp} Fahrenheit equals {temp_converted:.1f} Celsius')

    # Establish else if statement if the temp_scale is equal to Celsius

    elif (temp_scale == 'Celsius'
        or temp_scale == 'celsius'
        or temp_scale == 'C'
        or temp_scale == 'c'):

        # Call the c_to_f function passing the temp variable an an argument.

        temps.c_to_f(temp)

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
