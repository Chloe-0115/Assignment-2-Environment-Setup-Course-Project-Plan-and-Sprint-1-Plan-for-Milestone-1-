import os

BUDGET_FILE = 'budget_records.txt'
SAVINGS_GOAL_FILE = 'savings_goal.txt'

def read_budget_records():
    """Read budget records from the file."""
    if not os.path.exists(BUDGET_FILE):
        return []
    with open(BUDGET_FILE, 'r') as file:
        return file.readlines()

def write_budget_records(records):
    """Write budget records to the file."""
    with open(BUDGET_FILE, 'w') as file:
        file.writelines(records)

def add_income(amount):
    """Add an income record."""
    records = read_budget_records()
    records.append(f"{amount},income\n")
    write_budget_records(records)

def add_expense(amount):
    """Add an expense record."""
    records = read_budget_records()
    records.append(f"{amount},expense\n")
    write_budget_records(records)

def delete_record(index):
    """Delete a record by index."""
    records = read_budget_records()
    if 0 <= index < len(records):
        del records[index]
        write_budget_records(records)

def edit_record(index, new_amount, new_type):
    """Edit a record by index."""
    records = read_budget_records()
    if 0 <= index < len(records):
        records[index] = f"{new_amount},{new_type}\n"
        write_budget_records(records)

def calculate_budget_overview():
    """Calculate total income and expenses."""
    records = read_budget_records()
    income = 0
    expenses = 0

    for record in records:
        try:
            amount, category = record.strip().split(',')
            amount = float(amount)
            if category.lower() == 'income':
                income += amount
            elif category.lower() == 'expense':
                expenses += amount
        except ValueError:
            continue

    return income, expenses

def set_savings_goal(goal):
    """Set the savings goal."""
    with open(SAVINGS_GOAL_FILE, 'w') as file:
        file.write(str(goal))

def get_savings_goal():
    """Get the current savings goal."""
    if not os.path.exists(SAVINGS_GOAL_FILE):
        return 0
    with open(SAVINGS_GOAL_FILE, 'r') as file:
        return float(file.read().strip())