### Solar System Quiz
### by Andrew Kramer
#

"""

This program is a three question quiz about our solar system!

"""
### PSEUDOCODE
"""

Define the main function:

- Ask the user to answer the first question.
- Use if clause to verify if they answered correctly.
- If they answered correctly, display positive message.
- Use an else clause so if they answered incorrectly, display dismal message.

- Ask the user to answer the second question.
- Use if clause to verify if they answered correctly.
- If they answered correctly, display positive message.
- Use an else clause so if they answered incorrectly, display dismal message.

- Ask the user to answer the third question.
- Use if clause to verify if they answered correctly.
- If they answered correctly, display positive message.
- Use an else clause so if they answered incorrectly, display dismal message.

- Display a thank you message after all the third and final result.

"""


def main():

    # Ask the first quiz question.

    q1 = input('Who was the first astronaut on the moon? ')

    # Verify if the answer is correct.

    if q1 == 'Neil' or q1 == 'Armstrong' or q1 == 'Neil Armstrong':

        # Line break

        print()

        # Display congratulatory message.

        print('Yes! To the moon!')

        # Line break

        print()

    # If answer is wrong use else clause.

    else:

        # Line break
        
        print()

        # Display disappointing message.

        print("Wrong answer... I'll write that answer an ORBIT-tuary, haha!")

        # Line break

        print()

    # Ask the second quiz question.

    q2 = input('What is the name of our galaxy? ')

    # Verify if the answer is correct.

    if q2 == 'Milky Way' or q2 == 'Milky Way Galaxy' or q2 == 'The Milky Way Galaxy':

        # Line break

        print()

        # Display congratulatory message.

        print('Woo! Your answer is out of this world!')

        # Line break

        print()

    # If answer is wrong use else clause.

    else:

        # Line break

        print()

        # Display disappointing message.

        print("Wrong answer... I'll write that answer an ORBIT-tuary, haha!")

        # Line break

        print()

    # Ask the third quiz question.

    q3 = int(input('What year was Pluto discovered? '))

    # Verify if the answer is correct.

    if q3 == 1930:

        # Line break

        print()

        # Display congratulatory message.

        print('.....calculating')
        print('...............calculating')
        print(".........................YOU'RE RIGHT!")

        # Line break

        print()

    # If answer is wrong use else clause.

    else:

        # Line break

        print()

        # Display disappointing message.

        print("Wrong answer... I'll write that answer an ORBIT-tuary, haha!")

        # Line break

        print()

    # Display thank you message.

    print('Thanks for playing!')

main()
