from user_interface import (
    display_welcome_message, display_help, add_income_interface, add_expense_interface,
    delete_record_interface, edit_record_interface, display_budget_overview, set_savings_goal_interface
)

def main():
    """Main function to run the budget app."""
    display_welcome_message()
    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Delete Record")
        print("4. Edit Record")
        print("5. View Budget Overview")
        print("6. Set Savings Goal")
        print("7. Help")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_income_interface()
        elif choice == '2':
            add_expense_interface()
        elif choice == '3':
            delete_record_interface()
        elif choice == '4':
            edit_record_interface()
        elif choice == '5':
            display_budget_overview()
        elif choice == '6':
            set_savings_goal_interface()
        elif choice == '7':
            display_help()
        elif choice == '8':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()