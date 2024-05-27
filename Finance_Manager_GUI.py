import tkinter as tk
from tkinter import messagebox, simpledialog

class Transaction:
    """
    Represents a single financial transaction.
    """

    def __init__(self, date, description, amount):
        """
        Initializes a transaction with date, description, and amount.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.date = date
        self.description = description
        self.amount = amount

class FinanceManager:
    """
    Manages financial transactions and provides functionalities to add transactions, view transaction history, and calculate balance.
    """

    def __init__(self):
        """
        Initializes the FinanceManager with an empty list of transactions.
        """
        self.transactions = []

    def add_transaction(self, date, description, amount):
        """
        Adds a new transaction to the list.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.transactions.append(Transaction(date, description, amount))
        print("Transaction added successfully!")

    def view_transactions(self):
        """
        Displays the transaction history.
        """
        if self.transactions:
            transaction_history = "\nTransaction History:\n"
            for transaction in self.transactions:
                transaction_history += f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}\n"
            return transaction_history
        else:
            return "Your transaction history is empty!"

    def calculate_balance(self):
        """
        Calculates the total income, total expenses, and current balance.
        """
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        balance = total_income + total_expenses
        return f"Total Income: {total_income}\nTotal Expenses: {total_expenses}\nCurrent Balance: {balance}"

class FinanceManagerApp:
    """
    GUI application for managing personal finances using tkinter.
    """

    def __init__(self, root):
        self.finance_manager = FinanceManager()

        root.title("Personal Finance Manager")

        # Date
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        # Description
        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        # Amount
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # Buttons
        self.add_income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_button.pack(pady=5)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=5)

        self.view_transactions_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack(pady=5)

        self.calculate_balance_button = tk.Button(root, text="Calculate Balance", command=self.calculate_balance)
        self.calculate_balance_button.pack(pady=5)

    def add_income(self):
        """Handles adding income transactions."""
        date = self.date_entry.get()
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            self.finance_manager.add_transaction(date, description, amount)
            messagebox.showinfo("Success", "Income added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def add_expense(self):
        """Handles adding expense transactions."""
        date = self.date_entry.get()
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            self.finance_manager.add_transaction(date, description, -amount)
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def view_transactions(self):
        """Displays the transaction history."""
        transactions = self.finance_manager.view_transactions()
        messagebox.showinfo("Transaction History", transactions)

    def calculate_balance(self):
        """Calculates and displays the current balance."""
        balance_info = self.finance_manager.calculate_balance()
        messagebox.showinfo("Balance Information", balance_info)

def main():
    """Main function to run the Personal Finance Manager GUI application."""
    root = tk.Tk()
    app = FinanceManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
