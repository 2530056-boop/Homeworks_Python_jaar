# Portada:
# Name: Jesus Adrian Ramos Rodriguez
# Matricula: 2530056
# Group: IM 1-2

"""
Resumen ejecutivo:
This Python file implements six small programs that practice loop constructs (for and while).
- A for loop iterates a known number of times and is used for range summation and pattern printing.
- A while loop repeats until a condition changes and is used for sentinel reading, password attempts, and menus.
- Counters and accumulators are used to count items and accumulate sums respectively.
- Proper exit conditions are defined to avoid infinite loops (e.g., updating loop variables, using sentinels, and max attempts).
This document contains: problem descriptions, input/output specifications, validations, test cases, and implementations.
"""

# PRINCIPLES AND GOOD PRACTICES (comments):
# - Use for when the number of iterations is known (for i in range(start, stop)).
# - Use while when iterations depend on a condition (e.g., reading until 'EXIT').
# - Initialize counters and accumulators before loops.
# - Update control variables inside while loops to avoid infinite loops.
# - Keep loop bodies simple; extract complex logic into functions when needed.

# TEMPLATE FOR PROBLEMS (example comment block used before each problem)

# ----------------------------
# Problem 1: Sum of range with for
# Description: Calculate the sum of integers from 1 to n and the sum of even numbers in that range.
# Inputs:
# - n (int)
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
# Validations:
# - n must be convertible to int and n >= 1
# Test cases:
# 1) Normal: n=10 -> Sum 55, Even sum 30
# 2) Border: n=1 -> Sum 1, Even sum 0
# 3) Error: n=0 -> Error: invalid input
# ----------------------------

def sum_range(n):
    """Return tuple (total_sum, even_sum) or raise ValueError on invalid input."""
    try:
        n_int = int(n)
    except Exception:
        raise ValueError("Error: invalid input")
    if n_int < 1:
        raise ValueError("Error: invalid input")
    total_sum = 0
    even_sum = 0
    for i in range(1, n_int + 1):  # for + range example
        total_sum += i
        if i % 2 == 0:
            even_sum += i
    return total_sum, even_sum


# ----------------------------
# Problem 2: Multiplication table with for
# Description: Print multiplication table for base from 1 to m.
# Inputs:
# - base (int)
# - m (int)
# Outputs:
# - Lines like: "{base} x {i} = {product}"
# Validations:
# - base and m convertible to int; m >= 1
# Test cases:
# 1) Normal: base=5,m=4 -> lines for 1..4
# 2) Border: base=3,m=1 -> single line
# 3) Error: m=0 -> Error: invalid input
# ----------------------------

def multiplication_table(base, m):
    try:
        base_int = int(base)
        m_int = int(m)
    except Exception:
        raise ValueError("Error: invalid input")
    if m_int < 1:
        raise ValueError("Error: invalid input")
    lines = []
    for i in range(1, m_int + 1):
        product = base_int * i
        lines.append(f"{base_int} x {i} = {product}")
    return lines


# ----------------------------
# Problem 3: Average of numbers with while and sentinel
# Description: Read numbers until sentinel (-1) and compute count and average.
# Inputs:
# - Repeated numbers (float) via input() or via provided iterator for testing
# Outputs:
# - "Count:" <count>
# - "Average:" <average>
# - If no valid data -> "Error: no data"
# Validations:
# - Each item must convert to float; sentinel is ignored in calculations
# Test cases:
# 1) Normal: inputs 5, 7, -1 -> Count 2, Average 6.0
# 2) Border: inputs -1 -> Error: no data
# 3) Error: inputs 'a', 5, -1 -> invalid input for 'a' should print error message
# ----------------------------

SENTINEL_VALUE = -1.0

def average_with_sentinel(input_provider=None):
    """If input_provider is None, read from input(). Otherwise, call input_provider() repeatedly to get strings.
    Returns (count, average) or raises ValueError("Error: no data") or ValueError("Error: invalid input") for bad conversions.
    """
    total = 0.0
    count = 0
    if input_provider is None:
        def input_provider():
            return input()
    while True:
        raw = input_provider()
        try:
            value = float(raw)
        except Exception:
            raise ValueError("Error: invalid input")
        if value == SENTINEL_VALUE:
            break
        total += value
        count += 1
    if count == 0:
        raise ValueError("Error: no data")
    average = total / count
    return count, average


# ----------------------------
# Problem 4: Password attempts with while
# Description: Allow up to MAX_ATTEMPTS attempts to enter correct_password.
# Inputs:
# - user passwords via input() or input_provider for testing
# Outputs:
# - "Login success" or "Account locked"
# Validations:
# - MAX_ATTEMPTS must be > 0
# Test cases:
# 1) Normal: correct on second attempt -> Login success
# 2) Border: correct on first attempt -> Login success
# 3) Error: all attempts wrong -> Account locked
# ----------------------------

MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "admin123"

def password_attempts(input_provider=None):
    if MAX_ATTEMPTS <= 0:
        raise ValueError("Error: invalid configuration")
    attempts = 0
    if input_provider is None:
        def input_provider():
            return input()
    while attempts < MAX_ATTEMPTS:
        user_password = input_provider()
        attempts += 1
        if user_password == CORRECT_PASSWORD:
            return "Login success"
    return "Account locked"


