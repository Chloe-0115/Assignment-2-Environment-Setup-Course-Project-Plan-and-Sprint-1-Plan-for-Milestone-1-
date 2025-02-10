from budget_manager import (
    read_budget_records, add_income, add_expense, delete_record, edit_record,
    calculate_budget_overview, set_savings_goal, get_savings_goal
)

AFFIRMATIONS_FILE = 'affirmations.txt'

def load_affirmations():
    """Load affirmations from the file."""
    affirmations = {}
    with open(AFFIRMATIONS_FILE, 'r') as file:
        for line in file:
            key, message = line.strip().split('=', 1)
            affirmations[key] = message
    return affirmations

affirmations = load_affirmations()

def display_welcome_message():
    """Display the welcome message."""
    print(affirmations['welcome_message'])

def display_help():
    """Display help information."""
    print(affirmations['help_message'])

def add_income_interface():
    """Interface for adding income."""
    try:
        amount = float(input("Enter the income amount: "))
        add_income(amount)
        print(affirmations['add_success'])
    except ValueError:
        print(affirmations['invalid_number'])

def add_expense_interface():
    """Interface for adding expenses."""
    method = input("Add expense by (1) Manual entry or (2) Picture of receipt: ")
    if method == '1':
        try:
            amount = float(input("Enter the expense amount: "))
            add_expense(amount)
            print(affirmations['add_success'])
        except ValueError:
            print(affirmations['invalid_number'])
    elif method == '2':
        print("Feature to add by picture is not implemented yet.")
    else:
        print(affirmations['invalid_choice'])

def delete_record_interface():
    """Interface for deleting a record."""
    records = read_budget_records()
    if not records:
        print(affirmations['no_records'].format(action='delete'))
        return

    display_records(records)

    try:
        index = int(input("Enter the number of the record to delete: ")) - 1
        if 0 <= index < len(records):
            confirm = input(affirmations['delete_confirmation'].format(record=records[index].strip()))
            if confirm.lower() == 'yes':
                delete_record(index)
                print(affirmations['delete_success'])
            else:
                print(affirmations['delete_cancelled'])
        else:
            print(affirmations['invalid_number'])
    except ValueError:
        print(affirmations['invalid_number'])

def edit_record_interface():
    """Interface for editing a record."""
    records = read_budget_records()
    if not records:
        print(affirmations['no_records'].format(action='edit'))
        return

    display_records(records)

    try:
        index = int(input("Enter the number of the record to edit: ")) - 1
        if 0 <= index < len(records):
            new_amount = float(input(f"Enter the new amount for '{records[index].strip()}': "))
            new_type = input("Enter the type (income/expense): ").strip().lower()
            if new_type in ['income', 'expense']:
                edit_record(index, new_amount, new_type)
                print(affirmations['edit_success'])
            else:
                print(affirmations['invalid_choice'])
        else:
            print(affirmations['invalid_number'])
    except ValueError:
        print(affirmations['invalid_number'])

def display_budget_overview():
    """Display the budget overview."""
    income, expenses = calculate_budget_overview()
    savings_goal = get_savings_goal()
    print("\nBudget Overview:")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Savings Goal: ${savings_goal:.2f}")
    print(f"Net Savings: ${income - expenses:.2f}")
    print(f"Progress towards Savings Goal: ${income - expenses - savings_goal:.2f}\n")

def set_savings_goal_interface():
    """Interface for setting a savings goal."""
    try:
        goal = float(input("Enter your savings goal: "))
        set_savings_goal(goal)
        print("Savings goal set successfully.")
    except ValueError:
        print(affirmations['invalid_number'])

def display_records(records):
    """Display the list of records."""
    print("Current Records:")
    for i, record in enumerate(records, start=1):
        amount, category = record.strip().split(',')
        formatted_amount = int(float(amount)) if float(amount).is_integer() else float(amount)
        print(f"{i}. {formatted_amount},{category}")