# # basic
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 24, 21, 25, 23],
#     "Salary": [30000, 45000, 28000, 50000, 35000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR"]
# })

# # head  : shows the first 5 row
# print(df.head(3))

# # tail : show last 5 row
# print(df.tail(2))

# # shape
# print(df.shape)

# print("Rows:", df.shape[0])
# print("Columns:", df.shape[1])

# # columns
# # Shows the names of all columns.
# print(df.columns)

# # if only want the names as list.
# print(df.columns.tolist())

# # index
# # Shows the DataFrame's row index.
# print(df.index)

# df = pd.DataFrame(
#     {
#         "Name": ["Rahul", "Priya"],
#         "Age": [22, 24]
#     },
#     index=["student_1", "student_2"]
# )
# print(df)

# # data type
# print(df.dtypes)

# # info
# print(df.info())

# # describe
# print(df.describe())

# # size
# print(df.size)

# # practise
# df = pd.DataFrame({
#     "Student": ["A", "B", "C", "D", "E", "F"],
#     "Age": [20, 21, 19, 22, 20, 21],
#     "Marks": [85, 72, 91, 65, 78, 88],
#     "City": ["Surat", "Rajkot", "Surat", "Ahmedabad", "Rajkot", "Surat"]
# })

# # Q1
# # Show the first 3 rows.
# print(df.head(3))

# # Q2
# # Show the last 2 rows.
# print(df.tail(2))

# # Q3
# # Find the number of rows and columns.
# print(df.shape)

# # Q4
# # Print all column names.
# print(df.columns.tolist())

# # Q5
# # Print the row index.
# print(df.index)

# # Q6
# # Print the data types.
# print(df.dtypes)

# # Q7
# # Display the complete DataFrame information.
# print(df.info())

# # Q8
# # Display statistical information.
# print(df.describe())

# # Q9
# # Find the total number of cells.
# print(len(df))

# # q10 print the size 
# print(df.size)

# import pandas as pd
# ages = pd.Series([22,24,21])
# print(ages)

# # series with labels
# ages = pd.Series(
#     [22,24,21],
#     index = ["jensi","jeni","mahi"]
# )
# print(ages)

# print(ages["jeni"])

# # data frame : A DataFrame is a two-dimensional labeled data structure.
# data = {
#     "Name" : ["rahul","priya","amit"],
#     "age" : [22,24,21],
#     "Salary" : [30000,45000,23000]
# }
# df = pd.DataFrame(data)
# print(df)

# print(type(df["age"]))  # series beacuse age ae 1d array thay aetle te series ma ave
# print(type(df))   # data frame  beacuse te aakho data frame present kare che

# print(df["age"])   # -> series
# print(df[["age"]])          # -> data frame
# print(df[["Name","age"]])   # -> data frame

# # data science
# customers = pd.DataFrame({
#     "Customer": ["A", "B", "C", "D"],
#     "Age": [21, 30, 25, 40],
#     "Income": [25000, 50000, 35000, 80000],
#     "Purchased": [True, False, True, True]
# })

# print(customers["Income"])
# print(customers)
# print(customers[["Age","Income"]])

# students = pd.DataFrame({
#     "Name": ["Jensi", "Rahul", "Priya", "Amit"],
#     "Age": [20, 21, 22, 20],
#     "Marks": [85, 72, 91, 68]
# })

# # Q1
# # Print the complete DataFrame.
# print(students)

# # Q2
# # Print only the Marks column.
# print(students["Marks"])

# # Q3
# # Print Name and Marks.
# print(students[["Name","Marks"]])

# # Q4
# # Check the type of students["Marks"].
# print(type(students["Marks"]))

# # Q5
# # Check the type of students[["Marks"]].
# print(type(students[["Marks"]]))

# q5
# What is the difference between Series and DataFrame?
# series is define one row it is a 1d array.
# data frame means define all the data it is labled data.

# # data creation
# import pandas as pd
# marks = pd.Series([80,75,90,65,88])
# print(marks)

# # Creating a DataFrame from a Dictionary
# data = {
#     "Name" : ["rahul","priya","amit"],
#     "Age" : [23,21,20],
#     "Salary" : [30000,45000,21000]
# }
# df = pd.DataFrame(data)
# print(df)

# # Creating DataFrame from a List of Dictionaries
# data = [
#     {"Name": "Rahul", "Age": 22, "Salary": 30000},
#     {"Name": "Priya", "Age": 24, "Salary": 45000},
#     {"Name": "Amit", "Age": 21, "Salary": 28000}
# ]

# df = pd.DataFrame(data)

# print(df)

# # creating a dataframe from list of lists
# data = [
#     ["rahul",22,30000],
#     ["priya",24,45000],
#     ["amit",25,65000]
# ]

# df = pd.DataFrame(data,
#         columns = ["Name","Age","Salary"])

# print(df)

# # data from numpy
# import numpy as np
# import pandas as pd

# data = np.array([
#     [101,50000],
#     [102,34000],
#     [103,45000]
# ])
# df = pd.DataFrame(data,columns=["ID","Salary"])
# print(df)

# # empty dataframe
# df = pd.DataFrame()
# print(df)

# # Creating DataFrame from a Dictionary of Series
# names = pd.Series(["jensi","jeni","mahi"])
# ages = pd.Series([22,24,21])

# df = pd.DataFrame({
#     "Name" : names,
#     "Age" : ages
# })

# print(df)

# # practice
# data = {
#     "Products" : ["laptop","mouse","chair","notebook"],
#     "Price" : [60000,800,3500,100],
#     "Quantity" : [2,5,4,10],
#     "Category" : ["Electronics","Electronics","Furniture","stationary"]
# }
# df = pd.DataFrame(data)
# print(df)

# # list of list
# data = [
#     ["laptop",60000,2,"Electronics"],
#     ["Mouse",800,5,"Electronics"],
#     ["Chair",3500,4,"Furniture"],
#     ["notebook",100,10,"Stationary"]

# ]
# df = pd.DataFrame(data,
#         columns = ["Products","price","quantity","category"])
# print(df)

