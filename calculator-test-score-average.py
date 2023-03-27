### Test Score Average Calculator
### by Andrew Kramer
#

"""

This program calculates the average of three test scores.

"""
### PSEUDOCODE
"""

Define the main function:

- Prompt user for three test scores - score_a score_b score_c
- Input three test scores - score_a score_b score_c

- Calculate average of three test scores using the following equations
    Add score_a score_b score_c
    Divide result by 3 

- Display average as a percentage with two decimals

"""


def main():

    score_a = int(input('Enter the first test score (0-100): '))  # get 1st test score

    score_b = int(input('Enter the second test score (0-100): ')) # get 2nd test score

    score_c = int(input('Enter the third test score (0-100): '))  # get 3rd test score

    average = (score_a + score_b + score_c) / 3                   # calculate average of 3 test scores

    print(f'The average test score is {average:.2f}%')            # display calculated average as a percentage

main()
