import pandas as pd
from db_connection import get_connection

df = pd.read_csv("data/raw/train.csv")

customers = df[["Customer ID", "Customer Name", "Segment"]].drop_duplicates()

conn = get_connection()
cursor = conn.cursor()

query = """
INSERT IGNORE INTO dim_customers (customer_id, customer_name, segment)
VALUES (%s, %s, %s)
"""

for _, row in customers.iterrows():
    cursor.execute(query, (
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ dim_customers loaded")
