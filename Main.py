# List to store expenses
expenses = []

# Initialize option to None to enter the loop
option = None

# Start main loop for menu options
while option != 4:
    print("1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")

    # Get user input for menu selection
    try: 
        option = int(input("Choose an option: "))
        if option < 1 or option > 4:
            print("Please enter a valid option (1-4).")
            continue  # Skip the rest if option is invalid
    except ValueError:
        print("Please enter an integer value.")
        continue

    # Option 1: Add an expense
    if option == 1:
        # Input for expense name
        name = input("Enter the expense name: ")
        
        # Input for expense amount with error handling
        try:
            amount = float(input("Enter the expense amount: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number for amount.")
            continue

        # Add expense to the list
        expenses.append({"name": name, "amount": amount})
        print(f"Expense '{name}' of ${amount:.2f} added successfully.\n")

    # Option 2: View all expenses
    elif option == 2:
        if not expenses:  # Check if there are no expenses
            print("No expenses found!")
        else:
            print("Expenses:")
            total = 0
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
                total += expense['amount']
            print(f"Total Amount Spent: ${total:.2f}\n")

    # Option 3: Delete an expense
    elif option == 3:
        if not expenses:
            print("No expenses to delete.")
            continue
        try:
            # Input index of expense to delete
            index = int(input("Enter the index of the expense to delete: "))
            if 1 <= index <= len(expenses):
                deleted_expense = expenses.pop(index - 1)
                print(f"Expense '{deleted_expense['name']}' deleted successfully.\n")
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Please enter a valid index number.")

    # Option 4: Exit the program
    elif option == 4:
        print("Exiting the Expense Tracker. Goodbye!")
