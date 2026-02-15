import csv
import matplotlib.pyplot as plt
import pandas as pd




def show_charts():
    df = pd.read_csv("expenses.csv")

    # Category spending
    category_total = df.groupby("category")["amount"].sum()

    category_total.plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()






FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]

    print("\nSelect category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    choice = int(input("Enter category number: "))
    category = categories[choice - 1]

    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE, "r") as f:
        for row in f:
            print(row.strip())


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"].startswith(month):
                total += float(row["amount"])

    print("Total spending:", total)


def category_summary():
    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            data[cat] = data.get(cat, 0) + amt

    for k, v in data.items():
        print(k, ":", v)


def predict_spending():
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
        print("Predicted next month spending:", round(predicted, 2))


def highest_spending_category():
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

    highest = max(data, key=data.get)
    print(f"You spend most on: {highest} ({data[highest]})")



# -----------------------------------------------

# Smart Spending Warning System

def spending_warning():
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

    highest = max(data, key=data.get)

    # warning rule (you can change limit)
    if data[highest] > 2000:
        print("⚠ WARNING: Very high spending on", highest)
    else:
        print("Spending is under control 👍")
