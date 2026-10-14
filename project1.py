
# Section 1: Reading & Exploring Data

# Q1. Read the file Bank_Transactions_Data.xlsx into a DataFrame.
import pandas as pd
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df)

# # Q2. Display the first 5 rows of the dataset
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("The first 5 rows : ",df.head(5))

# # Q3. Display the first 25 rows of the dataset.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("The first 25 rows :",df.head(25))

# # Q4. Display the last 5 rows of the dataset
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("The last 5 rows :",df.tail(5))

# # Q5. Display the last 20 rows of the dataset.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("The last 20 rows :",df.tail(20))

# # Q6. Find the total number of rows and column
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Total rows :",df.shape[0])
# print("Total columns :",df.shape[1])

# # Q7. Display all column names of the dataset.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Columns name :",df.columns)

# # Q8. Display column data types, non-null counts, and memory usage
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Information of data :",df.info())

# # Q9. Display the statistical summary of all numeric columns.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Statistical summary :",df.describe())

# # Q10. Count how many transactions exist for each Transaction_Mode.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Transaction_Mode"].value_counts())

# # Q11. Count how many customers belong to each Account_Type.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Account_Type"].value_counts())

# # Q12. Find the number of unique branches in the Branch_Code column.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Unique value :",df["Branch_Code"].nunique())

# # Q13. Display all unique values of the KYC_Status column.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("All unique value :",df["KYC_Status"].unique())

# # Q14. Check only the data type of every column.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("All data type :",df.dtypes)

# # Q15. Display any 10 random transactions from the dataset.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Random transaction :",df.sample(10))

# # Section 2: Selecting Data

# # Q16. Select only the Customer_Name column.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Customer name :",df["Customer_Name"])

# # Q17. Select Transaction_ID, Transaction_Amount, and City columns together.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Columns :",df[["Transaction_ID","Transaction_Amount","City"]])

# # Q18. Select the first transaction using position.
# # # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("First transaction :",df.iloc[0])

# # Q19. Select the row with index label 1000.
# # # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print("Row with label 1000 :",df.loc[1000])

# # Q20. Select rows from position 50 to 60.
# print("Row from 50 to 60 :",df.iloc[50:61])

# Q21. Select rows 0 to 200 with only Customer_Name and Credit_Score using labels.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.loc[0:200,["Customer_Name","Credit_Score"]])

# # Q22. Select the value at row position 10 and column position 5.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.iloc[10,5])

# # Q23. Select every 5th row from the first 100 rows.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.iloc[0:100:5])

# # Q24. Select the last 20 rows using negative indexing.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.iloc[-20:])

# Q25. Select only the first 6 columns for all rows.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.iloc[:,0:6])

# Q26. Select the Credit_Score of the customer at row label 555.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.loc[555,"Credit_Score"])

# Q27. Select all columns from Account_Type to Merchant_Category using labels.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.loc[:,"Account_Type":"Merchant_Category"])

# Section 3: Sorting Data

# # Q28. Sort the dataset by Transaction_Amount in ascending order.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df = df.sort_values("Transaction_Amount", ascending=True)
# print(df)

# # Q29. Sort the dataset by Transaction_Amount in descending order.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df = df.sort_values("Transaction_Amount", ascending=False)
# print(df)

# # Q30. Sort customers by Credit_Score from highest to lowest.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# df = df.sort_values("Credit_Score", ascending=False)
# print(df)

# # Q31. Sort the dataset by Customer_Name alphabetically.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_values("Customer_Name",ascending=True)
# print(df)

# # Q32. Sort by Account_Type first and then by Transaction_Amount within each type.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_values(["Account_Type","Transaction_Amount"],ascending=True)
# print(df)

# # Q33. Sort by City ascending and Balance_After_Transaction descending together.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_values(["City","Balance_After_Transaction"],
#                 ascending=[True,False])
# print(df)

# # Q34. Sort the dataset by its index.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_index(ascending=True)
# print(df)

# # Q35. Sort the dataset by index in descending order.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_index(ascending=False)
# print(df)

# #Q36. Sort by Credit_Score and place all NaN values at the top.
# # df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.sort_values("Credit_Score",na_position="first")
# print(df)

