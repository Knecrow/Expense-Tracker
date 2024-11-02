# List to store expenses
expenses = []

# Function to add an expense
def add_expense():
    name = input("Enter the expense name: ")
    try:
        amount = float(input("Enter the expense amount: "))
        if amount < 0:
            print("Amount cannot be negative. Try again.")
            return
    except ValueError:
        print("Please enter a valid number for amount.")
        return

    expenses.append({"name": name, "amount": amount})
    print(f"Expense '{name}' of ${amount:.2f} added successfully.\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses found!")
    else:
        print("Expenses:")
        total = 0
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
            total += expense['amount']
        print(f"Total Amount Spent: ${total:.2f}\n")

# Function to delete an expense
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    try:
        index = int(input("Enter the index of the expense to delete: "))
        if 1 <= index <= len(expenses):
            deleted_expense = expenses.pop(index - 1)
            print(f"Expense '{deleted_expense['name']}' deleted successfully.\n")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Please enter a valid index number.")

# Main loop for menu options
def main():
    option = None
    while option != 4:
        print("1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Exit")

        try:
            option = int(input("Choose an option: "))
            if option < 1 or option > 4:
                print("Please enter a valid option (1-4).")
                continue
        except ValueError:
            print("Please enter an integer value.")
            continue

        if option == 1:
            add_expense()
        elif option == 2:
            view_expenses()
        elif option == 3:
            delete_expense()
        elif option == 4:
            print("Exiting the Expense Tracker. Goodbye!")

# Run the program
main()
