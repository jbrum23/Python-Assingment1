# Prompt the user for the product's revenue and cost.
revenue = float(input("What is the product's revenue? "))
cost = float(input("What is the product's cost? "))

# calculate profit
profit = revenue - cost

# calculate margin, ensuring we don't divide by zero
if revenue > 0:
    margin = (profit / revenue) * 100
else:
    margin = 0

# Display the profit and margin to the user.
print(f"The product's profit is: ${profit:.2f} | Margin : {margin:.2f}%") 