# # Q37. Find the top 10 highest-value transactions.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df = df.sort_values("Transaction_Amount",ascending=False)
# print(df.head(10))

# # Section 4: Filtering Data
# # Q38. Filter all transactions above 100000.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df[df["Transaction_Amount"] > 100000]
# print(result)

# # Q39. Filter all transactions from the city Ahmedabad.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["City"] == "Ahmedabad"]
# print(result)

# # Q40. Filter all customers with Credit_Score greater than or equal to 750.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Credit_Score"] >= 750]
# print(result)

# # Q41. Filter all customers whose Age is below 25.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Age"] < 25]
# print(result)

# # Q42. Filter Savings account transactions above 50000 (both conditions).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df[(df["Account_Type"] == "Savings") & (df["Transaction_Amount"] > 50000)]
# print(result)

# # Q43. Filter transactions done through ATM or Cheque.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Transaction_Mode"].isin(["ATM","Cheque"])]
# print(result)

# # Q44. Filter customers from Surat, Rajkot, or Vadodara.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["City"].isin(["Surat","Rajkot","Vadodara"])]
# print(result)

# # Q45. Filter transactions where amount is between 10000 and 100000.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df[df["Transaction_Amount"].between(10000,100000)]

# # Q46. Filter customers whose Credit_Score is between 700 and 800.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Credit_Score"].between(700,800)]
# print(result)

# # Q47. Filter transactions that are either from Mumbai or above 200000 (any one).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df[(df["City"] == "Mumbai") | (df["Transaction_Amount"] > 200000)]
# print(result)

# # Q48. Filter all transactions NOT done through UPI.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Transaction_Mode"] != "UPI"]
# print(result)

# # Q49. Filter Salaried customers with income above 1000000 using a query string.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.query("Employment_Type == 'Salaried' and Transaction_Amount > 1000000")
# print(result)

# # Q50. Hide (replace with NaN) all Transaction_Amount values below 500.
# import numpy as np
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df.loc[df["Transaction_Amount"] < 500, "Transaction_Amount"] = np.nan
# print(df)

# # Q51. Keep only rows where Age is between 18 and 100 (valid ages).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[df["Age"].between(18,100)]
# print(result)

# # Section 5: Handling Missing Values

# # Q52. Check which cells of the dataset are missing.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.isna())

# # Q53. Count total missing values in every column.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.isnull().sum())

# # Q54. Check which cells are NOT missing.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.notna())

# # Q55. Count missing values only in the Loan_Amount column.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Loan_Amount"].isnull().sum())

# # Q56. Remove all rows containing any missing value.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.dropna())

# # Q57. Remove rows only where Email is missing.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.dropna(subset="Email"))

# # Q58. Remove columns that contain any missing value.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.dropna(axis=1))

# # Q59. Fill missing Loan_Type values with 'No Loan'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Loan_Type"] = df["Loan_Type"].mask(
#     df["Loan_Type"].isna(),
#     "No Loan"
# )
# print(df)

# # Q60. Fill missing Credit_Score values with the average credit score.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = df["Credit_Score"].fillna(df["Credit_Score"].mean())
# print(df)

# # Q61. Fill missing Loan_Amount values with 0.
# df["Loan_Amount"] = df["Loan_Amount"].fillna(0)
# print(df)

# # Q62. Fill missing Balance_After_Transaction using the previous row's value.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Balanced_After"] = df["Balance_After_Transaction"].ffill()
# print(df[["Balance_After_Transaction","Balanced_After"]])

# # Q63. Fill missing Balance_After_Transaction using the next row's value.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Balanced_Transaction"] = df["Balance_After_Transaction"].bfill()
# print(df[["Balance_After_Transaction","Balanced_Transaction"]])

# # Q64. Fill missing numeric values using interpolation.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# numeric_cols = df.select_dtypes(include="number").columns

# df[numeric_cols] = df[numeric_cols].interpolate()

# print(df)

# # Q65. Replace all 1200 values in Credit_Score with NaN.
# import numpy as np
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df["Credit_Score"].replace(1200,np.nan)
# print(df)

