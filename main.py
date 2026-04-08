from tracker import (
    add_expense,
    view_expenses,
    monthly_summary,
    category_summary,
    predict_spending,
    highest_spending_category,
    show_charts,
    spending_warning
)

from charts import show_category_chart, show_monthly_chart


def menu():
    while True:
        print("\n Smart Expense Tracker ")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Predict Next Month Spending")
        print("6. Highest Spending Category")
        print("7. Show Charts")
        print("8. Exit")
        print("9. Spending Warning")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            monthly_summary()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            predict_spending()

        elif choice == "6":
            highest_spending_category()

        elif choice == "7":
            show_charts()
            show_category_chart()
            show_monthly_chart()

        elif choice == "8":
            print("Goodbye")
            break

        elif choice == "9":
            spending_warning()

        else:
            print("Invalid choice")


menu()
