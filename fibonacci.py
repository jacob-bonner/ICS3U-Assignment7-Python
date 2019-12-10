#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: December 2019
# This program calculates the first 100 fibonacci sequences


def calculate():
    # This function calculates the first 100 fibonacci sequences

    # Variables and lists
    first = 1
    second = 0
    fibonacci_list = []

    # Process
    for counter in range(100):
        answer = first + second
        fibonacci_list.append(answer)
        first = second
        second = answer
    return fibonacci_list


def main():
    # This function prints out the first 100 fibonacci sequences

    # Process
    number_list = calculate()
    for counter in range(100):
        if counter == 0:
            print(number_list[0], "+ 0 =", number_list[0])
        elif counter == 1:
            print("0 +", number_list[1], "=", number_list[1])
        else:
            print(number_list[counter - 2], "+", number_list[counter - 1],
                  "=", number_list[counter])


if __name__ == "__main__":
    main()