# # Section 6: Handling Duplicates

# # Q66. Check which rows are duplicates.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.duplicated())

# # Q67. Count the total duplicate rows in the dataset.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.duplicated().sum())

# # Q68. Remove all duplicate rows keeping the first occurrence.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.drop_duplicates())

# # Q69. Remove duplicate rows keeping the last occurrence.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.drop_duplicates(keep="last"))

# # Q70. Find duplicates based only on the Transaction_ID column.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.duplicated(subset="Transaction_ID"))

# # Q71. Keep only one row per Account_Number.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.drop_duplicates(subset="Account_Number"))


# #Section 7: Data Cleaning

# # Q72. Rename the column Transaction_Amount to Amount.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.rename(columns={"Transaction_Amount": "Amount"})
# print(df)

# # Q73. Rename Customer_Name to Name and City to Branch_City together.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df = df.rename(columns={"Customer_Name":"Name","City" : "Branch_City"})
# print(df.columns)

# # Q74. Delete the Fraud_Flag column.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.drop(columns = ["Fraud_Flag"]))

# # Q75. Delete rows at index 10, 11, and 12.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df.drop(index = [10,11,12]))

# # Q76. Remove extra spaces from City values.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["City"].str.strip())

# # Q77. Convert all Customer_Name values to lowercase.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.lower())

# # Q78. Convert all Customer_Name values to UPPERCASE.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.upper())

# # Q79. Convert City values to proper case.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["City"].str.title())

# # Q80. Standardize Gender by converting M/male to Male and F/female to Female.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Gender"].map({
#     "M" : "Male",
#     "male" : "Male",
#     "F" : "Female",
#     "female" : "Female"
# })
# print(result)

# # Q81. Standardize Transaction_Type so credit/CREDIT become Credit and debit becomes Debit.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Transaction_Type"].str.title()
# print(result)

# # Section 8: Data Type Conversion
# # Q82. Check the current data type of Transaction_Amount.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Transaction_Amount"].dtype)

# # Q83. Remove commas from Transaction_Amount values stored as text.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Transaction_Amount"].astype("string").str.replace(",","",regex=False)
# print(result)

# # Q84. Convert the cleaned Transaction_Amount to float type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(result.astype(float))

# # Q85. Convert Age to integer type after cleaning missing values.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Age"].fillna(df["Age"].mean())
# print(result)
# print(result.astype(int))

# # Q86. Convert Transaction_Date from text to datetime type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# print(result)

# # Q87. Convert Account_Type to category data type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Account_Type"].astype("category"))

# # Q88. Convert Annual_Income to numeric and force invalid values to NaN.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = pd.to_numeric(df["Annual_Income"],errors="coerce")
# print(result)

# # Section 9: Adding & Modifying Columns

# # Q89. Create a column Monthly_Income = Annual_Income divided by 12.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Annual_Income"] = pd.to_numeric(df["Annual_Income"],errors="coerce")
# df["Monthly_Income"] = df["Annual_Income"] / 12
# print(df[["Monthly_Income","Annual_Income"]])

# # Q90. Create a column Tax_Amount as 10% of Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Tax_Amount"] = df["Transaction_Amount"] * 1.10
# print(df[["Transaction_Amount","Tax_Amount"]])

# # Q91. Insert a column Bank_Name with value 'SBI' at position 4.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df.insert(4,"Bank_Name","SBI")
# print(df)

# # Q92. Create a column Amount_In_Thousands = Transaction_Amount divided by 1000.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Amount_In_Thousands"] = df["Transaction_Amount"] / 1000
# print(df[["Amount_In_Thousands"]])

# # Q93. Create a column Txn_Size: 'High' if amount >= 100000 else 'Low'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Txn_Size"] = df["Transaction_Amount"].apply(
#     lambda x : "High" if x >= 100000
#     else "Low"
# )
# print(df[["Transaction_Amount","Txn_Size"]])

# # Q94. Create a column Score_Category: 'Good' if Credit_Score >= 700 else 'Poor'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# df["Score_Category"] = df["Credit_Score"].apply(
#     lambda x : "Good" if x >= 700 else "Poor"
# )
# print(df[["Credit_Score","Score_Category"]])

