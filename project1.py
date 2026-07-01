# ==========================================
# Project 1: Simple Calculator with History
# ==========================================

# List to store calculation history
history = []

# --------------------------
# Arithmetic Functions
# --------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# --------------------------
# Function to Display Menu
# --------------------------

def show_menu():
    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Exit")

# --------------------------
# Function to Store History
# --------------------------

def save_history(expression, result):
    history.append({
        "Calculation": expression,
        "Result": result
    })

# --------------------------
# Function to View History
# --------------------------

def view_history():
    if len(history) == 0:
        print("\nNo calculations performed yet.")
    else:
        print("\n------ Calculation History ------")
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item['Calculation']} = {item['Result']}")

# --------------------------
# Main Program
# --------------------------

while True:

    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("\nThank you for using the calculator!")
        break

    elif choice == "5":
        view_history()
        continue

    elif choice in ["1", "2", "3", "4"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                expression = f"{num1} + {num2}"

            elif choice == "2":
                result = subtract(num1, num2)
                expression = f"{num1} - {num2}"

            elif choice == "3":
                result = multiply(num1, num2)
                expression = f"{num1} * {num2}"

            elif choice == "4":
                result = divide(num1, num2)
                expression = f"{num1} / {num2}"

            print("Result =", result)

            save_history(expression, result)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select between 1 and 6.")