# # q3
# Prices = pd.Series(
#     [60000, 800, 3500, 100],
#     index=["Laptop", "Mouse", "Chair", "Notebook"]
# )

# print(Prices)

# # task 4
# data = np.array([
#     [101,60000],
#     [102,800],
#     [103,3500],
#     [104,100]
# ])

# df = pd.DataFrame(data,columns=["Product_ID","Prices"])
# print(df)

# # reading a csv file
# import pandas as pd

# df = pd.read_csv("students.csv")
# print(df)

# # reading csv with selected columns
# df = pd.read_csv("Students.csv",
#         usecols = ["Name","Salary"])
# print(df)

# # with specific seprator
# df = pd.read_csv(
#     "students.csv",
#     sep=";"
# )
# print(df)

# # readong csv with missing value
# df = pd.read_csv(
#     "students.csv",
#     na_values=["NA", "N/A", "unknown"]
# )
# print(df)

# # reading excel
# df = pd.read_excel("students.xlsx")
# print(df)

# # selecting the data
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 24, 21, 25, 23],
#     "Salary": [30000, 45000, 28000, 50000, 35000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR"]
# })

# print(df)

# # selecting one column : []
# print(df["Name"])

# # selecting multiple column [[]]
# print(df[["Name","Salary"]])

# # .loc[] selecting by label
# print(df.loc[2,"Name"])
# print(df.loc[3,"Salary"])

# # Select Multiple Rows with .loc[]
# print(df.loc[[0,2,4]])

# # Select Rows + Columns Together
# print(df.loc[[0,2,4],["Name","Salary"]])

# # Select All Rows + Specific Columns
# print(df.loc[:,["Name","Salary"]])

# # 8. Selecting a Range with .loc[]
# print(df.loc[1:3])

# # iloc : selecting by position
# print(df.iloc[2])
# print(df.iloc[3])

# # .iloc row + column
# # syntax : df.iloc[row_position, column_position]
# print(df.iloc[0,2])
# print(df.iloc[2,0])
# print(df.iloc[3,1])

# # Multiple Rows with .iloc
# print(df.iloc[[0,2,4]])

# # 12. Multiple Rows + Columns with .iloc
# print(df.iloc[[0,2,4],[0,2]])

# # range
# print(df.iloc[1:3])

# # Select only Age.
# print(df["Age"])

# # Select Name and Department.
# print(df[["Name","Department"]])

# # Select Rahul's complete row.
# print(df.iloc[0])

# # Select Amit's salary.
# print(df.iloc[2,2])

# # Select rows 0, 2 and 4.
# print(df.loc[[0,2,4]])

# # Select Name and Salary for rows 1 and 3.
# print(df.loc[[1,3],["Name","Salary"]])

# # Using .iloc, select the first 3 rows.
# print(df.iloc[0:3])

# # Using .iloc, select the Name column from the first 3 rows.
# print(df.iloc[0:3,0])

# # Select Rahul, Amit, Raj + only Name and Salary.
# print(df.iloc[[0,2,4],[0,2]])

# # sorting the data
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 24, 21, 25, 23],
#     "Salary": [30000, 45000, 28000, 50000, 35000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR"]
# })

# print(df)

# # sort by column
# print(df.sort_values("Salary"))

# # desecding oder
# print(df.sort_values("Salary",ascending=False))

# # by age
# print(df.sort_values("Age",ascending=True))

# # by name
# print(df.sort_values("Name",ascending=True))

# # by multiple columns
# print(df.sort_values(["Department", "Salary"]))

# # diff order for diff columns
# print(df.sort_values(["Department","Salary"],
#             ascending=[True,False]))

# # sorting and index
# df = df.sort_values("Salary").reset_index(drop=True)
# print(df) 

# # sorting + selecting
# print(df.sort_values("Salary", ascending=False).head(3))

# # top 2 oldest employee
# print(df.sort_values("Age",ascending=False).head(2))

# # sort_index
# print(df.sort_index())

# # 1. Sort by Age from youngest to oldest.
# print(df.sort_values("Age",ascending=False))

# # 2. Sort by Salary from highest to lowest.
# print(df.sort_values("Salary",ascending=False))

# # 3. Sort Name alphabetically.
# print(df.sort_values("Name",ascending=True))

# # 4. Sort Department in reverse alphabetical order.
# print(df.sort_values("Name",ascending=False))

# # 5. Sort by Department first and Salary second.
# print(df.sort_values(["Department","Salary"]))

# # 6. Sort by Department A-Z and Salary highest-lowest.
# print(df.sort_values(["Department","Salary"],
#             ascending=[True,False]))

# # 7. Find the top 3 employees with the highest salary.
# print(df.sort_values("Salary",ascending=False).head(3))

# filtering data
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 24, 21, 25, 23],
#     "Salary": [30000, 45000, 28000, 50000, 35000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR"]
# })

# print(df)

# # basic filtering
# print(df[df["Salary"]>40000])

# # greater than
# print(df[df["Age"]>22])

# # salary less than
# print(df[df["Salary"]<35000])

# # greater than or equal to
# print(df[df["Age"]>= 23])

# # equal
# print(df[df["Department"] == "IT"])

# # not equal
# print(df[df["Department"] != "IT"])

# # multiple condition with and
# print(df[(df["Salary"] > 30000) & (df["Age"] > 22)])

# # multiple condition with or
# print(df[(df["Salary"] > 45000) | (df["Age"] < 22)])

# # Filtering Specific Categories with .isin()
# print(df[df["Department"].isin(["IT","HR"])])

# # not in mate (~) use karvu
# print(df[~df["Department"].isin(["IT", "HR"])]) 

# # filtering range with between
# print(df[df["Salary"].between(30000, 45000)]) 

# # Filtering Text with .str.contains() ⭐
# print(df[df["Name"].str.contains("a",case=False)]) # here case=false means dont care about uppercase and lowercase

# # filtering + selecting columns
# print(df.loc[df["Salary"] > 40000,["Name","Salary"]]) 

# # filtering + sorting
# print(df[df["Salary"] > 30000].sort_values("Salary",ascending=False))

# 1. Select employees whose Age is greater than 23.
# print(df[df["Age"] > 23])