# # Q95. Apply a lambda to increase every Balance_After_Transaction by 2%.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Salary"] = df["Balance_After_Transaction"].apply(
#     lambda x : x * 1.02
# )
# print(df["Salary"])

# # Q96. Create a column Age_Group: Young (18-30), Adult (31-50), Senior (51+).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Age_Group"] = pd.cut(
#     df["Age"],
#     bins = [0,18,35,60],
#     labels=["Young","Adult","Senior"]

# )
# print(df[["Age","Age_Group"]])

# # Q97. Update all KYC_Status values of 'verified' to 'Verified'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Status_level"] = (df["KYC_Status"].replace("verified","Verified"))
# print(df[["KYC_Status","Status_level"]])

# # Q98. Create a column Loan_Status: 'Has Loan' where Loan_Amount is present else 'No Loan'.
# import numpy as np
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Loan_Status"] = np.where(df["Loan_Amount"].notna(),
#                     "Has Loan",
#                     "No Loan")
# print(df[["Loan_Amount","Loan_Status"]])

# # Q99. Increase Annual_Income of all customers by 8%.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Annual_Income"] = pd.to_numeric(df["Annual_Income"],errors="coerce")
# df["Income"] = df["Annual_Income"] * 1.08
# print(df[["Income","Annual_Income"]])

# # Q100. Delete the newly created Bank_Name column.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Bank_Name"].drop())

# Section 10: String Functions
# Q101. Find the length of each Customer_Name.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.len())

# # Q102. Split Customer_Name into First_Name and Last_Name.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.split(" "))

# # Q103. Filter all customers whose name contains 'Shah'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.contains("Shah"))

# # Q104. Filter all customers whose name starts with 'A'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.startswith("A"))

# # Q105. Filter all customers whose name ends with 'Patel'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.endswith("Patel"))

# # Q106. Extract the numeric part from Transaction_ID (e.g. 00025297 from TXN00025297).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Transaction_ID"].str.replace("TXN","",regex=False))

# # Q107. Extract the numeric part from Branch_Code (e.g. 430 from BR430).
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df)
# print(df["Branch_Code"].str.replace("BR","",regex=False))

# # Q108. Filter all Email values that do NOT contain '@'.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(~df["Email"].str.contains("@"))

# # Q109. Extract the domain name from Email addresses.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Email"].str.split("@").str[1])

# # Q110. Remove '+91-' from Mobile_Number values.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Mobile_Number"].str.replace("+91","",regex=False))

# # Q111. Capitalize only the first letter of each City.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["City"] = df["City"].str.capitalize()
# print(df["City"])

# # Q112. Count how many customers have 'Joshi' in their name.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["Customer_Name"].str.contains("Joshi").sum())

# # Section 11: Date & Time Functions

# # Q113. Convert Transaction_Date with mixed formats into proper datetime.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# print(df["Transaction_Date"])
# print(df["Transaction_Date"].dtype)


# # Q114. Extract the year from Transaction_Date.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Year"] = df["Transaction_Date"].dt.year
# print(df)

# # Q115. Extract the month number from Transaction_Date.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Month"] = df["Transaction_Date"].dt.month
# print(df)

# # Q116. Extract the day from Transaction_Date.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Day"] = df["Transaction_Date"].dt.date
# print(df)

# # Q117. Extract the day name from Transaction_Date.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Day_name"] = df["Transaction_Date"].dt.day_name()
# print(df)

# # Q118. Extract the hour from Transaction_Time after converting to datetime.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Hour"] = df["Transaction_Date"].dt.hour
# print(df)

# # Q119. Filter all transactions of the year 2023.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# result = df[df["Transaction_Date"].dt.year == 2023] 
# print(result)

# # Q120. Filter all transactions done in the month of March.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# result  = df[df["Transaction_Date"].dt.month == 3] 
# print(result)

# # Q121. Filter all transactions done on Sunday.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# result  = df[df["Transaction_Date"].dt.day == "sunday"] 
# print(result)

