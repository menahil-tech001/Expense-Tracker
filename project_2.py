
expenses = []


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print("\nExpense", i)
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])


def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Spent:", total)


def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    for category, total in summary.items():
        print(category, ":", total)


def update_expense():
    view_expenses()

    if not expenses:
        return

    index = int(input("Enter expense number to update: ")) - 1

    if 0 <= index < len(expenses):
        expenses[index]["amount"] = float(input("Enter new amount: "))
        expenses[index]["category"] = input("Enter new category: ")
        expenses[index]["description"] = input("Enter new description: ")
        print("Expense updated successfully!")
    else:
        print("Invalid expense number.")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted successfully!")
    else:
        print("Invalid expense number.")


while True:
    print("\nEXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category Summary")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        update_expense()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