# # 2. Select employees whose Salary is less than 40000.
# print(df[df["Salary"] < 40000])

# # 3. Select employees from IT department.
# print(df[df["Department"] == "IT"])

# # 4. Select employees who are NOT from HR.
# print(df[df["Department"] != "HR"])

# # 5. Select employees whose Salary is greater than 30000
# #    AND Age is greater than 22.
# print(df[(df["Salary"] > 30000) & (df["Age"] > 22)])

# # 6. Select employees from IT OR HR.
# print(df[df["Department"].isin(["IT","HR"])])

# 7. Select employees whose Salary is between 30000 and 45000.
# print(df[df["Salary"].between(30000,45000)])

# 8. Find employees whose Salary is greater than 30000.
#    Show only Name, Department and Salary.
#    Sort them from highest Salary to lowest.

# print(df.loc[df["Salary"]>30000,["Name","Department","Salary"]].sort_values("Salary",ascending=False))

# # data cleaning
# import pandas as pd

# df = pd.DataFrame({
#     "Name": [" Rahul ", "Priya", "Amit", "Priya", "Neha"],
#     "Age": [22, 24, None, 24, 25],
#     "Salary": [30000, 45000, 28000, 45000, None],
#     "City": ["Surat", "Rajkot", "Surat", "Rajkot", " surat "]
# })

# print(df)

# # check missing value
# print(df.isna().sum())

# # check if there any missing value
# print(df.isna().any())

# # total missing value
# print(df.isna().sum().sum())

# # remove missing value
# # remove rows
# print(df.dropna())

# # fill missing value
# # with mean
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# print(df["Age"])

# # salary with mean
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df["Salary"])

# # remove duplicate
# print(df.duplicated())

# # count duplicate
# print(df.duplicated().sum())

# # remove duplicate
# df = df.drop_duplicates()
# print(df)

# # clean text data
# df["City"] = df["City"].str.strip()
# print(df["City"])

# # lowercase
# df["City"] = df["City"].str.lower()
# print(df["City"])

# # upper
# df["City"] = df["City"].str.upper()
# print(df["City"])

# # title
# df["City"] = df["City"].str.title()
# print(df["City"])

# # practical cleaning
# df["City"] = df["City"].str.strip().str.title()
# print(df["City"])

# # fix data type
# print(df.dtypes)

# # convert data type
# df["Age"] = pd.to_numeric(df["Age"])
# print(df["Age"])

# df["Age"] = df["Age"].astype(int)
# print(df["Age"])

# df["Salary"] = df["Salary"].astype(float)
# print(df["Salary"])

# # clean columns name
# df = df.rename(columns={
#     "Employee Name": "Name",
#     "Employee Age": "Age",
#     "Employee Salary": "Salary"
# })
# print(df)

# import pandas as pd

# df = pd.DataFrame({
#     "Name": [" Rahul ", "Priya", "Amit", "Priya", "Neha "],
#     "Age": [22, 24, None, 24, 25],
#     "Salary": [30000, 45000, 28000, 45000, None],
#     "City": ["Surat", "Rajkot", "surat", "Rajkot", " surat "]
# })

# # Find the number of missing values in each column.
# print(df.isna().sum())

# # Find the total number of missing values.
# print(df.isna().sum().sum())

# # Fill missing Age with the median.
# df["Age"] = df["Age"].fillna(df["Age"].median())
# print(df["Age"])

# # Fill missing Salary with the mean.
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df["Salary"])

# # Remove duplicate rows.
# print(df.drop_duplicates())

# # Remove extra spaces from Name.
# df["Name"] = df["Name"].str.strip()
# print(df["Name"])

# # Convert City into proper title case.
# df["City"] = df["City"].str.strip().str.title()
# print(df["City"])

# # q8 
# print(df.isna().sum())

# print(df.duplicated().sum())

# # Adding & sorting 
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Age": [22, 24, 21],
#     "Salary": [30000, 45000, 28000]
# })

# print(df)

# # add a new column
# # df["City"] = ["Surat","Rajkot","Ahmedabad"]
# # print(df)

# # 2. Add a Column Using Calculation
# df["Salary"] = df["Salary"] + 50000
# print(df)

# df["Age"] = df["Age"] + 1
# print(df)

# # Modify an Existing Column
# df["Salary"] = df["Salary"] * 1.10
# print(df)

# # modifying specific cell
# df.loc[0,"Salary"] = 35000
# print(df)

# # we can also modify multiple rows
# df.loc[df["Name"] == "Rahul","Salary"] = 40000
# print(df)

# # multiple column
# # df[["Age","Salary"]] = df[["Age","Salary"]].fillna(0)
# # print(df)

# # rename column
# df = df.rename(columns={
#     "Salary" : "Monthly_Salary"
# })
# print(df)

# # Change All Column Names

# # df.columns = ["Employee_Name", "Employee_Age", "Salary"]

# # 8. Add Column at a Specific Position
# df.insert(1, "City", ["Surat", "Rajkot", "Ahmedabad"])
# print(df)

# # delete column
# df = df.drop(columns=["Age"])
# print(df)

# # multiple column remove
# # df = df.drop(columns=["Age","Salary"])

# # delete row
# df = df.drop(index=1)
# print(df)

# # columns delete :: columns =
# # row delete :: index =

# # new row add
# new_row = pd.DataFrame([{
#     "Name": "Neha",
#     "Age": 25,
#     "Salary": 50000,
#     "City" : "Surat"
# }])

# df = pd.concat([df, new_row], ignore_index=True)
# print(df)

# df["Monthly_Salary"] = df["Monthly_Salary"].fillna(df["Monthly_Salary"].median())
# print(df)

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Age": [22, 24, 21],
#     "Salary": [30000, 45000, 28000]
# })

# df["Annual_Salary"] = df["Salary"] * 12

# df["Salary_After_Bonus"] = df["Salary"] * 1.10

# df.loc[df["Age"] >= 23, "Category"] = "Senior"

# df.loc[df["Age"] < 23, "Category"] = "Junior"