# # Q122. Calculate account age in days as Transaction_Date minus Account_Open_Date.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# df["Account_Open_Date"] = pd.to_datetime(df["Account_Open_Date"],format="mixed",errors="coerce")

# result  = (df["Transaction_Date"] - df["Account_Open_Date"]).dt.days
# print(result)

# # Q123. Display Transaction_Date in the format 05-Mar-2024.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# result  = df["Transaction_Date"].dt.strftime("%d-%m-%Y")
# print(result)

# # Q124. Find the earliest and latest transaction dates.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],format="mixed",errors="coerce")
# result  = df["Transaction_Date"].max()
# result  = df["Transaction_Date"].min()
# print(result)

# # Section 12: GroupBy & Aggregation

# # Q125. Find total Transaction_Amount for each Account_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Account_Type")["Transaction_Amount"].sum()
# print(result)

# # Q126. Find the average Credit_Score for each City.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# result = df.groupby("City")["Credit_Score"].mean()
# print(result)

# # Q127. Count the number of transactions in each Transaction_Mode.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# # df["Transaction_Amount"] = pd.to_datetime(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Transaction_Mode")["Transaction_ID"].count()
# print(result)

# # Q128. Find the maximum Transaction_Amount for each Merchant_Category.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_datetime(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Merchant_Category")["Transaction_Amount"].max()
# print(result)

# # Q129. Find the minimum Balance_After_Transaction for each Branch_Code.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_datetime(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Branch_Code")["Balance_After_Transaction"].min()
# print(result)

# # Q130. Find total Loan_Amount given for each Loan_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_datetime(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Loan_Type")["Loan_Amount"].sum()
# print(result)

# # Q131. Find the average Age of customers in each Employment_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_datetime(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Employment_Type")["Age"].mean()
# print(result)

# # Q132. Find sum, mean, and max of Transaction_Amount for each City in one output.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("City")["Transaction_Amount"].agg(
#     ["sum","mean","max"]
# )
# print(result)

# # Q133. Apply different functions: sum of Transaction_Amount and mean of Credit_Score per City.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# result = df.groupby("City").agg({
#     "Transaction_Amount" : "sum",
#     "Credit_Score" : "mean"
# })
# print(result)

# # Q134. Group by City and Account_Type together and find total transaction amount.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Account_Type"] = pd.to_numeric(df["Account_Type"],errors="coerce")
# result = df.groupby(["City","Account_Type"])["Transaction_Amount"].sum()
# print(result)

# # Q135. Find the top 5 cities by total transaction amount.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("City")["Transaction_Amount"].sum()
# print(result.head(5))

# # Q136. Group by Merchant_Category, find total amount, and sort descending.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Merchant_Category")["Transaction_Amount"].sum().sort_values(ascending=False)
# print(result)

# # Q137. Add a column showing the average transaction amount of each City next to every row.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("City")["Transaction_Amount"].transform("mean")
# print(result)

# # Q138. Count unique customers (Account_Number) in each Branch_Code.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Branch_Code")["Account_Number"].nunique()
# print(result)

# # Section 13: Pivot Table & Crosstab

# # Q139. Create a pivot table showing average Transaction_Amount by Account_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#        values="Transaction_Amount",
#        index = "Account_Type",
#        aggfunc="mean"   
# )
# print(result)

# # Q140. Create a pivot table with City as rows, Transaction_Type as columns, and total amount as values.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#     values = "Transaction_Amount",
#     index = "City",
#     columns="Transaction_Type",
#     aggfunc="sum"
# )
# print(result)

# # Q141. Create a pivot table showing average Credit_Score by Employment_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# result = df.pivot_table(
#     values = "Credit_Score",
#     index="Employment_Type",
#     aggfunc="mean"
# )
# print(result)

# # Q142. Create a pivot table with sum and mean of Transaction_Amount by City.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#     values = "Transaction_Amount",
#     index = "City",
#     aggfunc=["sum","mean"]
# )
# print(result)

# # Q143. Add row and column totals to a pivot table of amount by City and Account_Type.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#     values = "Transaction_Amount",
#     index = "City",
#     columns = "Account_Type",
#     aggfunc="sum",
#     margins=True
# )
# print(result)

