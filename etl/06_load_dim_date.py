import pandas as pd
from db_connection import get_connection

df = pd.read_csv("data/raw/train.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

dates = df["Order Date"].drop_duplicates()

date_records = []

for d in dates:
    date_records.append((
        d.date(),
        d.year,
        d.month,
        (d.month - 1) // 3 + 1,
        d.day
    ))

conn = get_connection()
cursor = conn.cursor()

query = """
INSERT INTO dim_date (date, year, month, quarter, day)
VALUES (%s, %s, %s, %s, %s)
"""

for record in date_records:
    cursor.execute(query, record)

conn.commit()
cursor.close()
conn.close()

print("✅ dim_date loaded")
