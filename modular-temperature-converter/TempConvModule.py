### Temperature Converter Module
### by Andrew Kramer
#

"""

This module includes functions that perform conversion formula processes for temperatures.

This module can also run as a standalone program to test
the conversion formulas within the functions.

Functions include:

   c_to_f    |   Celsius to Fahrenheit (void - does not return value)

   f_to_c    |   Fahrenheit to Celsius (value-returning)

"""


# Define c_to_f function. Converts Celsius to Fahrenheit.

def c_to_f(ctemp):

    # Convert Celsius to Fahrenheit and assign the converted value to ftemp variable.

    ftemp = (ctemp * 9/5) + 32

    # Print original argument aka parameter and converted value.

    print(f'{ctemp} Celsius is {ftemp:.1f} Fahrenheit')

# Define f_to_c function. Converts Fahrenheit to Celsius.

def f_to_c(ftemp):

    # Convert Fahrenheit to Celsius and assign the converted value to ctemp variable.

    ctemp = (ftemp - 32) * 5/9

    # Return the converted value to the program.

    return ctemp

# Define the main function of the program.
#
# Use the main function to test the internal
# formulas of the custom functions
# above without needing to import this
# module into a program.

def main():

    # Ask the user to input a temperature and assign it to the temp variable.

    temp = int(input('Enter a temperature: '))

    # Ask the user if the inputted temperature uses Fahrenheit or Celsius and
    # assign it to the convert variable.

    convert = (input('To convert to F enter "f" to convert to C enter "c": '))

    # Establish if statement if the convert variable is equal to 'f'

    if convert == 'f':

        # Convert the original temperature to Celsius.

        temp_converted = (temp - 32) * 5/9

        # Print the converted temperature.

        print(f'{temp_converted:.1f}')

    # Establish else statement if the convert variable is equal to anything but 'f'
    # less code for testing purposes, but any inputs other than 'f' will run this.

    else:

        # Convert the original temperature to Fahrenheit.

        temp_converted = (temp * 9/5) + 32

        # Print the converted temperature.

        print(f'{temp_converted:.1f}')

# Call the main function ONLY if the file is being run as
# a standalone program.

if __name__ == '__main__':

    main()