# print(df)

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Age": [22, 24, 21, 25],
#     "Salary": [30000, 45000, 28000, 50000]
# })

# # Add a City column: Surat, Rajkot, Surat, Ahmedabad.
# df["City"] = ["Surat","Rajkot","City","Ahmedabad"]
# print(df)

# # Create Annual_Salary from Salary.
# df["Annual_Salary"] = df["Salary"] * 12

# # Increase everyone's salary by 10%.
# df["Increase_salary"] = df["Salary"] * 1.10

# # Change Amit's age to 22.
# df.loc[2,"Age"] = 22

# # Change Neha's salary to 55000.
# df.loc[3,"Salary"] = 55000

# # Rename Salary to Monthly_Salary.
# df = df.rename(columns={"Salary" : "Monthly_salary"}) 
# print(df)

# # Delete the Age column.
# df = df.drop(columns=["Age"])
# print(df)

# # Add a new employee: Raj, 23, 35000, Surat.
# new = pd.DataFrame([{
#     "Name" : "Raj",
#     "Age" : 23,
#     "Salary" : 35000,
#     "City" : "Surat"
# }])
# df = pd.concat([df,new],ignore_index=True)
# print(df)

# # date & time
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "Order_Date": [
#         "2026-01-15",
#         "2026-02-20",
#         "2026-03-10",
#         "2026-04-05"
#     ],
#     "Sales": [5000, 7000, 4500, 8000]
# })

# print(df)
# print(df.dtypes)

# # convert to datetime
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df.dtypes)

# # extract year
# df["Year"] = df["Order_Date"].dt.year
# print(df)

# # month
# df["Month"] = df["Order_Date"].dt.month

# # month_name
# # df["Month"] = df["Order_Date"].dt.month_name()

# # day
# df["Day"] = df["Order_Date"].dt.day

# # day_name
# # df["Day"] = df["Order_Date"].dt.day_name()

# # extract weekday number
# df["Weekday"] = df["Order_Date"].dt.weekday
# print(df)

# # filter using dates
# df[df["Order_Date"] > "2026-02-01"]
# print(df)

# # sort by date
# df = df.sort_values("Order_Date")
# print(df)

# # diff between dates
# df = pd.DataFrame({
#     "Order_Date": pd.to_datetime([
#         "2026-01-10",
#         "2026-02-15",
#         "2026-03-20"
#     ]),
#     "Delivery_Date": pd.to_datetime([
#         "2026-01-15",
#         "2026-02-20",
#         "2026-03-25"
#     ])
# })

# df["Delivery_Days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days
# print(df)

# # today date
# today = pd.Timestamp.today()
# print(today)

# date + time
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# print(df["Order_Date"].dt.date)
# print(df["Order_Date"].dt.hour)
# print(df["Order_Date"].dt.minute)
# print(df["Order_Date"].dt.second)

# # group sales by month
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# df["Month"] = df["Order_Date"].dt.month
# print(df)
# print(df.groupby("Month")["Sales"].sum())

# import pandas as pd

# df = pd.DataFrame({
#     "Order_ID": [101, 102, 103, 104, 105],
#     "Order_Date": [
#         "2026-01-15",
#         "2026-02-20",
#         "2026-02-25",
#         "2026-03-10",
#         "2026-03-18"
#     ],
#     "Sales": [5000, 7000, 4500, 8000, 6000]
# })

# # Convert Order_Date to datetime.
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df.dtypes)

# # Create a Year column.
# df["year"] = df["Order_Date"].dt.year
# print(df)

# # Create a Month column.
# df["month"] = df["Order_Date"].dt.month
# print(df)

# # Create a Month_Name column.
# df["month_name"] = df["Order_Date"].dt.month_name()
# print(df)
# # Create a Day_Name column.
# df["Day_name"] = df["Order_Date"].dt.day_name()
# print(df)

# # Sort orders from newest to oldest.
# print(df.sort_values("Order_Date"))

# # Select orders after "2026-02-01".
# result = df[df["Order_Date"] > "2026-02-01"]
# print(result)

# # Find total sales for each month using groupby().
# result = df.groupby("month")["Sales"].sum()
# print(result)

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Birth_Date": ["2004-05-10", "2003-08-20", "2005-01-15"]
# })

# df["Birth_Date"] = pd.to_datetime(df["Birth_Date"])
# print(df.dtypes)

# df["year"] = df["Birth_Date"].dt.year
# print(df)

# # month and day
# df["month"] = df["Birth_Date"].dt.month

# df["date"] = df["Birth_Date"].dt.day
# print(df)

# df["month_name"] = df["Birth_Date"].dt.month_name()
# print(df)

# df["day_name"] = df["Birth_Date"].dt.day_name()
# print(df)

# df = pd.DataFrame({
#     "Order_Date": pd.to_datetime([
#         "2025-01-10",
#         "2026-02-15",
#         "2026-05-20",
#         "2027-03-10"
#     ]),
#     "Sales": [5000, 7000, 8000, 6000]
# })

# result = df[df["Order_Date"].dt.year == 2026]
# print(result)

# result = df[df["Order_Date"].dt.month == 3]
# print(result)

# result = df[df["Order_Date"].dt.month.isin([1,2])]
# print(result)

# result = df[
#     (df["Order_Date"] >= "2026-02-01") &
#     (df["Order_Date"] <= "2026-12-31")
# ]

# print(result)

# latest = df["Order_Date"].max()
# print(latest)

# earliest = df["Order_Date"].min()
# print(earliest)

# df = pd.DataFrame({
#     "Order_Date": pd.to_datetime([
#         "2026-01-01",
#         "2026-02-10",
#         "2026-03-15"
#     ]),
#     "Delivery_Date": pd.to_datetime([
#         "2026-01-05",
#         "2026-02-15",
#         "2026-03-20"
#     ])
# })

# df["Delivery_days"] = (
#     df["Delivery_Date"] - df["Order_Date"]
# ).dt.days

# print(df)

# # Find orders taking more than 4 days
# result = df[df["Delivery_days"] > 4]

# print(result)

