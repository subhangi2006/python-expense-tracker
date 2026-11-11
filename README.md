# Python Expense Tracker

A beginner-friendly, menu-driven command-line application built with Python. It helps users record expenses, view their expense history, calculate total spending, and see spending grouped by category.

## Features

- Add an expense with a category, amount, and optional note
- View all expenses entered during the current session
- Calculate total spending
- View totals for each expense category
- Validate amounts and menu choices

## Requirements

- Python 3.8 or later
- No external libraries are required

## Run the project

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python expense_tracker.py
   ```

   On some Windows installations, use `py expense_tracker.py`.

## Example

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add an expense
2. View all expenses
3. Show total spending
4. Show category summary
5. Exit
Choose an option (1-5): 1
Enter expense category: Food
Enter amount (INR): 150
Enter a short note (optional): Lunch
Expense added successfully!
```

## Concepts used

- Variables and data types
- Lists and dictionaries
- Functions
- Loops and conditional statements
- User input and output
- Exception handling
- Basic calculations and aggregation

## Current limitation

Expenses are stored in memory and are cleared when the program exits. Saving data permanently to a file is a possible future improvement.

## Author

Subhangi Panda

## Internship task

Python project: build a simple project and upload the completed source code to GitHub.
