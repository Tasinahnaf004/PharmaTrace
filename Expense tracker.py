import csv

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Expenses:")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")
        print()
    except FileNotFoundError:
        print("No expenses found.\n")


def total_spending():
    total = 0
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"\nTotal Spending: {total}\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def filter_by_category():
    search_category = input("Enter category to filter: ")
    found = False

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1].lower() == search_category.lower():
                    print(f"Date: {row[0]}, Amount: {row[2]}")
                    found = True

        if not found:
            print("No matching category found.\n")
        else:
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.\n")


main()