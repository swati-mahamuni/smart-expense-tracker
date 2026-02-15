import csv
import os
import matplotlib.pyplot as plt

FILE = "expenses.csv"


def file_exists():
    return os.path.exists(FILE)


def show_category_chart():
    if not file_exists():
        print("No data file found")
        return

    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            data[cat] = data.get(cat, 0) + amt

    if not data:
        print("No data to plot")
        return

    plt.bar(data.keys(), data.values())
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("category_spending.png")
    plt.show()


def show_monthly_chart():
    if not file_exists():
        print("no data file found")
        return

    data = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            month = row["date"][:7]
            amt = float(row["amount"])
            data[month] = data.get(month, 0) + amt

    if not data:
        print("No data to plot")
        return

    plt.plot(list(data.keys()), list(data.values()), marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_spending.png")
    plt.show()
