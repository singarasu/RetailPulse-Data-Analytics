
import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
orders_path = base_path / "data" / "raw" / "olist_orders_dataset.csv"

orders = pd.read_csv(orders_path)

missing_delivery = orders[
    orders["order_delivered_customer_date"].isna()
]

print("Total orders:", len(orders))
print("Orders missing customer delivery date:", len(missing_delivery))

print("\nMissing delivery dates by order status:")
print(
    missing_delivery["order_status"]
    .value_counts()
)

print("\nDelivered orders missing delivery date:")
delivered_missing = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isna())
]

print(
    delivered_missing[
        [
            "order_id",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ].to_string(index=False)
)

items_path = base_path / "data" / "raw" / "olist_order_items_dataset.csv"
reviews_path = base_path / "data" / "raw" / "olist_order_reviews_dataset.csv"

items = pd.read_csv(items_path)
reviews = pd.read_csv(reviews_path)

item_counts = items.groupby("order_id").size()
review_counts = reviews.groupby("order_id").size()

delivered_missing = delivered_missing.copy()

delivered_missing["item_count"] = (
    delivered_missing["order_id"].map(item_counts).fillna(0).astype(int)
)

delivered_missing["review_count"] = (
    delivered_missing["order_id"].map(review_counts).fillna(0).astype(int)
)

print("\nVerification of 8 delivered orders:")
print(
    delivered_missing[
        [
            "order_id",
            "order_delivered_carrier_date",
            "item_count",
            "review_count"
        ]
    ].to_string(index=False)
)

review_details = reviews[
    reviews["order_id"].isin(delivered_missing["order_id"])
][
    [
        "order_id",
        "review_creation_date",
        "review_answer_timestamp"
    ]
]

print("\nReview date investigation:")
print(review_details.to_string(index=False))
