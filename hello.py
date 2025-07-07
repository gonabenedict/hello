def greet_user():
    """Function to greet a user by name"""
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to our simple Python program!")
    return name

def calculate_age():
    """Function to calculate age from birth year"""
    current_year = 2025
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year
    print(f"You are approximately {age} years old.")
    return age

def simple_calculator():
    """Simple calculator function"""
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            return
    else:
        print("Error: Invalid operator!")
        return
    
    print(f"{num1} {operator} {num2} = {result}")

def main():
    """Main function to run the program"""
    print("=== Welcome to Simple Python Program ===")
    
    # Greet the user
    user_name = greet_user()
    
    # Calculate age
    user_age = calculate_age()
    
    # Run calculator
    simple_calculator()
    
    # Say goodbye
    print(f"\nThank you for using our program, {user_name}!")
    print("Have a great day!")

if __name__ == "__main__":
    main()

