# Title: "Smart Budget Tracker"
# Objective: Create a Python program that tracks a user's expenses and generates reports on their spending habits.
# Requirements:
# Users should be able to input different expenses with categories (e.g. food, transportation, entertainment, etc.)
# Users should be able to view their expenses and the total amount spent in each category
# Users should be able to view their overall spending and the total amount saved
# The program should provide a monthly spending report and an annual report
# The program should be able to suggest a budget for each category based on the user's expenses
#
# Skills required:
# Basic knowledge of Python programming
# Understanding of data structures (lists, dictionaries)
# Ability to use classes and objects in Python
# Understanding of file operations (read and write to a file)
# Ability to use built-in Python libraries such as csv and date time.
# This project will challenge you to apply your knowledge of Python to real-world problems and help
# learn how to structure a complex program while implementing various data structures and algorithms.
# Good luck!


class Expenses:
    def __init__(self, food_amount, transport_amount, entertainment_amount):
        self.__budget_available = {"food": food_amount, "transportation": transport_amount, "entertainment": entertainment_amount}
        self.__expenses = {"food": 0, "transportation": 0, "entertainment": 0}

    # Users should be able to input different expenses with categories (e.g. food, transportation, entertainment, etc.)
    def add_expense(self, key, value):
        self.__budget_available[key] = self.__budget_available[key] - value
        self.__expenses[key] = self.__expenses[key] + value

    # Users should be able to view their expenses and the total amount spent in each category
    def view_expenses(self):
        print(f"Expenses: {self.__expenses}")

    # Users should be able to view their overall spending and the total amount saved
    def view_overall_spending(self):
        print(f"Overall Spending: {self.__expenses}")
        print(f"Total amount saved: {self.__budget_available}")


budget_food_amount = 345
budget_transport_amount = 2000
budget_entertainment_amount = 1300
expenses = Expenses(budget_food_amount, budget_transport_amount, budget_entertainment_amount)
expenses.add_expense("food", 45)
expenses.view_overall_spending()
