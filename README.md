# Celebal_Week1_assignment

# Triangle Pattern Printer in Python

This is a simple Python program that prints three types of triangle patterns using the `*` character:

- Lower Triangle
- Upper Triangle
- Pyramid

The user is asked to enter the number of rows, and the patterns are printed based on that input.

## How It Works

- The program takes input from the user for the number of rows.
- If the user enters anything invalid or a negative number, it will show an error message and ask again.
- After a valid number is entered, it prints:
  - Lower triangle using a nested loop
  - Upper triangle by adding spaces before stars
  - Pyramid by centering the stars in each row

## Functions Used

- `lower_triangle(n)` – prints a lower triangular pattern.
- `upper_triangle(n)` – prints an upper triangular pattern.
- `pyramid(n)` – prints a pyramid shape.

## Input Handling

- Used a `while` loop to keep asking the user until they enter a valid positive integer.
- Basic error handling is done using `try-except`.

## Sample Output