# ----------------------------
# Problem 5: Simple menu with while
# Description: Text menu with options 1: greeting, 2: show counter, 3: increment, 0: exit
# Inputs:
# - option via input() or input_provider
# Outputs:
# - Messages per option; returns when 0 selected
# Validations:
# - option must be convertible to int and in {0,1,2,3}
# Test cases:
# 1) Normal: 1,2,3,2,0 -> executes actions accordingly
# 2) Border: 0 -> prints Bye!
# 3) Error: invalid option like 'a' -> Error: invalid option
# ----------------------------

def simple_menu(input_provider=None, output_collector=None):
    counter = 0
    if input_provider is None:
        def input_provider():
            return input()
    if output_collector is None:
        def output_collector(msg):
            print(msg)
    while True:
        raw = input_provider()
        try:
            option = int(raw)
        except Exception:
            output_collector("Error: invalid option")
            continue
        if option == 1:
            output_collector("Hello!")
        elif option == 2:
            output_collector(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            output_collector("Counter incremented")
        elif option == 0:
            output_collector("Bye!")
            break
        else:
            output_collector("Error: invalid option")


# ----------------------------
# Problem 6: Pattern printing with nested loops
# Description: Print right-angle triangle of '*' with n rows. Optionally print inverted pattern.
# Inputs:
# - n (int)
# Outputs:
# - Lines of asterisks
# Validations:
# - n convertible to int and n >= 1
# Test cases:
# 1) Normal: n=4 -> lines '*','**','***','****'
# 2) Border: n=1 -> single '*'
# 3) Error: n=0 -> Error: invalid input
# ----------------------------

def pattern_triangle(n, inverted=False):
    try:
        n_int = int(n)
    except Exception:
        raise ValueError("Error: invalid input")
    if n_int < 1:
        raise ValueError("Error: invalid input")
    lines = []
    for i in range(1, n_int + 1):  # nested loops conceptually; here we use string multiplication
        lines.append("*" * i)
    if inverted:
        for i in range(n_int, 0, -1):
            lines.append("*" * i)
    return lines


# ----------------------------
# Test driver demonstrating the required test cases for each problem.
# The driver runs non-interactive test cases and prints outputs.
# ----------------------------

def run_demo_tests():
    print("--- Problem 1 Tests ---")
    for case in [10, 1, 0]:
        try:
            total, even = sum_range(case)
            print(f"Input n={case} -> Sum 1..n: {total}, Even sum 1..n: {even}")
        except Exception as e:
            print(f"Input n={case} -> {e}")

    print("\n--- Problem 2 Tests ---")
    for base, m in [(5, 4), (3, 1), (2, 0)]:
        try:
            lines = multiplication_table(base, m)
            print(f"base={base}, m={m}")
            for l in lines:
                print(l)
        except Exception as e:
            print(f"base={base}, m={m} -> {e}")

    print("\n--- Problem 3 Tests ---")
    # Normal: 5,7,-1 ; Border: -1 ; Error: 'a',5,-1
    demo_inputs = [iter(["5", "7", "-1"]), iter(["-1"]), iter(["a", "5", "-1"]) ]
    for it in demo_inputs:
        def provider():
            return next(it)
        try:
            count, avg = average_with_sentinel(provider)
            print(f"Count: {count}, Average: {avg}")
        except Exception as e:
            print(e)

    print("\n--- Problem 4 Tests ---")
    # Normal: wrong, correct ; Border: correct ; Error: three wrong
    inputs_list = [iter(["wrong", "admin123"]), iter(["admin123"]), iter(["no", "no", "no"])]
    for it in inputs_list:
        def provider():
            return next(it)
        try:
            result = password_attempts(provider)
            print(result)
        except StopIteration:
            print("Account locked")
        except Exception as e:
            print(e)

    print("\n--- Problem 5 Tests ---")
    # Normal: 1,2,3,2,0 ; Border: 0 ; Error: 'a',0
    sequences = [iter(["1","2","3","2","0"]), iter(["0"]), iter(["a","0"]) ]
    for it in sequences:
        outputs = []
        def provider():
            return next(it)
        def collector(msg):
            outputs.append(msg)
        try:
            simple_menu(provider, collector)
        except StopIteration:
            outputs.append("Stopped unexpectedly")
        print(outputs)

    print("\n--- Problem 6 Tests ---")
    for n in [4, 1, 0]:
        try:
            lines = pattern_triangle(n)
            print(f"n={n}")
            for l in lines:
                print(l)
        except Exception as e:
            print(f"n={n} -> {e}")


if __name__ == "__main__":
    run_demo_tests()


# CONCLUSIONS (comments):
# - For loops are ideal when the number of iterations is known; while loops are natural when waiting for a condition.
# - Counters and accumulators simplify tracking quantities and computing sums/averages.
# - The main risk with while is infinite loops; always update the control variable or use a sentinel/break.
# - Menus and password attempts are typical use-cases for while loops because they depend on user actions.
# - Nested loops (or repeated loops) are useful to build patterns; string multiplication can simplify some pattern tasks.

# REFERENCES (minimum 5):
# 1) Python documentation - for statements: https://docs.python.org/3/tutorial/controlflow.html#for-statements
# 2) Python documentation - while statements: https://docs.python.org/3/tutorial/controlflow.html#while-statements
# 3) W3Schools Python loops: https://www.w3schools.com/python/python_for_loops.asp
# 4) Real Python - Python Loops: https://realpython.com/python-for-loop/
# 5) GeeksforGeeks - Loop control in Python: https://www.geeksforgeeks.org/loops-in-python/

# GitHub repository (replace with your repo):
# https://github.com/2530056-boop/Homeworks_Python_jaar.git

