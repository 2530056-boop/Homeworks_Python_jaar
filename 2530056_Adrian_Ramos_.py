# --------------------------------------------------
# COVER PAGE
# Name: Jesus Adrian Ramos Rodriguez
# Matriculation: 2530056
# --------------------------------------------------

# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# In Python, int represents whole numbers without a fractional part,
# while float represents real numbers with decimals. Booleans (True/False)
# are produced by comparison expressions and control program logic.
# Validating ranges and avoiding division by zero prevents runtime errors
# and incorrect calculations. This document implements six small programs
# (problems 1-6) with clear inputs, outputs, validations, and test cases,
# demonstrating the combined use of ints, floats, and booleans for
# decision-making in practical scenarios.
# --------------------------------------------------

# --------------------------------------------------
# PRINCIPLES AND BEST PRACTICES
# --------------------------------------------------
# - Use appropriate data types: int for counters/indices, float for
#   measurements and monetary values.
# - Avoid duplicating complex expressions: store intermediate
#   results in descriptive variables.
# - Validate inputs before processing (type conversion, ranges).
# - Use clear variable names in lower_snake_case and constants in
#   UPPER_SNAKE_CASE.
# - Document how booleans are interpreted: true means condition met,
#   false means condition not met.
# --------------------------------------------------


# ==================================================
# PROBLEM 1: Temperature converter and range flag
# ==================================================
# Problem 1: Temperature converter and range flag
# Description: Convert Celsius to Fahrenheit and Kelvin, and
# determine is_high_temperature (true if temp_c >= 30.0).
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
#
# Validations:
# - temp_c must convert to float
# - temp_k (temp_c + 273.15) must be >= 0.0
#
# Test cases:
# 1) Normal: temp_c = 25.0
# 2) Border: temp_c = -273.15
# 3) Error: temp_c = -300.0 (below absolute zero)
# --------------------------------------------------
try:
    temp_c_input = input("Enter temperature in °C: ")
    temp_c = float(temp_c_input)
except Exception:
    print("Error: invalid input")
else:
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: temperature is below absolute zero")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = (temp_c >= 30.0)
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())


# ==================================================
# PROBLEM 2: Work hours and overtime payment
# ==================================================
# Problem 2: Work hours and overtime payment
# Description: Calculate weekly pay. Up to 40 hours at hourly_rate;
# overtime (>40) paid at 1.5x. has_overtime is true if hours_worked > 40.
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
# - On invalid input: print "Error: invalid input"
#
# Test cases:
# 1) Normal: hours_worked = 45.0, hourly_rate = 100.0
# 2) Border: hours_worked = 40.0, hourly_rate = 50.0
# 3) Error: hours_worked = -5.0
# --------------------------------------------------
try:
    hours_input = input("Enter hours worked this week: ")
    rate_input = input("Enter hourly rate: ")
    hours_worked = float(hours_input)
    hourly_rate = float(rate_input)
except Exception:
    print("Error: invalid input")
else:
    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)
        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())


# ==================================================
# PROBLEM 3: Discount eligibility with booleans
# ==================================================
# Problem 3: Discount eligibility with booleans
# Description: A 10% discount applies if is_student or is_senior
# or purchase_total >= 1000.0. Convert YES/NO to booleans.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string "YES"/"NO")
# - is_senior_text (string "YES"/"NO")
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - is_student_text and is_senior_text must be "YES" or "NO"
# - On invalid input: print "Error: invalid input"
#
# Test cases:
# 1) Normal: purchase_total=1200.0, is_student="NO", is_senior="NO"
# 2) Border: purchase_total=1000.0, is_student="NO", is_senior="NO"
# 3) Error: is_student="MAYBE"
# --------------------------------------------------
try:
    purchase_text = input("Enter purchase total: ")
    is_student_text = input("Are you a student? (YES/NO): ")
    is_senior_text = input("Are you a senior? (YES/NO): ")
    purchase_total = float(purchase_text)
except Exception:
    print("Error: invalid input")
else:
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:
        is_student_text = is_student_text.strip().upper()
        is_senior_text = is_senior_text.strip().upper()
        if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
        else:
            is_student = (is_student_text == "YES")
            is_senior = (is_senior_text == "YES")
            discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
            if discount_eligible:
                final_total = purchase_total * 0.9
            else:
                final_total = purchase_total
            print("Discount eligible:", str(discount_eligible).lower())
            print("Final total:", final_total)


# ==================================================
# PROBLEM 4: Basic statistics of three integers
# ==================================================
# Problem 4: Basic statistics of three integers
# Description: Read three integers and print sum, average,
# max, min and all_even flag.
#
# Inputs:
# - n1 (int), n2 (int), n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - All three values must convert to int
#
# Test cases:
# 1) Normal: 5, 10, 15
# 2) Border: 0, 0, 0
# 3) Error: non-integer input
# --------------------------------------------------
try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))
except Exception:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())


# ==================================================
# PROBLEM 5: Loan eligibility (income and debt ratio)
# ==================================================
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Determine loan eligibility using monthly_income,
# monthly_debt and credit_score.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0.0
# - monthly_debt >= 0.0
# - credit_score >= 0
# - On invalid input: print "Error: invalid input"
#
# Test cases:
# 1) Normal: monthly_income=10000.0, monthly_debt=2000.0, credit_score=700
# 2) Border: monthly_income=8000.0, monthly_debt=3200.0, credit_score=650
# 3) Error: monthly_income=0.0
# --------------------------------------------------
try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))
except Exception:
    print("Error: invalid input")
else:
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())


# ==================================================
# PROBLEM 6: Body Mass Index (BMI) and category flag
# ==================================================
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculate BMI and flags for underweight, normal,
# overweight categories.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI:" <bmi_rounded>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - On invalid input: print "Error: invalid input"
#
# Test cases:
# 1) Normal: weight_kg=70.0, height_m=1.75
# 2) Border: bmi at 18.5 -> weight=1.70*1.70*18.5
# 3) Error: height_m = 0.0
# --------------------------------------------------
try:
    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))
except Exception:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)
        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)
        print("BMI:", bmi_rounded)
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())


# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Integers and floats are combined to model real situations: ints
# for counts and indexes, floats for measurements and monetary values.
# Comparisons produce boolean values that drive program flow and
# decisions (true/false). Validating inputs avoids crashes (e.g.,
# division by zero) and incorrect results. Logical operators (and,
# or, not) allow building complex eligibility rules used in payroll,
# discounts and loan decisions.
# --------------------------------------------------

# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# References:
# 1) Python documentation - Numeric and Boolean types
# 2) Python documentation - Built-in Functions (min, max, round)
# 3) Python tutorial - Errors and Exceptions
# 4) Class notes on data validation and control structures
# 5) Programming textbook: Algorithms and Problem Solving
# --------------------------------------------------

# --------------------------------------------------
# GITHUB REPOSITORY
# --------------------------------------------------
# https://github.com/2530056-boop/Homeworks_Python_jaar.git
# --------------------------------------------------
