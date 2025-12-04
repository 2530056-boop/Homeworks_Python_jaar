
# Portada:
# Name: Jesus Adrian Ramos Rodriguez
# Matricula: 2530056
# Group: IM 1-2
#
# Executive Summary:
# This file contains six small Python programs (Problems 1-6) demonstrating function design,
# parameter validation, and returning values. A function in Python is a reusable block of code
# declared with def that can accept parameters, execute logic, and optionally return a value.
# Parameters are the names used in the function definition; arguments are the actual values
# passed when calling the function. Separating logic into functions improves reusability,
# testability, and readability. A return value allows other code to use the function's result
# programmatically instead of only printing it. This document contains problem descriptions,
# inputs, outputs, validations, implementation, and three test cases per problem.
#
# Principles and Good Practices (short):
# - Prefer small functions that do a single thing (single responsibility).
# - Avoid repeating logic: extract repeated code into helper functions.
# - Try to make functions pure when possible (same input -> same output, no side effects).
# - Document with concise comments what each function does and its expected parameters.
# - Use clear function names (e.g., calculate_area, summarize_numbers).
#
# -----------------------------------------------------------------------------
# Problem 1: Rectangle area and perimeter
# Description: Calculate area and perimeter of a rectangle using functions.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width > 0
# - height > 0
# - On invalid input print "Error: invalid input" and do not call the functions.
#
# Test cases:
# 1) Normal: width=5, height=3 -> Area:15, Perimeter:16
# 2) Border: width=0.0001, height=1 -> small positive values
# 3) Error: width=-2, height=3 -> Error: invalid input


def calculate_area(width, height):
    """Return area of rectangle (width * height)."""
    return width * height


def calculate_perimeter(width, height):
    """Return perimeter of rectangle (2*(width+height))."""
    return 2 * (width + height)


def problem_1_demo():
    print('\n--- Problem 1: Rectangle area and perimeter ---')
    test_cases = [
        (5.0, 3.0),        # normal
        (0.0001, 1.0),     # border (small positive)
        (-2.0, 3.0)        # error
    ]
    for width, height in test_cases:
        print(f'Input: width={width}, height={height}')
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            print('Error: invalid input')
            continue
        if width <= 0 or height <= 0:
            print('Error: invalid input')
            continue
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print('Area:', area)
        print('Perimeter:', perimeter)


# -----------------------------------------------------------------------------
# Problem 2: Grade classifier
# Description: Classify a numeric score (0-100) into letter grades A/B/C/D/F.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - On invalid input print "Error: invalid input" and do not classify.
#
# Test cases:
# 1) Normal: score=92 -> A
# 2) Border: score=89.999 -> B (close to threshold)
# 3) Error: score=120 -> Error: invalid input


def classify_grade(score):
    """Return a letter grade for a numeric score between 0 and 100."""
    # Assume input validated by caller; still perform safe checks
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def problem_2_demo():
    print('\n--- Problem 2: Grade classifier ---')
    test_scores = [92, 89.999, 120]
    for s in test_scores:
        print(f'Input: score={s}')
        if not isinstance(s, (int, float)):
            print('Error: invalid input')
            continue
        if s < 0 or s > 100:
            print('Error: invalid input')
            continue
        category = classify_grade(s)
        print('Score:', s)
        print('Category:', category)


# -----------------------------------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# Description: Convert a comma-separated text to a list of numbers, then summarize.
#
# Inputs:
# - numbers_text (string like "10,20,30")
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - numbers_text not empty after strip
# - After conversion, list not empty
# - All elements convertible to float
# - On invalid input print "Error: invalid input"
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Border: "5" (single number)
# 3) Error: "10,abc,20" -> invalid input


def summarize_numbers(numbers_list):
    """Return dict with min, max and average of a non-empty list of numbers."""
    if not numbers_list:
        raise ValueError('Empty list')
    total = sum(numbers_list)
    count = len(numbers_list)
    average = total / count
    return {'min': min(numbers_list), 'max': max(numbers_list), 'average': average}


def parse_numbers_text(numbers_text):
    """Parse a comma-separated string into a list of floats. Raises ValueError on invalid input."""
    if not isinstance(numbers_text, str) or numbers_text.strip() == '':
        raise ValueError('Empty input')
    parts = [p.strip() for p in numbers_text.split(',')]
    numbers = []
    for p in parts:
        if p == '':
            # ignore empty tokens (e.g., trailing comma) or treat as error — here treat as error
            raise ValueError('Invalid token')
        try:
            num = float(p)
        except Exception:
            raise ValueError('Invalid number')
        numbers.append(num)
    if len(numbers) == 0:
        raise ValueError('Empty list')
    return numbers


def problem_3_demo():
    print('\n--- Problem 3: List statistics ---')
    test_texts = ['10,20,30', '5', '10,abc,20']
    for txt in test_texts:
        print(f'Input: "{txt}"')
        try:
            numbers = parse_numbers_text(txt)
            summary = summarize_numbers(numbers)
            print('Min:', summary['min'])
            print('Max:', summary['max'])
            print('Average:', summary['average'])
        except ValueError:
            print('Error: invalid input')


# -----------------------------------------------------------------------------
# Problem 4: Apply discount list (pure function)
# Description: Apply a discount rate to a list of prices and return a new list.
#
# Inputs:
# - prices_text (string like "100,200,300")
# - discount_rate (float between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text not empty and convertible
# - all prices > 0
# - 0 <= discount_rate <= 1
# - On invalid input print "Error: invalid input"
#
# Test cases:
# 1) Normal: "100,200,300", discount_rate=0.1 -> [90,180,270]
# 2) Border: "0.01", discount_rate=0 -> no discount
# 3) Error: "100,-50", discount_rate=0.2 -> invalid input due to negative price


