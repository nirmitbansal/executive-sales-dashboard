import pandas as pd
from db_connection import get_connection

# Load CSV
df = pd.read_csv("data/raw/train.csv")

# Fix dates
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Fix postal code
df["Postal Code"] = df["Postal Code"].fillna("UNKNOWN").astype(str)

conn = get_connection()
cursor = conn.cursor()

# Helper: get location_id
def get_location_id(row):
    query = """
    SELECT location_id FROM dim_location
    WHERE country=%s AND region=%s AND state=%s AND city=%s AND postal_code=%s
    """
    cursor.execute(query, (
        row["Country"],
        row["Region"],
        row["State"],
        row["City"],
        row["Postal Code"]
    ))
    result = cursor.fetchone()
    return result[0] if result else None

insert_query = """
INSERT INTO fact_sales (
    order_id, order_date, ship_date,
    customer_id, product_id, location_id, sales
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    location_id = get_location_id(row)

    cursor.execute(insert_query, (
        row["Order ID"],
        row["Order Date"].date(),
        row["Ship Date"].date(),
        row["Customer ID"],
        row["Product ID"],
        location_id,
        row["Sales"]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ fact_sales loaded")
