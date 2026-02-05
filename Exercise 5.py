# Prompt for product name and normalize input
product = input("What's the product? ").strip().lower()

# Determine product category using match-case
match product:
    case "electronics" | "gadget" | _ if product.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

# Output result
print(f"Product: {product} | Category: {category}")