def apply_discount(prices_list, discount_rate):
    """Return a new list with discounted prices. Does not modify input list."""
    if not isinstance(prices_list, list):
        raise ValueError('Prices must be a list')
    if not (isinstance(discount_rate, (int, float)) and 0 <= discount_rate <= 1):
        raise ValueError('Invalid discount rate')
    discounted = []
    for p in prices_list:
        if p <= 0:
            raise ValueError('Price must be > 0')
        discounted_price = p * (1 - discount_rate)
        discounted.append(discounted_price)
    return discounted


def problem_4_demo():
    print('\n--- Problem 4: Apply discount list ---')
    test_inputs = [
        ('100,200,300', 0.1),
        ('0.01', 0.0),
        ('100,-50', 0.2)
    ]
    for prices_text, rate in test_inputs:
        print(f'Input: prices_text="{prices_text}", discount_rate={rate}')
        try:
            prices = parse_numbers_text(prices_text)
            # ensure all > 0
            if any(p <= 0 for p in prices):
                raise ValueError('Price must be > 0')
            discounted = apply_discount(prices, rate)
            print('Original prices:', prices)
            print('Discounted prices:', discounted)
        except ValueError:
            print('Error: invalid input')


# -----------------------------------------------------------------------------
# Problem 5: Greeting function with default parameters
# Description: Create greet(name, title='') that returns "Hello, <full_name>!".
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name not empty after strip
# - title may be empty
#
# Test cases:
# 1) Normal: name="Alice", title="Dr." -> "Hello, Dr. Alice!"
# 2) Border: name=" Bob ", title="" -> "Hello, Bob!"
# 3) Error: name="   " -> Error: invalid input


def greet(name, title=""):
    """Return greeting message 'Hello, <title + name>!'."""
    if not isinstance(name, str):
        raise ValueError('Invalid name')
    n = name.strip()
    if n == '':
        raise ValueError('Invalid name')
    t = '' if title is None else str(title).strip()
    if t:
        full_name = f"{t} {n}"
    else:
        full_name = n
    return f'Hello, {full_name}!'


def problem_5_demo():
    print('\n--- Problem 5: Greeting function ---')
    test_cases = [
        ('Alice', 'Dr.'),
        (' Bob ', ''),
        ('   ', 'Mr.')
    ]
    for name, title in test_cases:
        print(f'Input: name="{name}", title="{title}"')
        try:
            greeting = greet(name, title)
            print('Greeting:', greeting)
        except ValueError:
            print('Error: invalid input')


# -----------------------------------------------------------------------------
# Problem 6: Factorial function (iterative)
# Description: Compute factorial(n). Implemented iteratively to avoid recursion depth
# issues for reasonable n. Limit n to 0 <= n <= 20 to avoid huge integers for this task.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be int
# - n >= 0
# - n <= 20 (chosen limit)
# - On invalid input print "Error: invalid input"
#
# Test cases:
# 1) Normal: n=5 -> 120
# 2) Border: n=0 -> 1
# 3) Error: n=-3 or n=100 -> Error: invalid input


MAX_FACTORIAL_N = 20  # safe upper bound for this exercise


def factorial(n):
    """Iterative factorial. Returns n! for 0 <= n <= MAX_FACTORIAL_N."""
    if not isinstance(n, int):
        raise ValueError('n must be integer')
    if n < 0 or n > MAX_FACTORIAL_N:
        raise ValueError('n out of allowed range')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def problem_6_demo():
    print('\n--- Problem 6: Factorial ---')
    test_ns = [5, 0, -3]
    for n in test_ns:
        print(f'Input: n={n}')
        try:
            if not isinstance(n, int):
                raise ValueError('n must be integer')
            if n < 0 or n > MAX_FACTORIAL_N:
                raise ValueError('n out of allowed range')
            f = factorial(n)
            print('n:', n)
            print('Factorial:', f)
        except ValueError:
            print('Error: invalid input')


# -----------------------------------------------------------------------------
# Main demo runner: calls demos for each problem. In production, a test harness or
# unit tests would be more appropriate. We call each demo to show outputs.
#

def main():
    problem_1_demo()
    problem_2_demo()
    problem_3_demo()
    problem_4_demo()
    problem_5_demo()
    problem_6_demo()
    print('\nAll demos completed.\n')


if __name__ == '__main__':
    main()


# -----------------------------------------------------------------------------
# Conclusions (5-8 lines):
# Functions help organize code by encapsulating specific tasks and enabling reuse.
# Returning values instead of only printing makes functions composable and testable.
# Default parameters increase flexibility, allowing optional arguments without overloads.
# Encapsulating repeated logic (parsing, validation) reduces bugs and simplifies maintenance.
# Separating main program flow from helper functions clarifies responsibilities and aids unit testing.

# References (minimum 5):
# 1) Python documentation - Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Python documentation - Exceptions: https://docs.python.org/3/tutorial/errors.html
# 3) Real Python - Functions: https://realpython.com/defining-your-own-python-function/
# 4) W3Schools - Python Functions: https://www.w3schools.com/python/python_functions.asp
# 5) GeeksforGeeks - Python Program to find factorial: https://www.geeksforgeeks.org/python-program-to-find-factorial-of-a-number/
#
# GitHub repository (replace with your own):
# https://github.com/2530056-boop/Homeworks_Python_jaar.git
# -----------------------------------------------------------------------------
