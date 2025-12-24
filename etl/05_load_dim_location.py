import pandas as pd
from db_connection import get_connection

df = pd.read_csv("data/raw/train.csv")

# Clean Postal Code
df["Postal Code"] = df["Postal Code"].fillna("UNKNOWN").astype(str)

locations = df[[
    "Country",
    "Region",
    "State",
    "City",
    "Postal Code"
]].drop_duplicates()

conn = get_connection()
cursor = conn.cursor()

query = """
INSERT INTO dim_location (country, region, state, city, postal_code)
VALUES (%s, %s, %s, %s, %s)
"""

for _, row in locations.iterrows():
    cursor.execute(query, (
        row["Country"],
        row["Region"],
        row["State"],
        row["City"],
        row["Postal Code"]
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ dim_location loaded")
