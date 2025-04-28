#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if the user enters the correct random number using a break statement
import random


def main():
    # Step 0: Import random module
    # This is already done at the top of the code

    # Step 1: GET user_num_str
    user_num_str = input("Enter a number between 0 and 9: ")

    # Step 2: GENERATE chosen_number (0-9)
    chosen_number = random.randint(0, 9)

    # Step 3: TRY user_num_str
    try:
        # Step 4: Check if user_num_str is equal to chosen_number
        user_num = int(user_num_str)  # Convert input to integer
        if user_num == chosen_number:
            print("You guessed right!")
        elif user_num > 9 or user_num < 0:
            print(f"Enter number within 0-9!")
        else:
            print(f"Try one more time! The number was {chosen_number}.")
    except ValueError:
        # Step 5: EXCEPT Invalid input
        print(f"Error. You entered {user_num_str}. Please enter an integer.")


if __name__ == "__main__":
    main()
