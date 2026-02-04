def evaluate_credit_score(score):
    # Check for invalid range first
    if score < 300 or score > 850:
        return "Invalid score."
    if score >= 750:
        return "Excellent - Loan Approved. Interest rate: Low"
    elif 700 <= score < 750:
        return "Good - Loan Approved with Review. Interest rate: Low"
    elif 600 <= score < 700:
        return "Fair - Loan Conditional. Seek credit improvement."
    else:  # score < 600
        return "Poor - Loan Denied. Seek credit improvement."
# Get user input
score = int(input("What's your credit score? "))

# Evaluate and print result
result = evaluate_credit_score(score)
print(result)