# # date + time
# df = pd.DataFrame({
#     "Login": [
#         "2026-09-20 08:30:15",
#         "2026-09-20 14:45:30",
#         "2026-09-21 18:20:10"
#     ]
# })

# df["login"] = pd.to_datetime(df["Login"])

# df["Hour"] = df["login"].dt.hour
# df["Minute"] = df["login"].dt.minute
# df["Second"] = df["login"].dt.second
# print(df)

# # Find users who logged in after 5 PM
# result = df[df["login"].dt.hour >= 17 ]
# print(result)

# import pandas as pd

# df = pd.DataFrame({
#     "Order_ID": [101, 102, 103, 104, 105, 106],
#     "Order_Date": [
#         "2026-01-15",
#         "2026-02-20",
#         "2026-02-25",
#         "2026-03-10",
#         "2026-03-18",
#         "2026-04-05"
#     ],
#     "Sales": [5000, 7000, 4500, 8000, 6000, 9000]
# })

# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# # Create Year.
# df["year"] = df["Order_Date"].dt.year

# # 2. Create Month.
# df["month"] = df["Order_Date"].dt.month

# # 3. Create Month_Name.
# df["Month_name"] = df["Order_Date"].dt.month_name()

# # 4. Create Day.
# df["day"] = df["Order_Date"].dt.day

# # 5. Create Day_Name.
# df["Day_name"] = df["Order_Date"].dt.day_name()

# # 6. Find only orders from February.
# result = df[df["Order_Date"].dt.month == 2]
# print(df)
# print(result)

# # 7. Find orders where Sales > 6000.
# result = df[df["Sales"] > 6000]
# print(result)

# # 8. Find orders after "2026-02-20".
# result = df[df["Order_Date"] > "2026-02-20"]
# print(result)

# # 9. Find the earliest order date.
# result = df["Order_Date"].max()
# print(result)

# # 10. Find the latest order date.
# result = df["Order_Date"].min()
# print(result)

# # 11. Sort from newest → oldest.
# result = (df.sort_values("Order_Date"))
# print(result)

# # 12. Find total sales for each month.
# result = df.groupby("month")["Sales"].sum()
# print(result)

# # 13. Find total sales for each month name.
# result = df.groupby("Month_name")["Sales"].sum()
# print(result)

# # 14. Find orders from January OR March.
# result = df[df["Order_Date"].dt.month.isin([1,3])]
# print(result)

# # 15. Find orders where the day of the month is greater than 20.
# result = df[df["Order_Date"].dt.day > 20]
# print(result)

# Gruoping the data
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj", "Kiran"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
#     "Salary": [30000, 45000, 35000, 50000, 40000, 45000]
# })

# print(df)

# # group of department by salary
# result = df.groupby("Department")["Salary"].sum()
# print(result)

# # average salary
# result = df.groupby("Department")["Salary"].mean()
# print(result)

# result = df.groupby("Department")["Salary"].max()
# print(result)

# result = df.groupby("Department")["Salary"].min()
# print(result)

# # count the employee
# result = df.groupby("Department")["Name"].count()
# print(result)

# # multiple calculation
# result = df.groupby("Department")["Salary"].agg(
#     ["sum", "mean", "max", "min"]
# )

# print(result)

# # agg with names
# result = df.groupby("Department")["Salary"].agg(
#     Total_Salary = "sum",
#     Average_Salary = "mean",
#     Maximum_Salary = "max",
#     Minimum_Salary = "min"
# )
# print(result)

# # group by two columns
# # df["Gender"] = ["Male","Female","Female","Male"]

# # df.groupby(["Department","Gender"])["Salary"].mean()

# # group by + multiple columns
# # result = df.groupby("Department")({
# #     "Salary" : "mean",
# #     "Age" : "max"
# # })
# # print(result)

# # groupby + sorting
# result = (
#     df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
# )

# print(result)

# # filtering
# result = (
#     df.groupby("Department")["Salary"].mean()
# )
# result = result[result > 40000]
# print(result)

# # Total sales by city:
# df.groupby("City")["Sales"].sum()

# # Average sales by city:
# df.groupby("City")["Sales"].mean()

# # Total sales by product:
# df.groupby("Product")["Sales"].sum()

# # Total sales by city and product:
# df.groupby(["City", "Product"])["Sales"].sum()

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj", "Kiran", "Meera", "Jay"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
#     "Age": [22, 24, 21, 25, 23, 26, 24, 22],
#     "Salary": [30000, 45000, 35000, 50000, 40000, 45000, 55000, 38000]
# })

# # Q1

# # Find total salary of each department.
# print(df.groupby("Department")["Salary"].sum())

# # Q2
# # Find average salary of each department.
# print(df.groupby("Department")["Salary"].mean())

# # Q3
# # Find maximum salary of each department.
# print(df.groupby("Department")["Salary"].max())

# # Q4
# # Find minimum salary of each department.
# print(df.groupby("Department")["Salary"].min())


# # Q5
# # Count the number of employees in each department.
# print(df.groupby("Department")["Salary"].count())


# # Q6
# # Find total salary AND average salary for each department.
# result = df.groupby("Department")["Salary"].agg(
#     ["sum","mean"]
# )
# print(result)

# # Q7
# # Find departments sorted by highest average salary → lowest.
# result = df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
# print(result)

# # Q8
# # Group by Department and Age, and find the average salary.
# result = df.groupby(["Department","Age"])["Salary"].mean()
# print(result)

# # Q9 ⭐
# # Find the department whose total salary is greater than 100000.
# result = (df.groupby("Department")["Salary"].sum())

# result = result[result > 100000]
# print(result)

# Q10 🔥
# Create a summary containing:

# Department
# Employee_Count
# Total_Salary
# Average_Salary
# Maximum_Salary
# Minimum_Salary

# # using one groupby() + agg().
# result = df.groupby("Department")["Salary"].agg(
#     ["count","sum","mean","max","min"]
# )
# print(result)

# import pandas as pd
# df = pd.read_excel("E:\\Pandas\\Pandas_GroupBy_Practice.xlsx")
# print(df)

# # 1. Find the total Salary for each Department.
# print(df.groupby("Department")["Salary"].sum())

