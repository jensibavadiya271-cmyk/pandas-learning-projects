import pandas as pd

print("STEP 1")

df = pd.read_excel(
    r"E:\Pandas\Bank_Transactions_Data.xlsx",
    engine="openpyxl"
)

print("STEP 2")

print(df["Transaction_Mode"].value_counts())

print("STEP 3")