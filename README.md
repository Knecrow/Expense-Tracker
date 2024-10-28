Code Overview:
Expense List:

Stores all expenses as a list of dictionaries, where each dictionary has name and amount keys.
Main Menu Loop:

Loops until the user chooses the option to exit.
Displays menu options:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit
Option 1: Add Expense:

Prompts user for expense name and amount.
Validates amount to ensure it’s a non-negative number.
Appends the expense to the list and confirms the addition.
Option 2: View Expenses:

Lists all expenses if any exist.
Shows each expense's name and amount and calculates the total amount spent.
Option 3: Delete Expense:

Allows the user to delete an expense by specifying its index in the list.
Validates index input and confirms deletion.
Option 4: Exit:

Ends the program with a goodbye message.
Error Handling:
Input validation ensures the program runs smoothly:
Checks if the user’s option choice is an integer between 1 and 4.
Validates that amount is a non-negative number.
Confirms the index for deletion is within range.
