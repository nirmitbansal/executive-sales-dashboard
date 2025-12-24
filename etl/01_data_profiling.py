import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/train.csv")

print("===== BASIC INFO =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isna().sum())

print("\n===== SAMPLE DATA =====")
print(df.head(3))
