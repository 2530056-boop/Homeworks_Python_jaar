# --------------------------------------------------
# COVER PAGE
# Name: Jesus Adrian Ramos Rodriguez
# Matricula: 2530056
# Group: IM 1-2
# --------------------------------------------------

# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# The Fibonacci series is a numerical sequence where each term is the sum of
# the previous two, starting with 0 and 1. Calculating the series up to n
# terms means generating the first n values in this sequence. This program
# reads an integer n, validates the input, and prints the first n Fibonacci
# terms using an iterative loop. The program also handles invalid inputs such
# as non-integer values or numbers outside the allowed range.
# --------------------------------------------------

# --------------------------------------------------
# PROBLEM: Fibonacci Series Generator
# --------------------------------------------------
# Description:
# Program that reads an integer n and prints the first n terms of the
# Fibonacci series, starting at 0 and 1.
#
# Inputs:
# - n (int): number of terms to generate
#
# Outputs:
# - "Fibonacci series:" followed by the n generated terms
#
# Validations:
# - n must be an integer
# - n >= 1
# - Optional limit: n <= 50 (to avoid excessively large outputs)
#
# Test Cases:
# 1) Normal case:
#    Input: n = 7
#    Expected output: 0 1 1 2 3 5 8
#
# 2) Border case:
#    Input: n = 1
#    Expected output: 0
#
# 3) Error case:
#    Input: n = "abc"
#    Expected output: Error: invalid input
#
# (Optional Table – textual description)
# Test case table:
# | Type   | Input | Expected Output              |
# |--------|--------|------------------------------|
# | Normal |   7    | 0 1 1 2 3 5 8                |
# | Border |   1    | 0                            |
# | Error  | "abc" | Error: invalid input         |
#
# (Optional Flow Diagram – textual description)
# 1. Start
# 2. Read n
# 3. Validate integer -> if fail, print error and stop
# 4. Validate range (1 ≤ n ≤ 50) -> if fail, print error
# 5. Use loop to generate Fibonacci
# 6. Print series
# 7. End
# --------------------------------------------------


# ================================
#          FIBONACCI CODE
# ================================

# Read input
n_input = input("Enter number of terms: ")

# Input validation: can it be converted to int?
try:
    terms_count = int(n_input)
except:
    print("Error: invalid input")
    exit()

# Logical validations
if terms_count < 1 or terms_count > 50:
    print("Error: invalid input")
    exit()

# Fibonacci generation
first_term = 0
second_term = 1

print("Fibonacci series:", end=" ")

# Case n = 1
if terms_count == 1:
    print(first_term)
    exit()

# Case n >= 2: print first two terms
print(first_term, second_term, end=" ")

# Loop for remaining terms
for _ in range(3, terms_count + 1):
    next_term = first_term + second_term
    print(next_term, end=" ")
    first_term = second_term
    second_term = next_term

print()  # newline at the end


# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Using a loop makes generating the Fibonacci sequence efficient and easy to
# control, especially when handling larger values of n. Managing edge cases
# such as n = 1 or n = 2 ensures correct behavior even for minimal inputs.
# This logic can be reused in many algorithms involving iterative patterns,
# mathematical sequences, or dynamic programming methods.
# --------------------------------------------------

# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Documentation – for loops & while loops:
#    https://docs.python.org/3/tutorial/controlflow.html
# 2) Fibonacci sequence explanation – Khan Academy:
#    https://www.khanacademy.org/math/algebra/sequences
# 3) Python Official Tutorial – Input and Error Handling:
#    https://docs.python.org/3/tutorial/errors.html
#   4)Python documentation - Built-in Functions (min, max, round)
# 5) Python tutorial - Errors and Exceptions
# --------------------------------------------------

# --------------------------------------------------
# GitHub Repository
# https://github.com/2530056-boop/Homeworks_Python_jaar.git
# --------------------------------------------------
