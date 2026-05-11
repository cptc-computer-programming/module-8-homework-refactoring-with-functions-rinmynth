# Assignment #8: Refactoring with Functions

## Overview

In this assignment, you will practice refactoring Python code using functions to improve readability, organization, testing, and maintainability.

You will work from starter code and reorganize the program into reusable functions.

## Learning Objectives

- Refactor code into modular functions
- Write functions with parameters and return values
- Use a `main()` function to organize program flow
- Improve readability and maintainability of code

---

# Requirements

Your program must refactor the provided starter code according to the specifications below. Edit the starter code in the file `one_week_later.py`.

---

# Program Specifications

## 1. Use a `main()` Function

Your program must include a `main()` function to control the flow of the program.

Use the following structure:

    def main():
        # your code here

    if __name__ == "__main__":
        main()

---

## 2. Prompt the User for Input

Inside `main()`, prompt the user for:

- Month (`1-12`)
- Day (`1-31`)

Example:

    Enter the month (1-12): 11
    Enter the day (1-31): 13

---

## 3. Create a Function

Create a function named:

`find_date_one_week_later(month, date)`

This function should:

- Accept the month and day as parameters
- Calculate the date exactly one week later
- Return the new month and date

You should move the existing date calculation logic from the starter code into this function.

Example:

    def find_date_one_week_later(month, date):
        # your code here

---

## 4. Call the Function from `main()`

Inside `main()`:

- Call `find_date_one_week_later(month, date)`
- Store the returned values
- Print the result

Example output:

    A week after 11/13 is 11/20.

---
# Example Run

    Enter the month (1-12): 11
    Enter the day (1-31): 13
    A week after 11/13 is 11/20.
---

# Extra Credit (10 pts)

## Number Guessing Game

**Create a separate Python file** that implements a number guessing game.

### Requirements

- The program randomly selects a number between 1 and 100
- The user repeatedly guesses the number
- After each guess:
  - Print `"Too high, try again."`
  - OR print `"Too low, try again."`
- When the user guesses correctly:
  - Print `"You got it in x tries."`

---

## Required Functions

### `main()`

- Controls the overall game
- Calls `pick_number()`
- Calls `respond()`
- Tracks total guesses

---

### `pick_number()`

- Uses the `random` library
- Picks a number between global constants:
  - `LOWEST`
  - `HIGHEST`
- Returns the selected number

Example:

    LOWEST = 1
    HIGHEST = 100

---

### `respond(number, guess)`

- Compares the guess to the secret number
- Prints:
  - `"Too high, try again."`
  - `"Too low, try again."`

---


# Submission Instructions

1. Complete your assignment in `one_week_later.py`
2. Push your work to your GitHub Classroom repository
3. Open the automatically generated feedback pull request
4. Submit the feedback PR link to the Canvas assignment



