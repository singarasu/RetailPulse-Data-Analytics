
import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent
products_path = base_path / "data" / "raw" / "olist_products_dataset.csv"

products = pd.read_csv(products_path)

print("Total products:", len(products))

missing_summary = products.isna().sum()
missing_summary = missing_summary[missing_summary > 0]

print("\nMissing values:")
print(missing_summary)

print("\nProducts missing category:")
print(products["product_category_name"].isna().sum())

print("\nProducts missing physical dimensions:")
dimension_columns = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

print(products[dimension_columns].isna().any(axis=1).sum())

print("\nMissing value combinations:")
print(
    products[
        products.isna().any(axis=1)
    ][
        ["product_id", "product_category_name"] + dimension_columns
    ].to_string(index=False)
)
