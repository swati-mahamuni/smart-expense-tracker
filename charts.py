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
            try:
                   amt = float(row["amount"])
            except ValueError:
             continue
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

import pandas as pd

def show_monthly_chart():
    try:
        df = pd.read_csv(FILE)

        if df.empty:
            print("No data to plot")
            return

        # ✅ Clean and fix data
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df["amount"] = pd.to_numeric(df["amount"], errors='coerce')

        # remove invalid rows
        df = df.dropna(subset=["date", "amount"])

        # ✅ Group by month
        monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

        # ✅ Convert index to proper datetime (IMPORTANT FIX)
        monthly.index = monthly.index.to_timestamp()

        # ✅ Sort correctly
        monthly = monthly.sort_index()

        # ✅ Plot
        plt.figure()
        plt.plot(monthly.index, monthly.values, marker="o")
        plt.title("Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Spending")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("monthly_spending.png")
        plt.show()

    except FileNotFoundError:
        print("expenses.csv file not found")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    show_category_chart()
    show_monthly_chart()