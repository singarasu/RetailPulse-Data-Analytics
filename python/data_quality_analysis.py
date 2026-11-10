import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

print(f"Total datasets found: {len(csv_files)}")

for file in csv_files:
    df = pd.read_csv(file)

    total_rows = len(df)
    total_columns = len(df.columns)

    missing_cells = df.isnull().sum().sum()
    missing_percentage = (
        missing_cells / (total_rows * total_columns)
    ) * 100

    duplicate_rows = df.duplicated().sum()
    duplicate_percentage = (
        duplicate_rows / total_rows
    ) * 100

    print("\n" + "=" * 75)
    print(f"Dataset: {file.name}")
    print(f"Rows: {total_rows:,}")
    print(f"Columns: {total_columns}")
    print(f"Missing Cells: {missing_cells:,}")
    print(f"Missing Percentage: {missing_percentage:.2f}%")
    print(f"Duplicate Rows: {duplicate_rows:,}")
    print(f"Duplicate Percentage: {duplicate_percentage:.2f}%")

    primary_keys = {
    "olist_customers_dataset.csv": ["customer_id"],
    "olist_orders_dataset.csv": ["order_id"],
    "olist_order_items_dataset.csv": ["order_id", "order_item_id"],
    "olist_order_payments_dataset.csv": ["order_id", "payment_sequential"],
    "olist_order_reviews_dataset.csv": ["review_id"],
    "olist_products_dataset.csv": ["product_id"],
    "olist_sellers_dataset.csv": ["seller_id"],
    "product_category_name_translation.csv": ["product_category_name"]
}

for file_name, key_columns in primary_keys.items():
    file_path = data_path / file_name
    df = pd.read_csv(file_path)

    duplicate_keys = df.duplicated(subset=key_columns).sum()

    print("\n" + "=" * 75)
    print(f"Dataset: {file_name}")
    print(f"Primary Key Columns: {key_columns}")
    print(f"Duplicate Key Records: {duplicate_keys}")

    if duplicate_keys == 0:
        print("Status: Primary key uniqueness check passed")
    else:
        print("Status: Duplicate key values found")

    reviews = pd.read_csv(data_path / "olist_order_reviews_dataset.csv")

duplicate_reviews = reviews[
    reviews.duplicated(subset=["review_id"], keep=False)
]

print("\nDUPLICATE REVIEW ID ANALYSIS")
print(f"Total affected rows: {len(duplicate_reviews)}")
print(f"Unique duplicate review IDs: {duplicate_reviews['review_id'].nunique()}")

print("\nSample duplicate records:")
print(
    duplicate_reviews
    .sort_values("review_id")
    .head(10)
    .to_string(index=False)
)

datasets_to_check = [
    "olist_orders_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv"
]

for file_name in datasets_to_check:
    df = pd.read_csv(data_path / file_name)

    print(f"\nMISSING VALUE ANALYSIS: {file_name}")

    missing_counts = df.isnull().sum()

    print(missing_counts[missing_counts > 0])

    orders = pd.read_csv(data_path / "olist_orders_dataset.csv")

print("\nORDER STATUS VS MISSING DELIVERY DATES")

for column in [
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date"
]:
    print(f"\nMissing {column}:")
    print(
        orders[orders[column].isnull()]
        ["order_status"]
        .value_counts(dropna=False)
    )

products = pd.read_csv(data_path / "olist_products_dataset.csv")

print("\nPRODUCT MISSING VALUE PATTERNS")

missing_products = products[products.isnull().any(axis=1)]

print(f"Products with missing information: {len(missing_products)}")
print(missing_products.isnull().sum())

products = pd.read_csv(data_path / "olist_products_dataset.csv")

missing_category = products[
    products["product_category_name"].isnull()
]

missing_physical_data = products[
    products["product_weight_g"].isnull()
]

print("\nPRODUCT DATA INVESTIGATION")

print(f"Products without category: {len(missing_category)}")
print(f"Products without physical data: {len(missing_physical_data)}")

print("\nSample products without category:")
print(
    missing_category[
        ["product_id", "product_category_name",
         "product_name_lenght", "product_description_lenght",
         "product_photos_qty"]
    ].head(10).to_string(index=False)
)

print("\nProducts without physical data:")
print(
    missing_physical_data[
        ["product_id", "product_weight_g", "product_length_cm",
         "product_height_cm", "product_width_cm"]
    ].to_string(index=False)
)