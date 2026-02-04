def format_greeting(name, title="Customer"):
   # Remove leading/trailing whitespace
    cleaned_name = name.strip()
    
    # Handle empty name case
    if cleaned_name == "":
        return "Hello, Valued Customer!"
    
    # Convert to proper capitalization
    titled_name = cleaned_name.title()
    
    # Split the name into parts
    parts = titled_name.split()
    
    # Find first part with alphabetic characters
    first_name = ""
    for part in parts:
        if part.isalpha():  
            first_name = part
            break
    
    return f"Hello, {first_name} ({title})!"

# The main program
full_name = input("What's your full name? ")
custom_title = input("Enter your title (press Enter for default): ").strip()

# Optional extension: Use default title if none provided
if custom_title == "":
    greeting = format_greeting(full_name)
else:
    greeting = format_greeting(full_name, custom_title)

print(greeting)
