
import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

datasets = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}

for name, filename in datasets.items():

    file_path = raw_path / filename
    df = pd.read_csv(file_path)

    print("\n" + "=" * 50)
    print("Dataset:", name)
    print("Rows:", len(df))

    missing = df.isnull().sum()
    print("\nMissing Values:")
    print(missing[missing > 0])

    print("\nDuplicate Rows:", df.duplicated().sum())


orders = pd.read_csv(raw_path / "olist_orders_dataset.csv")

print("\nORDER STATUS ANALYSIS")
print(orders["order_status"].value_counts())

print("\nMissing Delivery Dates by Order Status")

print(
    orders.groupby("order_status")[
        [
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ].apply(lambda group: group.isnull().sum())
)
