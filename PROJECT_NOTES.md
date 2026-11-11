# Project Notes — Python Expense Tracker

## Objective

Build a small Python application that records expenses and summarizes spending.

## How it works

1. The program displays a menu.
2. The user chooses an action.
3. For adding an expense, the program asks for a category, amount, and optional note.
4. The expense is stored as a dictionary inside a list.
5. The user can view the list, total all amounts, or see totals grouped by category.
6. The program continues until the user selects Exit.

## Data structure

Each expense is stored as a dictionary, for example:

```python
{"category": "Food", "amount": 150.0, "note": "Lunch"}
```

All expense dictionaries are stored in the `expenses` list.

## Main functions

- `add_expense()`: collects and validates expense details.
- `view_expenses()`: displays recorded expenses.
- `show_total()`: calculates the total using `sum()`.
- `show_category_summary()`: groups amounts by category.
- `main()`: runs the menu loop and calls the selected function.

## Python concepts practised

| Concept | How it is used |
|---|---|
| Variables | Store category, amount, note, and menu choice |
| Input/output | Read user entries and display results |
| Lists | Store multiple expenses |
| Dictionaries | Store each expense's details |
| Functions | Organize the program into reusable tasks |
| While loop | Keep the menu running |
| If/elif/else | Handle menu choices |
| For loop | Display and summarize expenses |
| Exception handling | Handle non-numeric amounts |
| List/dictionary operations | Add records and group totals |

## Testing checklist

- [ ] Add a valid expense.
- [ ] Try an empty category.
- [ ] Try a negative amount.
- [ ] Try text instead of a numeric amount.
- [ ] View expenses.
- [ ] Check the total for multiple expenses.
- [ ] Check the category summary.
- [ ] Enter an invalid menu option.
- [ ] Exit the application.

## Possible future improvements

- Save expenses to a CSV or JSON file.
- Add dates to expenses.
- Allow users to delete or edit an expense.
- Add a monthly budget and budget alerts.
- Create charts of spending by category.
