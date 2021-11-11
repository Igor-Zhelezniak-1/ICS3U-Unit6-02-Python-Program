#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program generate random numbers

import random


def largest_number_calculator(random_numbers):
    # This function tells which number is higher

    largest_number = random_numbers[0]
    for loop_counter in range(0, len(random_numbers)):
        if largest_number < random_numbers[loop_counter]:
            largest_number = random_numbers[loop_counter]
        else:
            pass

    return largest_number


def main():
    # this function generate random numbers
    random_numbers = []
    print("Starting ...\n")
    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(-100, 100)  # a number between 0 and 100
        random_numbers.append(random_number)
        print(
            "The random number {0} is: {1}".format(
                loop_counter + 1, random_numbers[loop_counter]
            )
        )
    largest_number = largest_number_calculator(random_numbers)
    print("\nThe largest number is {0}".format(largest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
