def show_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit")

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def perform_calculation(choice, num1, num2):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            print("Division by zero is not allowed!")
            return None
    elif choice == "5":
        return num1 % num2
    elif choice == "6":
        return num1 ** num2

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == "7":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice in ["1", "2", "3", "4", "5", "6"]:
        num1, num2 = get_numbers()
        if num1 is not None and num2 is not None:
            result = perform_calculation(choice, num1, num2)
            if result is not None:
                print(f"Result: {result}")
    else:
        print("Invalid choice. Please select a valid option.")