import pandas as pd
from db_connection import get_connection

df = pd.read_csv("data/raw/train.csv")

products = df[[
    "Product ID",
    "Product Name",
    "Category",
    "Sub-Category"
]].drop_duplicates()

conn = get_connection()
cursor = conn.cursor()

query = """
INSERT IGNORE INTO dim_products (product_id, product_name, category, sub_category)
VALUES (%s, %s, %s, %s)
"""

for _, row in products.iterrows():
    cursor.execute(query, (
        row["Product ID"],
        row["Product Name"],
        row["Category"],
        row["Sub-Category"]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ dim_products loaded")