# # Q144. Create a pivot table with City and Branch_Code as multiple row indexes.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#     values = "Transaction_Amount",
#     index= ["City","Branch_Code"],
#     aggfunc="sum"
# )
# print(result)

# # Q145. Create a pivot table with Transaction_Amount and Loan_Amount as multiple values.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#     values = ["Transaction_Amount","Loan_Amount"],
#     index = "City",
#     aggfunc = "sum"
    
# )
# print(result)

# # Q146. Count transactions for each combination of City and Transaction_Mode.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = pd.crosstab(
#     df["City"],
#     df["Transaction_Mode"]
# )
# print(result)

# # Q147. Create a crosstab of Account_Type vs KYC_Status.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = pd.crosstab(
#     df["Account_Type"],
#     df["KYC_Status"]
# )
# print(result)

# # Q148. Fill missing combinations in a pivot table with 0.
# pd.set_option("display.max_columns", None)
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.pivot_table(
#      values="Transaction_Amount",
#     index="City",
#     columns="Transaction_Mode",
#     aggfunc="sum",
#     fill_value=0
# )
# print(result)

# # Section 14: Merge & Join

# # Q149. Merge the transactions DataFrame with a customer details DataFrame using Account_Number.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[["Account_Number", "Customer_Name", "Account_Type"]]

# df2 = df[["Account_Number", "Transaction_Type", "Transaction_Amount"]]

# result = pd.merge(
#     df1,
#     df2,
#     on="Account_Number"
# ) 
# print(result)

# # Q150. Merge two DataFrames keeping only matching Account_Number rows.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[["Account_Number", "Customer_Name", "Account_Type"]]

# df2 = df[["Account_Number", "Transaction_Type", "Transaction_Amount"]]

# result = pd.merge(
#     df1,
#     df2,
#     on="Account_Number",
#     how = "inner"
# ) 
# print(result)

# # Q151. Account_Type == "Savings" વાળો DataFrame બનાવો અને તેને original DataFrame સાથે Customer_Name પર left merge કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[df["Account_Type"] == "Savings"][["Customer_Name","Account_Type"]]
# result = pd.merge(
#     df,df1,
#     on = "Customer_Name",
#     how = "left"
# )
# print(result)

# # Q152. Account_Type == "Current" વાળો DataFrame બનાવો અને તેને original DataFrame સાથે Customer_Name પર right merge કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[df["Account_Type"] == "Current"][["Customer_Name","Account_Type"]]
# result = pd.merge(
#     df,df1,
#     on = "Customer_Name",
#     how = "right"
# )
# print(result)

# # Q153. Gender == "Male" અને Gender == "Female" ના બે DataFrames બનાવો અને તેમને Customer_Name પર outer merge કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[df["Gender"] == "Male"][["Customer_Name","Gender"]]
# df2 = df[df["Gender"] == "Female"][["Customer_Name","Gender"]]

# result = pd.merge(
#     df1,df2,
#     on = "Customer_Name",
#     how="outer"
# )
# print(result)

# # # Q154. Dataset ને બે parts માં divide કરો — first 50 rows અને remaining rows. બંને DataFrames ને one below another combine કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")

# df1 = df.iloc[:50]
# df2 = df.iloc[50:]

# result = pd.concat(
#     [df1, df2],
#     ignore_index=True
# )

# print(result)

# # Q155. Dataset ના બે DataFrames બનાવો: એકમાં Customer_Name, Age અને બીજામાં Credit_Score, Annual_Income. બંનેને side by side combine કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[["Customer_Name","Age"]]
# df2 = df[["Credit_Score","Annual_Income"]]
# result = pd.concat(
#     [df1,df2],
#     axis=1
# )
# print(result)

# # Q156. Original DataFrame માં Customer_Name ને Name તરીકે rename કરો અને તેની copy માં Customer_Name રાખો. પછી બંને DataFrames ને Name vs Customer_Name પર merge કરો.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df[["Customer_Name","Credit_Score"]].copy()
# df1 = df1.rename(columns = {"Customer_Name" : "Name"})
# df2 = df[["Customer_Name","Annual_Income"]].copy()
# result = pd.merge(
#     df1,df2,
#     left_on = "Name",
#     right_on="Customer_Name",
#     how="inner"
# )
# print(result)

# # Section 15: Advanced Operations

# # Q157. Convert the wide dataset into long format with City as identifier and amount columns as values.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# # Convert Transaction_Amount to numeric
# df["Transaction_Amount"] = pd.to_numeric(
#     df["Transaction_Amount"],
#     errors="coerce"
# )
# wide = df.pivot_table(
#     index = "City",
#     columns="Transaction_Mode",
#     values = "Transaction_Amount",
#     aggfunc="sum"
# ).reset_index()

# long = pd.melt(
#      wide,
#     id_vars="City",
#     var_name="Transaction_Mode",
#     value_name="Amount"
# )
# print(long)

# # Q158. Convert a column containing lists of services into separate rows.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df1 = df.explode("Transaction_Mode")
# print(df1)

# # Q159. Convert columns of a summary table into row index.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# summary = df.groupby("City")[["Transaction_Amount"]].mean()
# result = summary.stack()
# print(result)

# # Q160. Convert row index back into columns.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# un_column = result.unstack()
# print(un_column)

# # Q161. Interchange rows and columns of a summary table.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# summary = df.groupby("City")[["Transaction_Amount"]].mean()
# result = summary.T
# print(result)

# # Q162. Limit all Credit_Score values to a maximum of 900.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# result = df["Credit_Score"].clip(0,900)
# print(result)

# # Q163. Limit Age values to a minimum of 18.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Age"].clip(18,100)
# print(result)

# # Q164. Create a MultiIndex using City and Branch_Code as index.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df.set_index(["City","Branch_Code"])
# print(result)

# # Q165. Swap the levels of the MultiIndex (Branch_Code first, City second).
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df.set_index(["City", "Branch_Code"])
# result = result.swaplevel("Branch_Code","City")
# print(result)

# # Q166. Reset the MultiIndex back to normal columns.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# reset = result.reset_index()
# print(reset)

# # Section 16: Window Functions
# # Q167. Calculate the running total (cumulative sum) of Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].cumsum()
# print(result)

# # Q168. Calculate the cumulative product of a small numeric column for 10 rows.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df["Age"].cumprod()
# print(result.head(10))

# # Q169. Calculate the cumulative maximum of Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].cummax()
# print(result)

# # Q170. Calculate the cumulative minimum of Balance_After_Transaction.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Balance_After_Transaction"] = pd.to_numeric(df["Balance_After_Transaction"],errors="coerce")
# result = df["Balance_After_Transaction"].cummin()
# print(result)

# # Q171. Calculate the 7-day rolling average of daily transaction amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].rolling(7).mean()
# print(result)

# # Q172. Calculate the 30-day rolling maximum of daily transactions.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].rolling(30).max()
# print(result)

# # Q173. Calculate the 30-day rolling minimum of daily transactions.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].rolling(30).max()
# print(result)
# result1 = df["Transaction_Amount"].rolling(30).max()
# print(result1)

# # Q174. Calculate the rolling sum of Transaction_Amount with window size 10.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].rolling(10).sum()
# print(result)
# result1 = df["Transaction_Amount"].rolling(30).max()
# print(result1)

# # Q175. Calculate the expanding average of Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].expanding().mean()
# print(result)

# # Q176. Calculate the expanding sum of Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].expanding().sum()
# print(result)

# # Section 17: Ranking & Statistical Analysis
# # Q177. Rank all transactions by Transaction_Amount (highest = rank 1).
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Rank"] = df["Transaction_Amount"].rank(ascending=False)
# print(df[["Rank","Transaction_Amount"]])

# # Q178. Rank customers by Credit_Score within each City.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# result = df.groupby("City")["Credit_Score"].rank(ascending=False)
# print(result)

# # Q179. Calculate the percentage change in daily total transaction amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].pct_change()*100
# print(result)

# # Q180. Calculate the day-over-day difference in total transactions.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].diff()
# print(result)

# # Q181. Shift the Transaction_Amount column one row down.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].shift(-1)
# print(result)

# # Q182. Create a column showing the previous transaction amount next to the current one.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Transaction_Amount"].shift(1)
# print(result)

# # Q183. Find the correlation between Credit_Score and Annual_Income.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# df["Annual_Income"] = pd.to_numeric(df["Annual_Income"],errors="coerce")
# result = df["Credit_Score"].corr(df["Annual_Income"])
# print(result)

# # Q184. Find the covariance between Age and Transaction_Amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df["Age"].cov(df["Transaction_Amount"])
# print(result)

# # Q185. Find the correlation matrix of all numeric columns.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df.corr(numeric_only=True)
# print(result)

# # Q186. Find the standard deviation of Transaction_Amount for each Account_Type.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# result = df.groupby("Account_Type")["Transaction_Amount"].std()
# print(result)

# # Section 18: Resampling & Categorical Data

# # Q187. Convert Transaction_Date to datetime and set it as the index.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# df = df.set_index(df["Transaction_Date"])
# print(df)

# # Q188. Calculate total transaction amount for each month.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# df = df.set_index(df["Transaction_Date"])
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# print(df.resample("ME")["Transaction_Amount"].sum())

# # Q189. Calculate the average transaction amount for each week.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# df = df.set_index(df["Transaction_Date"])
# print(df.resample("W")["Transaction_Amount"].mean())

# # Q190. Calculate quarterly total transaction amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# df = df.set_index(df["Transaction_Date"])
# print(df.resample("QE")["Transaction_Amount"].sum())

# # Q191. Calculate yearly total transaction amount.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Transaction_Amount"] = pd.to_numeric(df["Transaction_Amount"],errors="coerce")
# df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],errors="coerce")
# df = df.set_index(df["Transaction_Date"])
# print(df.resample("YE")["Transaction_Amount"].sum())

# # Q192. Convert KYC_Status to category type and display its categories.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# print(df["KYC_Status"].dtype)
# df["KYC_Status"] = df["KYC_Status"].astype("category")
# print(df["KYC_Status"].cat.categories)

# # Q193. Divide Credit_Score into 3 bins labeled Poor, Average, Excellent.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Credit_Score"] = pd.to_numeric(df["Credit_Score"],errors="coerce")
# df["Credit_Group"] = pd.cut(
#     df["Credit_Score"],
#     bins = 3,
#     labels = ["Poor","Average","Excellent"]
# )
# print(df[["Credit_Score","Credit_Group"]])

# # Q194. Divide Annual_Income into 4 bins with an equal number of customers.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# df["Annual_Income"] = pd.to_numeric(df["Annual_Income"],errors="coerce")
# df["Credit_Group"] = pd.qcut(
#     df["Credit_Score"],
#     q = 4,
#     labels=["Low","Medium","High","Very high"]
    
# )
# print(df[["Credit_Score","Credit_Group"]])

# # Section 19: Data Validation & Exporting

# # Q195. Check that no Age value is negative or above 100 after cleaning.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[(df["Age"] < 0) | (df["Age"] > 100).any()]
# print(result)

# # Q196. Verify that all Credit_Score values are between 300 and 900.
# df = pd.read_excel("E:\\Pandas\\Bank_Transactions_Data.xlsx")
# result = df[(df["Credit_Score"] > 0) | (df["Credit_Score"] < 900).all()]
# print(result)

# # Q197. Export the cleaned dataset to a CSV file without the index.
# df.to_csv("cleaned_bank_transactions.csv", index=False)

# # Q198. Export the dataset to an Excel file.
# df.to_excel("cleaned_bank_transactions.csv")

# # Q199. Export only Transaction_ID, Customer_Name, and Transaction_Amount to CSV.
# result = df[[
#     "Transaction_ID",
#     "Customer_Name",
#     "Transaction_Amount"
# ]]

# result.to_csv(
#     "E:\\Pandas\\selected_transactions.csv",
#     index=False
# )

# # Q200. Export only Credit transactions to a separate Excel file.
# credit_df = df[df["Transaction_Type"] == "Credit"]

# credit_df.to_excel(
#     "E:\\Pandas\\credit_transactions.xlsx",
#     index=False)

import math
x = 100
result = math.log10(x)
print(result)