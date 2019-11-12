#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program reverses a digit

import math


def main():

    number = int(input("Enter a number: "))
    result = ""

    if number == 0:
        print(0)
        exit(0)

    while number != 0:
        result += str(number % 10)
        number = math.floor(number / 10)

    print(result)


if __name__ == "__main__":
    main()
