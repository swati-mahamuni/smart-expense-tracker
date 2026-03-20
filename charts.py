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

import pandas as pd
import matplotlib.pyplot as plt

def show_monthly_chart():
    try:
        df = pd.read_csv("expenses.csv")

        if df.empty:
            print("No data to plot")
            return

        # convert to datetime
        df["date"] = pd.to_datetime(df["date"])

        # group by month
        monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

        # convert index to string for plotting
        monthly.index = monthly.index.astype(str)

        # sort values (VERY IMPORTANT)
        monthly = monthly.sort_index()

        # plot
        plt.plot(monthly.index, monthly.values, marker="o")
        plt.title("Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Spending")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("monthly_spending.png")
        plt.show()

    except Exception as e:
        print("Error:", e)