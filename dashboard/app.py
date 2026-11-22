"""Interactive dashboard for the synthetic UK retail dataset.

Run from the repository root:

    python dashboard/app.py

then open http://127.0.0.1:8050 in a browser.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Load data
products = pd.read_csv(DATA_DIR / "products.csv")
transactions = pd.read_csv(DATA_DIR / "transactions.csv")
line_items = pd.read_csv(DATA_DIR / "transaction_line_items.csv")
reviews = pd.read_csv(DATA_DIR / "reviews.csv")

# Sales by category
sales_cat = line_items.groupby("category")["line_total"].sum().reset_index()
fig_sales_cat = px.bar(
    sales_cat,
    x="category",
    y="line_total",
    color="category",
    title="Total Sales by Category",
    labels={"line_total": "Sales (£)", "category": "Category"},
)

# Average rating by category
avg_rating = reviews.merge(products[["product_id", "category"]], on="product_id")
avg_rating = avg_rating.groupby("category")["rating"].mean().reset_index()
fig_rating = px.bar(
    avg_rating,
    x="category",
    y="rating",
    color="category",
    title="Average Product Rating by Category",
    labels={"rating": "Mean rating (1-5)", "category": "Category"},
)

# Sales by month
transactions["tx_datetime"] = pd.to_datetime(transactions["tx_datetime"])
transactions["month"] = transactions["tx_datetime"].dt.to_period("M").astype(str)
monthly_sales = transactions.groupby("month")["order_total"].sum().reset_index()


def handle_partial_months(monthly_sales, transactions):
    """Keep only the months the transaction data covers from start to end.

    The transactions run from 9 Aug 2024 to 7 Aug 2025, so the first and
    last months hold only a few days of sales each and would appear as false
    dips in the monthly trend. Monthly totals are only comparable for whole
    months, so partial months are dropped rather than plotted.
    """
    first_day = transactions["tx_datetime"].min().normalize()
    last_day = transactions["tx_datetime"].max().normalize()

    months = pd.PeriodIndex(monthly_sales["month"], freq="M")
    starts_in_range = months.start_time >= first_day
    ends_in_range = months.end_time.normalize() <= last_day

    return monthly_sales[starts_in_range & ends_in_range].reset_index(drop=True)


monthly_sales = handle_partial_months(monthly_sales, transactions)
fig_monthly = px.line(
    monthly_sales,
    x="month",
    y="order_total",
    markers=True,
    title="Monthly Sales Trend (complete months only)",
    labels={"order_total": "Sales (£)", "month": "Month"},
)
# Start the axis at zero so month-to-month noise is shown in proportion.
fig_monthly.update_yaxes(rangemode="tozero")

# Dash app
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("UK Retail Analytics Dashboard"),
        html.P("All data is synthetic. See the README for how it was built."),
        html.Div(
            [
                html.Div(
                    dcc.Graph(figure=fig_sales_cat),
                    style={"width": "48%", "display": "inline-block"},
                ),
                html.Div(
                    dcc.Graph(figure=fig_rating),
                    style={"width": "48%", "display": "inline-block"},
                ),
            ]
        ),
        html.Div(dcc.Graph(figure=fig_monthly)),
    ]
)

if __name__ == "__main__":
    app.run()
