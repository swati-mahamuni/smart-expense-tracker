import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

FILE = "expenses.csv"


# create file if not exists
def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "description"])


def add_expense():
    ensure_file()  #make sure csv exists

# validate date input
    while True:
        date = input("Enter date (yyyy-mm-dd): ")
        try:
            year, month, day = map(int, date.split("-"))
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
            else:
                print("Invalid month or day. Try again.")
        except:
            print("Invalid format! Please enter date as YYYY-MM-DD.")

# Category selection
    categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]
    print("\nSelect category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            else:
                print("Please enter a number between 1 and", len(categories))
        except ValueError:
            print("Invalid input! Please enter a number.")

# Amount input
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

# Description input
    desc = input("Enter description: ")

# Write to CSV
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])

    print("Expense added successfully...")

def view_expenses():
    ensure_file()
    with open(FILE, "r") as f:
        for row in f:
            print(row.strip())


def monthly_summary():
    ensure_file()
    month = input("Enter month (yyyy-mm): ")
    total = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"].startswith(month):
                total += float(row["amount"])

    print("Total spending:", total)


def category_summary():
    ensure_file()
    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            data[cat] = data.get(cat, 0) + amt

    if not data:
        print("No data available")
        return

    for k, v in data.items():
        print(k, ":", v)


def predict_spending():
    ensure_file()
    total = 0
    count = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["amount"])
            count += 1

    if count == 0:
        print("No data available")
    else:
        avg = total / count
        predicted = avg * 30
        print("Predicted nex month spending:", round(predicted, 2))


def highest_spending_category():
    ensure_file()
    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            data[cat] = data.get(cat, 0) + amt

    if not data:
        print("no data available")
        return

    highest = max(data, key=data.get)
    print("you spend most on:", highest, "(", data[highest], ")")


def show_charts():
    ensure_file()

    df = pd.read_csv(FILE)

    if df.empty:
        print("no data to plot")
        return

    category_total = df.groupby("category")["amount"].sum()

    category_total.plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()


def spending_warning():
    ensure_file()
    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            data[cat] = data.get(cat, 0) + amt

    if not data:
        print("no data available")
        return

    highest = max(data, key=data.get)

    if data[highest] > 2000:
        print("Warning: Very high spending on", highest)
    else:
        print("Spending is under control")
