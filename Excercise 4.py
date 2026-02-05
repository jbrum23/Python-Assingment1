# Function to determine tax bracket and rate
def get_tax_bracket(income):
    # Handle invalid income
    if income < 0:
        return "Invalid income.", 0.0

    # Determine bracket and tax rate
    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30

    # Bonus: ternary expression for deduction eligibility
    bracket = bracket + " (Deduction Eligible)" if int(income) % 2 == 0 else bracket

    return bracket, rate


# Main program
income = float(input("What's your annual income? "))

bracket, rate = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")