# # 2. Find the average Salary for each Department.
# print(df.groupby("Department")["Salary"].mean())

# # 3. Find the maximum Salary for each Department.
# print(df.groupby("Department")["Salary"].max())

# # 4. Find the minimum Salary for each Department.
# print(df.groupby("Department")["Salary"].min())

# # 5. Count employees in each Department.
# print(df.groupby("Department")["Salary"].count())

# # 6. Find the total Sales for each City.
# print(df.groupby("City")["Sales"].sum())

# # 7. Find the average Sales for each Product.
# print(df.groupby("Product")["Sales"].mean())

# # 8. Find the total Units_Sold for each Product.
# print(df.groupby("Product")["Units_Sold"].sum())

# # 9. Find total Salary by Department and Gender.
# print(df.groupby(["Department","Gender"])["Salary"].sum())

# # 10. Find average Age by Department.
# print(df.groupby("Department")["Age"].mean())

# # 11. Find average Salary by City.
# print(df.groupby("City")["Salary"].mean())

# # 12. Find total Sales by Department and Product.
# print(df.groupby(["Department","Product"])["Sales"].sum())

# # 13. Find maximum Sales for each City.
# print(df.groupby("City")["Sales"].max())

# # 14. Find minimum Salary for each Gender.
# print(df.groupby("Gender")["Salary"].min())

# # 15. Find employee count by City.
# print(df.groupby("City")["Employee_ID"].count())

# # 16. Sort departments by highest average Salary to lowest.
# result = df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
# print(result)

# # 17. Find departments whose total Salary is greater than 200000.
# result = (df.groupby("Department")["Salary"].sum())
# result = result[result > 200000]
# print(result)

# # 18. Find cities whose total Sales are greater than 300000.
# result = (df.groupby("City")["Sales"].sum())
# result = result[result > 300000]
# print(result)

# # 19. Find the average Salary of employees aged 25 or above, grouped by Department.
# result = (df[df["Age"] > 25].groupby("Department")["Salary"].mean())
# print(result)

# # 20. Find total Sales for each Department, then sort highest to lowest.
# print(df.groupby("Department")["Sales"].sum().sort_values(ascending=False))

# # 21. Create one summary using agg(): Employee_Count, Total_Salary, Average_Salary, Max_Salary, Min_Salary for each Department.
# result = df.groupby("Department")["Salary"].agg(
#     ["count","sum","mean","max","min"]
# )
# print(result)

# # 22. Create a summary by City with Employee_Count, Average_Age, Average_Salary, Total_Sales.
# result = df.groupby("City").agg(
#     Employee_count = ("Employee_ID","count"),
#     Average_Age = ("Age","mean"),
#     Average_Salary = ("Salary","mean"),
#     Total_Sales = ("Sales","sum")
# )
# print(result)

# # 23. Find the Department + Product combination with the highest total Sales.
# print(df.groupby(["Department","Product"])["Sales"].sum().sort_values(ascending=False))

# # 24. Find the Department + Gender combination with the highest average Salary.
# print(df.groupby(["Department","Gender"])["Sales"].sum().sort_values(ascending=False))

# # 25. Find the Product with the highest total Units_Sold.
# print(df.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False))

# # 26. Find the top 3 cities by total Sales.
# print(df.groupby("City")["Sales"].sum().head(3))

# # 27. Find the top 3 Departments by average Salary.
# print(df.groupby("Department")["Salary"].mean().head(3))

# # 28. Find the average Sales per Unit for each Product. (Use Sales / Units_Sold first.)
# df["Sales_Per_Unit"] = df["Sales"] / df["Units_Sold"]

# result = df.groupby("Product")["Sales_Per_Unit"].mean()

# print(result)

# # 29. Create a Department summary and include total Sales, average Sales, total Units_Sold and employee count.
# result = df.groupby("Department").agg(
#     total_sales = ("Sales","sum"),
#     average_sales = ("Sales","mean"),
#     total_units_sold = ("Units_Sold","sum"),
#     employee_count = ("Employee_ID","count")
# )
# print(result)

# # 30. Find the City with the highest average Salary among employees aged 25+.
# result = df[df["Age"] > 25].groupby("City")["Salary"].mean().sort_values(ascending=False)
# print(result)

# # 31. Find the Product that generates the highest average Sales per employee record.
# result = df.groupby("Product")["Sales"].mean()
# answer = result.idxmax()
# print(answer)

# # 32. Build a complete Department × Product summary with total Sales and total Units_Sold.
# result = df.groupby(["Department","Product"]).agg(
#     total_sales = ("Sales","sum"),
#     totalunits_Sold = ("Units_Sold","sum")
# )
# print(result)

# # pivot table
import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Department": ["IT", "HR", "IT", "HR", "IT"],
#     "Salary": [30000, 40000, 35000, 45000, 50000]
# })

# print(df)

# # total salary
# result = df.pivot_table(
#     values = "Salary",
#     index = "Department",
#     aggfunc="sum"
# )
# print(result)

# # average salary
# print(df.pivot_table(
#     values="Salary",
#     index="Department",
#     aggfunc="mean"
# ))

# # Maximum salary
# print(df.pivot_table(
#     values="Salary",
#     index="Department",
#     aggfunc="max"
# ))

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj", "Pooja"],
#     "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
#     "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
#     "Salary": [30000, 40000, 35000, 45000, 50000, 38000]
# })

# print(df.pivot_table(
#     values="Salary",
#     index="Department",
#     columns="Gender",
#     aggfunc="sum",
#     fill_value=0,
#     margins=True
# ))

# df = pd.DataFrame({
#     "City": ["Surat", "Surat", "Rajkot", "Rajkot", "Surat"],
#     "Product": ["Laptop", "Mouse", "Laptop", "Mouse", "Laptop"],
#     "Sales": [50000, 2000, 45000, 3000, 55000]
# })

# # Q1
# # City-wise total Sales find karo.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     aggfunc="sum"
# ))

# # Q2
# # City-wise average Sales find karo.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     aggfunc="mean"
# ))

# # Q3
# # Product-wise total Sales find karo.
# print(df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc="sum"
# ))

