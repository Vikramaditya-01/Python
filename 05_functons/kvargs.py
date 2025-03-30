def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"({key} : {value})")

# Taking dynamic input from the user
user_input = input("Enter key-value pairs (e.g., name=Vikramaditya, branch=CSE): ")

# Processing input to handle spaces
kwargs_dict = dict(item.strip().split("=") for item in user_input.replace(" ", "").split(",") if "=" in item)

# Calling the function with dynamic user input
print_kwargs(**kwargs_dict)
