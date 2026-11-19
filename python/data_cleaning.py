
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

print("\nORDER STATUS ANALYSIS")
print(orders["order_status"].value_counts())

print("\nMissing Delivery Dates by Order Status")

missing_by_status = orders.groupby("order_status")[
    [
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date"
    ]
].apply(lambda group: group.isnull().sum())

print(missing_by_status.to_string())

delivered_orders = orders[orders["order_status"] == "delivered"]

print("Delivered Orders:", len(delivered_orders))
print(
    "Missing Customer Delivery Date:",
    delivered_orders["order_delivered_customer_date"].isnull().sum()
)

reviews = pd.read_csv(raw_path / "olist_order_reviews_dataset.csv")

print("\nREVIEW ANALYSIS")

print("Total Reviews:", len(reviews))

print("\nMissing Review Titles:",
      reviews["review_comment_title"].isnull().sum())

print("Missing Review Messages:",
      reviews["review_comment_message"].isnull().sum())

print("\nReview Scores:")
print(reviews["review_score"].value_counts().sort_index())

products = pd.read_csv(raw_path / "olist_products_dataset.csv")

print("\nPRODUCT ANALYSIS")

print("Total Products:", len(products))

print("\nMissing Values:")
print(products.isnull().sum()[products.isnull().sum() > 0])

print("\nProducts Missing Category:",
      products["product_category_name"].isnull().sum())

print("\nProducts Missing Dimensions:",
      products[["product_weight_g", "product_length_cm",
                "product_height_cm", "product_width_cm"]].isnull().any(axis=1).sum())

missing_category = products[products["product_category_name"].isnull()]

print("\nMISSING CATEGORY PRODUCT DETAILS")
print("Total:", len(missing_category))

print("\nMissing Values Count:")
print(missing_category.isnull().sum())

print("\nSample Records:")
print(missing_category.head(5).to_string())

geo = pd.read_csv(raw_path / "olist_geolocation_dataset.csv")

print("\nGEOLOCATION ANALYSIS")

print("Total Rows:", len(geo))
print("Exact Duplicate Rows:", geo.duplicated().sum())

print("\nDuplicate ZIP Code Prefixes:")
print(geo["geolocation_zip_code_prefix"].duplicated().sum())

print("\nUnique ZIP Code Prefixes:")
print(geo["geolocation_zip_code_prefix"].nunique())

print("\nSample Duplicate Records:")
print(
    geo[geo.duplicated(
        subset=["geolocation_zip_code_prefix"],
        keep=False
    )].head(10).to_string()
)