# # Q4
# # City rows + Product columns + total Sales nu Pivot Table banao.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     columns="Product",
#     aggfunc="sum"
# ))

# # Q5
# # Q4 ma Grand Total add karo.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     columns="Product",
#     aggfunc="sum",
#     margins=True
# ))


# df = pd.read_excel("E:\\Pandas\\Pandas_PivotTable_Practice.xlsx")
# print(df)

# # multiple values
# df.pivot_table(
#     values=["Sales", "Units_Sold"],
#     index="Product",
#     aggfunc="sum"
# )

# # multiple aggeragation
# df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc=["sum", "mean", "max", "min"]
# )

# # pivot + sort
# result = df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc="sum"
# )
# result = result.sort_values("Sales", ascending=False)
# print(result)

# # pivot + filtering
# result = df.pivot_table(
#     values="Sales",
#     index="City",
#     aggfunc="sum"
# )
# result = result[result["Sales"] > 200000]
# print(result)

# # 1. Total Sales for each Product.
# print(df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc="sum"
# ))

# # 2. Total Sales for each City.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     aggfunc="sum"
# ))

# # 3. Average Sales for each Product.
# print(df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc="mean"
# ))

# # 4. Total Units_Sold for each Product.
# print(df.pivot_table(
#     values="Units_Sold",
#     index="Product",
#     aggfunc="sum"
# ))

# # 5. Total Sales for each Region.
# print(df.pivot_table(
#     values="Sales",
#     index="Region",
#     aggfunc="sum"
# ))

# # 6. Month as rows and total Sales as values.
# print(df.pivot_table(
#     values="Sales",
#     index="Month",
#     aggfunc="sum"
# ))

# # 7. City as rows, Product as columns, total Sales as values.
# print(df.pivot_table(
#     values="Sales",
#     index="City",
#     columns="Product",
#     aggfunc="sum",
#     fill_value=0
# ))

# # 8. Product as rows, Month as columns, total Sales as values.
# print(df.pivot_table(
#     values="Sales",
#     index="Product",
#     columns = "Month",
#     aggfunc="sum"
# ))

# # 9. Region as rows, Product as columns, total Units_Sold as values.
# print(df.pivot_table(
#     values="Units_Sold",
#     index="Region",
#     columns = "Product",
#     aggfunc="sum"
# ))

# # 10. City as rows with total Sales AND total Units_Sold.
# print(df.pivot_table(
#     values=["Sales","Units_Sold"],
#     index="City",
#     aggfunc="sum"
# ))

# # 11. Region as rows with average Sales.
# print(df.pivot_table(
#     values="Sales",
#     index="Region",
#     aggfunc="mean"
# ))

# # 12. Month as rows, Product as columns, total Sales.
# print(df.pivot_table(
#     values="Sales",
#     index="Month",
#     columns="Product",
#     aggfunc="sum"
# ))

# # 13. Add Grand Total to the Month × Product Sales pivot.
# print(df.pivot_table(
#     values="Sales",
#     index="Month",
#     columns="Product",
#     aggfunc="sum",
#     margins=True
# ))
# # 14. Average Sales by City and Product.
# print(df.pivot_table(
#     values="Sales",
#     index=["City","Product"],
#     aggfunc="mean"
# ))
# # 15. Find the Product with highest total Sales.
# result = df.pivot_table(
#     values="Sales",
#     index="Product",
#     aggfunc="sum"
# )
# print(result.sort_values("Sales", ascending=False).head(1))

# # 16. Find the City with highest total Sales.
# result = df.pivot_table(
#     values="Sales",
#     index="City",
#     aggfunc="sum"
# )
# print(result.sort_values("Sales", ascending=False).head(1))

# # 17. Region × Product pivot for total Sales; identify largest value.
# result = df.pivot_table(
#     values="Sales",
#     index=["Region","Product"],
#     aggfunc="sum"
# )
# print(result.sort_values("Sales",ascending=False).head(1))

# # 18. Month × Region pivot for total Sales.
# result = df.pivot_table(
#     values="Sales",
#     index=["Month","Region"],
#     aggfunc="sum"
# )
# print(result)

# # 19. City × Month pivot for total Sales.
# result = df.pivot_table(
#     values="Sales",
#     index=["City","Month"],
#     aggfunc="sum"
# )
# print(result)

# # 20. Product × Month pivot for total Units_Sold.
# result = df.pivot_table(
#     values="Units_Sold",
#     index=["Product","Month"],
#     aggfunc="sum"
# )
# print(result)

# # 21. City rows, Product columns, total Sales, Grand Total.
# result = df.pivot_table(
#     values="Sales",
#     index="City",
#     columns="Product",
#     aggfunc="sum",
#     fill_value=0,
#     margins=True
# )
# print(result)

# # 22. Region rows with Sales sum AND Sales mean.
# print(df.pivot_table(
#     values="Sales",
#     index="Region",
#     aggfunc=["sum","mean"]
# ))

# # 23. Product rows, Month columns, Sales sum AND Units_Sold sum.
# result = df.pivot_table(
#     values=["Sales","Units_Sold"],
#     index = "Product",
#     columns="Month",
#     aggfunc="sum"
# )
# print(result)

# # 24. Find the City–Product combination with highest Sales.
# result = df.pivot_table(
#     values="Sales",
#     index=["City","Product"],
#     aggfunc="sum"
# )
# result = result.sort_values("Sales",ascending=False).head(1)
# print(result)


# Merge & join
# Merge
import pandas as pd

# students = pd.DataFrame({
#     "Student_ID": [101, 102, 103, 104],
#     "Name": ["Rahul", "Priya", "Amit", "Neha"]
# })

# print(students)

# marks = pd.DataFrame({
#     "Student_ID": [101, 102, 103, 105],
#     "Marks": [85, 90, 78, 88]
# })

# print(marks)

# result = pd.merge(
#     students,marks,on="Student_ID"
# )
# print(result)

# # inner join
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="inner"
# )
# print(result)

# # left join
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="left"
# )
# print(result)

# # right join
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="right"
# )
# print(result)

# # outer join
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="outer"
# )
# print(result)

