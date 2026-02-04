revenue = float(input("What is the product's revenue? "))
cost = float(input("What is the product's cost? "))

profit = revenue - cost

if revenue > 0:
    margin = (profit / revenue) * 100
else:
    margin = 0

print(f"The product's profit is: ${profit:.2f} | Margin : {margin:.2f}%") 