# # join
# students = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"]
# }, index=[101, 102, 103])

# marks = pd.DataFrame({
#     "Marks": [85, 90, 78]
# }, index=[101, 102, 103])
# result = students.join(marks)
# print(result)

# import pandas as pd

# students = pd.DataFrame({
#     "Student_ID": [101, 102, 103, 104],
#     "Name": ["Rahul", "Priya", "Amit", "Neha"]
# })

# marks = pd.DataFrame({
#     "Student_ID": [101, 102, 103, 105],
#     "Marks": [85, 90, 78, 88]
# })

# # Q1 — Inner Merge
# # students ane marks ne Student_ID par merge karo.
# # Condition: inner join use karo.
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="inner"
# )
# print(result)

# # Q2 — Left Merge
# # Badha students records rakhi ne marks sathe merge karo.
# # Condition: left join use karo.
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="left"
# )
# print(result)


# # Q3 — Right Merge
# # Badha marks records rakhi ne students sathe merge karo.
# # Condition: right join use karo.
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="right"
# )
# print(result)

# # Q4 — Outer Merge
# # Banne DataFrame na badha records combine karo.
# # Condition: outer join use karo.
# result = pd.merge(
#     students,
#     marks,
#     on="Student_ID",
#     how="outer"
# )
# print(result)

# # join
# students2 = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Age": [22, 23, 21]
# }, index=[101, 102, 103])

# marks2 = pd.DataFrame({
#     "Marks": [85, 90, 78]
# }, index=[101, 102, 103])
# print(students2.join(marks2))

# customers = pd.read_excel("E:\\Pandas\\merge_join_complete_practice.xlsx",sheet_name="Customers")
# print(customers)

# orders = pd.read_excel("E:\\Pandas\\merge_join_complete_practice.xlsx",sheet_name="Orders")
# print(orders)

# products = pd.read_excel("E:\\Pandas\\merge_join_complete_practice.xlsx",sheet_name="Products")
# print(products)

# Q1 — Inner Merge
# Customers અને Orders ને Customer_ID column પર inner merge કરો.
# # Goal: ફક્ત જે customers એ order કર્યો છે તે records જોઈએ.
# result = customers.merge(
#     orders,
#     on="Customer_ID",
#     how="inner"
# )
# print(result)

# # Q2 — Left Merge
# # Customers ને left table રાખીને Orders સાથે left merge કરો.
# # Goal: બધા customers દેખાવા જોઈએ, ભલે તેમણે order કર્યો હોય કે ન કર્યો હોય.
# result = customers.merge(
#     orders,
#     on="Customer_ID",
#     how="left"
# )
# print(result)

# # Q3 — Right Merge
# # Customers અને Orders નું right merge કરો.
# # Goal: Orders table ના બધા records રાખવાના છે.
# result = customers.merge(
#     orders,
#     on = "Customer_ID",
#     how="right"
# )
# print(result)

# # Q4 — Outer Merge
# # Customers અને Orders નું outer merge કરો.
# # Goal: બંને tables ના બધા records જોઈએ.
# result = customers.merge(
#     orders,
#     on = "Customer_ID",
#     how="outer"
# )
# print(result)

# # Q5 — Merge + Select Columns ⭐
# # Customers અને Orders ને merge કર્યા પછી ફક્ત આ columns બતાવો:
# # Name
# # City
# # Product
# # Sales
# result = customers.merge(
#     orders,
#     on="Customer_ID",
#     how="inner"
# )
# result = result[["Customer","City","Product_ID","Sales"]]
# print(result)

# # 🔥 Level 2 — Real Data Science Practice
# # Q6
# # દરેક customer ની total Sales શોધો.
# # merge → groupby → sum
# result = customers.merge(
#       orders,
#       on="Customer_ID",
#       how="inner"
# )
# result = result.groupby("Customer_ID")["Sales"].sum()
# print(result)

# # Q7
# # સૌથી વધારે total Sales કરનાર customer શોધો.
# result = customers.merge(
#       orders,
#       on="Customer_ID",
#       how="inner"
# )
# result = result.groupby("Customer_ID")["Sales"].sum()
# result = result.sort_values(ascending=False).head(1)
# print(result)

# # Q8
# # એવા customers શોધો જેમણે કોઈ order કર્યો નથી.
# result = customers.merge(
#       orders,
#       on="Customer_ID",
#       how="left"
# )
# print(result)

# # Q9
# # Orders અને Products ને appropriate common column પર merge કરીને દરેક order સાથે product ની information જોડો.
# result = orders.merge(
#     products,
#     on="Product_ID",
#     how="inner"
# )
# print(result)

# # Q10
# # Merged data માંથી નીચેની information બનાવો:
# # Customer Name
# # City
# # Product
# # Sales
# result = customers.merge(
#     orders,
#     on="Customer_ID",
#     how="inner"
# )

# result = result.merge(
#     products,
#     on="Product_ID",
#     how="inner"
# )

# result = result[["Customer", "City", "Product", "Sales"]]

# print(result)

# 🧠 Join Practice
# Q11
# Customers માંથી appropriate column ને index બનાવીને Orders સાથે .join() કરવાનો પ્રયાસ કરો.
# customers_index = customers.set_index("Customer_ID")

# orders_index = orders.set_index("Customer_ID")
# result = customers_index.join(orders_index)
# print(result)

# # Q12
# # Products table ને Orders સાથે .join() કરવાની શક્યતા તપાસો.
# # Question: Join કરવા માટે બંને DataFrames માં કયો common index/key જોઈએ?
# orders_index = orders.set_index("Product_ID")

# products_index = products.set_index("Product_ID")
# result = orders_index.join(products_index)
# print(result)

# Q13

# એક final table બનાવો જેમાં:

# Customer Name
# City
# Product
# Sales
# Product-related information

# બધી information એક જ DataFrame માં હોય.
# result = customers.merge(
#     orders,
#     on="Customer_ID",
#     how="inner"
# )
# result = result.merge(
#     products,
#     on="Product_ID",
#     how="inner"
# )
# result = result[["Customer","City","Product","Sales","Category","Price"]]
# print(result)

