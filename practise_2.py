# # apply function
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Salary": [30000, 45000, 28000]
# })

# df["Salary"] = df["Salary"].apply(lambda x: x * 1.10)

# print(df)

# # function with apply
# def increse_salary(x):
#     return x*1.10

# df["Salary"] = df["Salary"].apply(increse_salary)
# print(df)

# # with condition
# def check_salary(x):
#     if x>=40000:
#         return "High"
#     else:
#         return "Low"

# df["salary_level"] = df["Salary"].apply(check_salary)
# print(df)

# # apply + lambda
# df["salary_level"] = df["Salary"].apply(
#     lambda x : "High" if x >= 40000 else "Low"
# )
# print(df)

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Salary": [30000, 45000, 28000],
#     "Bonus": [5000, 7000, 4000]
# })

# df["Total"] = df.apply(
#     lambda row : row["Salary"] + row["Bonus"],
#     axis=1
# )
# print(df)

# import pandas as pd
# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 28, 35, 19, 42],
#     "Salary": [30000, 45000, 60000, 25000, 70000]
# })

# # Salary ના આધારે નવી column Salary_Level બનાવો:
# df["Salary_level"] = df["Salary"].apply(
#     lambda x: "High" if x>= 50000 else "Low"
# )
# print(df)

# # Age ના આધારે Age_Group બનાવો:
# df["Age_Group"] = df["Age"].apply(
#     lambda x: "Young" if x<25 else "Adult"
# )
# print(df)

# # દરેક salary માં 5000 bonus ઉમેરો અને Final_Salary બનાવો.
# df["Final_Salary"] = df["Salary"].apply(
#     lambda x: x + 5000
# )
# print(df)

# # Q4 Salary અને Age બંને જોઈને નવી column બનાવો:
# df["Condition"] = df.apply(
#     lambda row: "Eligible"
#     if row["Salary"] >= 50000 and row["Age"] >= 30
#     else "Not eligible",
#     axis=1
# )
# print(df)

# # q5 એક function બનાવો જે salary ને:

# # < 30000       → "Low"
# # 30000–50000   → "Medium"
# # > 50000       → "High"

# # માં convert કરે અને apply() થી column બનાવો.
# def convert_salary(x):
#     if x < 30000:
#         return "Low"
#     elif x >= 30000 and x <= 50000:
#         return "Medium"
#     else:
#         return "High" 

# df["Salary_level"] = df["Salary"].apply(convert_salary)
# print(df)

# # Map
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Gender": ["M", "F", "M"]
# })
# df["Gender"] = df["Gender"].map({
#     "M" : "Male",
#     "F" : "Female"
# })
# print(df)

# # # with function
# # def double_salary(x):
# #     return x * 2

# # df["Salary"] = df["Salary"].map(double_salary)
# # print(df)

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Gender_Code": [1, 2, 1, 2, 1],
#     "Department_Code": [101, 102, 101, 103, 102],
#     "Salary" : [30000,45000,28000,50000,35000]
# })

# df["Gender"] = df["Gender_Code"].map({
#     1 : "Male",
#     2 : "Female"
# })
# print(df)

# df["Department"] = df["Department_Code"].map({
#     101 : "IT",
#     102 : "HR",
#     103 : "Finance"
# })
# print(df)

# df["Final_Salary"] = df["Salary"].map(
#     lambda x : x + 5000
# )
# print(df)

# df["Type"] = df["Department"].map({
#     "IT" : "Technology",
#     "HR" : "Human Resource"
# })
# print(df)

# # Replace
# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "City": ["Surat", "Rajkot", "surat", "Ahmedabad"]
# })
# df["City"] = df["City"].replace("surat","Surat")
# print(df)

# # multiple replace
# df["City"] = df["City"].replace({
#     "Surat": "SRT",
#     "Rajkot": "RJK",
#     "Ahmedabad": "AMD"
# })

# # numeric value replace
# # df["Age"] = df["Age"].replace(0, 18)

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Gender": ["M", "F", "M", "F", "M"],
#     "City": ["surat", "Surat", "rajkot", "Rajkot", "AHMEDABAD"],
#     "Status": ["Y", "N", "Y", "N", "Y"]
# })
# df["Gender"] = df["Gender"].replace({
#     "M" : "Male",
#     "F" : "Female"
# })

# df["City"] = df["City"].replace({
#     "surat" : "Surat",
#     "rajkot" : "Rajkot",
#     "AHMEDABAD" : "Ahmedabad"
# })

# df["Status"] = df["Status"].replace({
#     "Y" : "Active",
#     "N" : "Inactive"
# })
# print(df)

# # string function
# # Lower 
# df["City"] = df["City"].str.lower()

# # upper
# df["City"] = df["City"].str.upper()

# # title
# df["City"] = df["City"].str.title()

# # strip
# df["City"] = df["City"].str.strip()

# # contains
# df[df["Name"].str.contains("rahul", case=False)]

# # startwith
# df[df["Name"].str.startswith("R")]

# # endwith
# df[df["Name"].str.endswith("a")]

# # len
# df["Name_Length"] = df["Name"].str.len()

# # replace
# df["City"] = df["City"].str.replace("Ahmedabad", "AMD")

# df = pd.DataFrame({
#     "Name": ["  rahul", "PRIYA  ", " amit ", "Neha"],
#     "City": ["surat", "RAJKOT", " Ahmedabad ", "surat"],
#     "Email": [
#         "rahul@gmail.com",
#         "priya@yahoo.com",
#         "amit@gmail.com",
#         "neha@outlook.com"
#     ]
# })

# df["Name"] = df["Name"].str.strip().str.title()


# df["City"] = df["City"].str.strip().str.title()


# df["Email"] = df["Email"].str.contains("gmail")


# df["Name_Length"] = df["Name"].str.len()


# result = df["Name"].str.strip().str.lower().str.startswith("A",na=False)
# print(result)

# df["Name"] = df["Name"].str.strip().str.lower()
# print(df)

# practise
# import pandas as pd
# df = pd.read_excel("E:\\Pandas\\Pandas_Apply_Map_Replace_String_Practice.xlsx")
# print(df)

# # Use apply() with lambda to add 10% to Salary and create Salary_10_Percent.
# df["Salary_10_percent"] = df["Salary"].apply(
#       lambda x : x + 1.10
# )


# # Use apply() to create Salary_Level: >=50000 High, otherwise Low.
# df["Salary_level"] = df["Salary"].apply(
#     lambda x: "High" if x>= 50000 else "Low"
# )


# # Use apply() with a custom function to create Age_Group: <25 Young, 25-35 Adult, >35 Senior.
# def Age_group(x):
#     if x < 25:
#         return "Young"
#     elif x >= 25 and x<= 35:
#         return "Adult"
#     else:
#         return "Senior"

# df["Age_group"] = df["Salary"].apply(Age_group)


# # Use apply(axis=1) to create Total_Score = Performance + Age.
# df["Total_Score"] = df.apply(
#     lambda row: row["Performance"] + row["Age"],
#     axis=1
# )


# # Use apply(axis=1) to create Eligible: Salary >=50000 AND Performance >=80.
# df["Condition"] = df.apply(
#     lambda row:"Eligible" 
#     if row["Salary"] >= 50000 and row["Performance"] >= 80
#     else "Not eligible",
#     axis=1
# )

# # Use apply() to create Performance_Level: >=85 Excellent, 70-84 Good, <70 Needs Improvement.
# def performance_level(x):
#     if x >= 85:
#         return "Excellent"
#     elif x>70 and x < 84:
#         return "Good"
#     else:
#         return "Needs Improvement"

# df["Performance_level"] = df["Performance"].apply(performance_level)
# print(df)

# # Use map() to convert Gender_Code: 1=Male, 2=Female.
# df["Gender"] = df["Gender_Code"].map({
#     1 : "Male",
#     2 : "Female"
# })

# # Use map() to convert Department_Code: 101=IT, 102=HR, 103=Finance.
# df["Department"] = df["Department_Code"].map({
#     101 : "IT",
#     102 : "HR",
#     103 : "Finance"
# })

# # Use map() to convert Status_Code: Y=Active, N=Inactive.
# df["Status"] = df["Status_Code"].map({
#     "Y" : "Active",
#     "N" : "Inactive"
# })

# # Use map() + lambda to increase every Salary by 2000.
# df["Salary"] = df["Salary"].map(
#     lambda x : x + 2000
# )
# # print(df)


# # Use replace() to convert Status_Code Y/N to Active/Inactive.
# df["Status"] = df["Status_Code"].replace({
#     "Y" : "Active",
#     "N" : "Inactive"
# })

# # Use replace() to convert Department_Code 101/102/103 to IT/HR/Finance.
# df["Department"] = df["Department_Code"].replace({
#     101 : "IT",
#     102 : "HR",
#     103 : "Finance"
# })

# # Use replace() to convert Gender_Code 1/2 to Male/Female.
# df["Gender"] = df["Gender_Code"].map({
#     1 : "Male",
#     2 : "Female"
# })
# print(df)

# # Use str.strip() to remove extra spaces from Name and City.
# df["Name"] = df["Name"].str.strip()
# print(df)

# df["City"] = df["City"].str.strip()
# print(df)

# # Use str.lower() to convert Name to lowercase.
# result = df["Name"].str.lower()
# print(result)

# # Use str.title() after strip() to clean City.
# df["City"] = df["City"].str.strip().str.title()
# print(df)

# # Use str.contains() to find employees whose Email contains gmail.
# df["Email"] = df["Email"].str.contains("gmail")
# print(df)

# # Use str.startswith() to find employees whose Name starts with 'a' after cleaning.
# result = df["Name"].str.startswith("a")
# print(result)

# # Use str.endswith() to find employees whose Name ends with 'a' after cleaning.
# result = df["Name"].str.endswith("a")
# print(result)

# # Use str.len() to create Name_Length.
# result = df["Name"].str.len()
# print(result)

# # Use str.replace() to replace spaces in Name with underscores.
# result = df["Name"].str.replace(" ","_")
# print(result)

# # Use chained string operations: strip + lower on Name.
# df["Name"] = df["Name"].str.strip().str.lower()
# print(df)

# # Use chained string operations: strip + title on City.
# df["City"] = df["City"].str.strip().str.title()
# print(df)

# # Create Clean_Name using strip + title, without changing the original Name.
# df["New_name"] = df["Name"].str.strip().str.title()
# print(df)

# # Create a final cleaned DataFrame with Clean_Name, Clean_City, Clean_Email, Department and Gender.
# df["Clean_name"] = df["Name"].str.strip().str.title()

# df["Clean_City"] = df["City"].str.strip().str.title()

# df["Clean_email"] = df["Email"].str.strip().str.title()

# df["Department"] = df["Department_Code"].map({
#     101 : "IT",
#     102 : "HR",
#     103 : "Finance"
# })

# df["Gender"] = df["Gender_Code"].map({
#     1 : "Male",
#     2 : "Female"
# })
# print(df)

# # Create a new column Final_Salary using apply() with a 5% raise.
# df["Final_salary"] = df["Salary"].apply(
#     lambda x : x * 1.05
# )
# print(df)

# # Create Bonus using apply(): Salary >=50000 gets 5000, otherwise 2000.
# df["Bonus_Apply"] = df["Salary"].apply(
#      lambda x : 5000 if x >= 50000 else 2000
# )
# print(df)

# # Create Salary_Category using apply() and three salary ranges.
# def salary_category(x):
#     if x < 30000:
#         return "Low"
#     elif x >= 30000 and x <= 50000:
#         return "Medium"
#     else:
#         return "High"

# df["Salary_Category"] = df["Salary"].apply(salary_category)
# print(df)


# # Create a final feature table using apply + map + replace + string cleaning.
# df["Clean_Name"] = df["Name"].str.strip().str.title()

# df["Clean_City"] = df["City"].str.strip().str.title()

# df["Clean_email"] = df["Email"].str.strip().str.title()

# df["Department"] = df["Department_Code"].map({
#     101 : "IT",
#     102 : "HR",
#     103 : "Finance"
# })

# df["Gender"] = df["Gender_Code"].map({
#     1 : "Male",
#     2 : "Female"
# })


# df["Status"] = df["Status_Code"].replace({
#     "Y": "Active",
#     "N": "Inactive"
# })

# df["Salary_Category"] = df["Salary"].apply(
#     lambda x: "Low" if x < 30000
#     else "Medium" if x <= 50000
#     else "High"
# )
# final_df = df[
#     [
#         "Employee_ID",
#         "Clean_Name",
#         "Clean_City",
#         "Department",
#         "Gender",
#         "Clean_email",  
#         "Salary",
#         "Salary_Category",
#         "Status"
#     ]
# ]

# print(final_df)
# aggeragation function 

# import pandas as pd
# df = pd.DataFrame({
#     "Name" : ["A","B","C","D"],
#     "Salary" : [30000,40000,50000,60000],
#     "Age" : [23,19,22,24]
# })
# print(df["Salary"].sum())

# # multiple columns per aggeragation
# print(df[["Salary"]].agg(["sum","mean","max","min"]))

# # diff columns mate diff function
# print(
#     df.agg({
#     "Salary": ["mean", "max"],
#     "Age": ["min", "max"]
# }))

# # group by sathe
# df = pd.DataFrame({
#     "Name": ["A", "B", "C", "D", "E"],
#     "Department": ["IT", "HR", "IT", "HR", "IT"],
#     "Salary": [30000, 40000, 50000, 60000, 70000]
# })
# print(df.groupby("Department")["Salary"].agg(["mean", "min", "max", "sum"]))

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Karan", "Meera"],
#     "Department": ["IT", "HR", "IT", "HR", "IT", "Finance"],
#     "Salary": [45000, 52000, 48000, 60000, 55000, 62000],
#     "Age": [22, 25, 24, 27, 23, 28]
# })

# # Q1. Find the total salary of all employees.
# print(df[["Salary"]].sum())

# # Q2. Find the average salary.
# print(df["Salary"].mean())

# # Q3. Find the highest salary.
# print(df['Salary'].max())

# # Q4. Find the lowest age.
# print(df["Age"].min())

# # q5. find the count
# print(df["Name"].count())

# # q6 size
# print(df.groupby("Department").size())

# # Q5. Find mean, min, and max of Salary using one aggregation command.
# print(df[["Salary"]].agg(["mean","min","max"]))

# # Indexing
# import pandas as pd
# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103],
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Salary": [30000, 45000, 35000]
# })

# print(df)

# df = df.set_index("Employee_ID")

# print(df)

# print(df.loc[101])
# print(df.loc[102,"Salary"])

# # reset index :: Bring index back as a normal column
# df = df.reset_index()
# print(df)

# # drop = true :: This is useful after sorting/filtering.
# df = df[df["Salary"] > 30000].reset_index(drop=True)
# print(df)

# # rename index
# df = df.rename(index = {
#     101 : "E101",
#     102 : "E102",
#     103 : "E103"
# })
# print(df)

# # syntax 
# # Set index
# df.set_index("Employee_ID")

# # Set multiple indexes
# df.set_index(["Department", "City"])

# # Access by index label
# df.loc[101]

# # Access specific value
# df.loc[101, "Salary"]

# # Reset index
# df.reset_index()

# # Reset without keeping old index
# df.reset_index(drop=True)

# # Rename index
# df.rename(index={101: "E101"})

# # Check index
# # df.index
# import pandas as pd
# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103],
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Salary": [30000, 45000, 35000],
#     "Department" : ["IT","IT","HR"]
# })

# df = df[(df["Salary"] > 40000) & (df["Department"] == "IT")].reset_index(drop=True)
# print(df)

# # Practise
# import pandas as pd

# df = pd.read_excel("E:\\Pandas\\pandas_indexing_practice.xlsx")
# print(df)

# # Set Order_ID as the index and display the row where Order_ID is 105.
# df = df.set_index("Order_ID")
# print(df)
# print(df.loc[105])

# # Set Order_ID as the index and display only the Sales of Order_ID 110.
# print(df.loc[110,"Sales"])

# # Find all orders where Sales > 20,000 and City = "Surat", then reset the index.

# df = df[(df["Sales"] > 20000) & (df["City"] == "Surat")].reset_index(drop=True)
# print(df)

# # Set Order_ID as the index and display orders from Order_ID 103 to 107.
# df = pd.read_excel("E:\\Pandas\\pandas_indexing_practice.xlsx")
# df = df.set_index("Order_ID")
# print(df.loc[103:107])

# # Set Order_ID as the index and display the Product and Profit of Order_ID 103.

# print(df.loc[[103],["Product","Profit"]])

# # Using .iloc, display the first 3 rows with only the Customer, Sales, and Profit columns.
# print(df.iloc[0:3,[4,5,6]])

# # Set Order_ID as the index and display all orders where Profit > 5,000.
# df = df.set_index("Order_ID")
# print(df)
# df = (df["Profit"] > 5000)
# print(df)

# # Find all orders where Quantity >= 3, then reset the index.
# df = df.set_index("Order_ID")
# print(df)
# df = (df["Quantity"] >= 3).reset_index(drop=True)
# print(df)

# # Set Order_ID as the index and display the Customer and Sales for Order_ID 101, 104, and 108.
# df = df.set_index("Order_ID")
# print(df)
# print(df.loc[[101,104,108],["Customer","Sales"]])

# # Set Order_ID as the index and display the last 5 rows using .iloc.
# df = df.set_index("Order_ID")
# print(df)
# print(df.iloc[-5:])

# # Working with duplicates
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Rahul", "Neha", "Priya"],
#     "Age": [22, 24, 21, 22, 25, 24],
#     "Department": ["IT", "HR", "IT", "IT", "Finance", "HR"],
#     "Salary": [30000, 45000, 28000, 30000, 50000, 45000]
# })

# print(df)
# print(df.duplicated())

# # count duplicates
# print(df.duplicated().sum())

# # display duplicate row
# print(df[df.duplicated()])

# # remove duplicate row
# df = df.drop_duplicates()
# print(df)

# # 6. Duplicate based on one column
# print(df.duplicated(subset=["Name"]))

# print(df[df.duplicated(subset=["Name"])])

# print(df.drop_duplicates(keep="last"))


# df = pd.DataFrame({
#     "Employee_ID": [101,102,103,104,105,106,107,108,109,110,111,112],
#     "Name": ["Rahul","Priya","Amit","Neha","Karan","Rahul","Pooja","Amit","Meena","Priya","Raj","Neha"],
#     "Age": [22,24,21,25,28,22,23,21,26,24,30,25],
#     "Department": ["IT","HR","IT","Finance","IT","IT","HR","IT","Finance","HR","IT","Finance"],
#     "Salary": [30000,45000,28000,50000,60000,30000,35000,28000,52000,45000,65000,50000],
#     "City": ["Surat","Rajkot","Ahmedabad","Surat","Vadodara","Surat","Rajkot","Ahmedabad","Surat","Rajkot","Vadodara","Surat"]
# })

# # "Find all completely duplicated rows using duplicated().",
# print(df.duplicated(subset=["Name"]))

# # "Count the total number of completely duplicated rows.",
# print(df.duplicated().sum())

# # "Display only the duplicate rows.",
# print(df[df.duplicated()])

# # "Remove all completely duplicated rows.",
# print(df.drop_duplicates(subset=["Name"]))

# # "Find duplicate Employee names using duplicated(subset=['Name']).",
# print(df[df.duplicated(subset=["Name"])])

# # "Display only rows where the Name is duplicated."
# print(df[df.duplicated(subset=["Name"], keep=False)])

# # "Count the duplicate Names."
# print(df.duplicated(subset=["Name"]).sum())

# # "Remove duplicate rows based only on Name, keeping the first occurrence.",
# print(df[df.duplicated(subset=["Name"], keep="first")])

# # "Remove duplicate rows based only on Name, keeping the last occurrence.",
# print(df[df.duplicated(subset=["Name"], keep="last")])

# # "Remove all rows whose Name is duplicated using keep=False.",
# print(df[df.duplicated(subset=["Name"], keep=False)])

# # "Check whether the DataFrame contains any complete duplicate rows.",
# print(df.duplicated().any())

# # "Remove complete duplicates and reset the index using drop=True."
# df = df.drop_duplicates().reset_index(drop=True)

# print(df)

# Advance operation
import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 28, 35, 24, 31],
#     "Department": ["IT", "HR", "IT", "Finance", "IT"],
#     "Salary": [30000, 45000, 60000, 35000, 52000]
# })

# # query
# print(df.query("Salary > 40000 and Department == 'IT'"))

# salary_limit = 40000

# print(df.query("Salary > @salary_limit"))

# # explode

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Skills": [
#         ["Python", "SQL"],
#         ["Python", "Excel", "Power BI"],
#         ["Python", "ML"]
#     ]
# })

# print(df)
# df = df.explode("Skills")
# print(df)

# # melt
# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya"],
#     "Math": [80, 90],
#     "Python": [85, 95],
#     "SQL": [75, 88]
# })

# print(df)

# # wide data -> long data using melt
# long_df = df.melt(
#     id_vars = "Name",
#     var_name = "Subject",
#     value_name = "Marks"
# )
# print(long_df)

# # stack
# df = pd.DataFrame({
#     "Math": [80, 90],
#     "Python": [85, 95]
# }, index=["Rahul", "Priya"])

# print(df)

# df = df.stack()
# print(df)

# # unstack
# print(df.unstack())

# # transpose
# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya"],
#     "Age": [22, 24],
#     "Salary": [30000, 45000]
# })
# print(df)
# print(df.T)


# # clip
# # set lower and upper value
# df = pd.DataFrame({
#     "Name": ["A", "B", "C", "D"],
#     "Marks": [35, 55, 75, 110]
# })
# df["Marks"] = df["Marks"].clip(40,100)
# print(df)

# import pandas as pd

# students = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Skills": [
#         ["Python", "SQL"],
#         ["Python", "Excel", "Power BI"],
#         ["Python", "ML"],
#         ["SQL", "Tableau"],
#         ["Python", "SQL", "ML"]
#     ],
#     "Math": [80, 90, 75, 85, 70],
#     "Python": [85, 95, 80, 88, 75],
#     "SQL": [78, 90, 82, 80, 72]
# })

# print(students)

# # Create a DataFrame where the Skills column contains multiple skills as lists. Use explode() to convert each skill into a separate row.
# q1 = students.explode("Skills")
# print(q1)

# # Using a student marks DataFrame with Math, Python, and SQL columns, use melt() to convert the data from Wide Data to Long Data.
# q2 = students.melt(
#     id_vars = "Name",
#     var_name= "Subject",
#     value_name="Marks"
# )
# print(q2)

# # Using a DataFrame with Name, Math, and Python, use stack() to move the subject columns into the index.
# q3 = students.stack()
# print(q3)

# # Take the result from Question 3 and use unstack() to convert it back to the original structure.
# print(q3.unstack())

# # Create a DataFrame with Name, Age, and Salary. Use transpose() to interchange rows and columns
# employees = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Age": [22, 25, 30, 28, 35],
#     "Salary": [25000, 45000, 80000, 65000, 95000]
# })
# print(employees.T)

# # Create a DataFrame with Marks containing values below 40 and above 100. Use clip() to restrict all marks between 40 and 100.
# marks = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj"],
#     "Marks": [25, 45, 78, 105, 120]
# })

# print(marks)
# marks["Marks"] = marks["Marks"].clip(40,100)
# print(marks)

# # Create a Long DataFrame containing Name, Subject, and Marks. Use pivot() to convert it into Wide Data.
# long_df = pd.DataFrame({
#     "Name": ["Rahul", "Rahul", "Rahul",
#              "Priya", "Priya", "Priya",
#              "Amit", "Amit", "Amit"],

#     "Subject": ["Math", "Python", "SQL",
#                 "Math", "Python", "SQL",
#                 "Math", "Python", "SQL"],

#     "Marks": [80, 85, 78,
#               90, 95, 88,
#               75, 82, 80]
# })
# q7 = long_df.pivot_table(
#     index="Name",
#     columns="Subject",
#     values="Marks"
# )
# print(q7)

# # Create a Wide DataFrame containing Name, Math, Python, and SQL. Use melt() to convert it into Long Data.
# wide_df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit"],
#     "Math": [80, 90, 75],
#     "Python": [85, 95, 82],
#     "SQL": [78, 88, 80]
# })

# print(wide_df)
# q8 = wide_df.melt(
#     id_vars = "Name",
#     var_name= "Subject",
#     value_name="Marks"
# )
# print(q8)

# # Create a Long DataFrame containing City, Product, and Sales. Use pivot() to make Product the columns and City the index.
# sales = pd.DataFrame({
#     "City": ["Surat", "Surat", "Rajkot", "Rajkot", "Ahmedabad", "Ahmedabad"],
#     "Product": ["Laptop", "Mouse", "Laptop", "Mouse", "Laptop", "Mouse"],
#     "Sales": [60000, 5000, 55000, 7000, 65000, 6000]
# })

# print(sales)
# df = sales.pivot_table(
#     index="City",
#     values="Sales",
#     columns="Product"
# )
# print(df)

# # Create a DataFrame where each employee has a list of purchased products. Use explode() to create one row for each purchased product.
# products = pd.DataFrame({
#     "Employee": ["Rahul", "Priya", "Amit", "Neha"],
#     "Purchased_Products": [
#         ["Laptop", "Mouse"],
#         ["Keyboard", "Monitor", "Mouse"],
#         ["Laptop", "Headphones"],
#         ["Monitor", "Keyboard"]
#     ]
# })
# df = products.explode("Purchased_Products")
# print(df)

# # Create a DataFrame with Salary values ranging from 20,000 to 100,000. Use clip() to limit salaries between 30,000 and 70,000.
# import pandas as pd

# salary = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Raj", "Karan"],
#     "Salary": [20000, 28000, 45000, 60000, 75000, 100000]
# })

# print(salary)
# salary["Salary"] = salary["Salary"].clip(30000,70000)
# print(salary)

# # Create a Wide DataFrame with Name, January, February, and March sales. Use melt() to convert the monthly sales into Month and Sales columns.
# monthly_sales = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha"],
#     "January": [10000, 12000, 9000, 15000],
#     "February": [11000, 14000, 10000, 16000],
#     "March": [13000, 15000, 12000, 17000]
# })
# df = monthly_sales.melt(
#     id_vars="Name",
#     var_name="Month",
#     value_name="Sales"
# )
# print(df)

# window function
import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Rahul", "Priya", "Amit", "Neha", "Karan"],
#     "Department": ["IT", "HR", "IT", "HR", "IT"],
#     "Salary": [45000, 52000, 48000, 60000, 55000]
# })

# df["Cumulative_Salary"] = df["Salary"].cumsum()
# print(df)

# # cummax :: highest salary
# df["Running_Max"] = df["Salary"].cummax()
# print(df)

# # cummin :: lowest salary
# df["Running_Min"] = df["Salary"].cummin()
# print(df)

# # cumprod
# df = pd.DataFrame({
#     "Month": [1, 2, 3, 4],
#     "Growth": [1.1, 1.2, 1.1, 1.3]
# })
# df["Cumulative_Growth"] = df["Growth"].cumprod()
# print(df)

# # rolling
# # 3 lakhu to 3 sales nu mean avshe mate 1 and 2 incomplete reshe
# df = pd.DataFrame({
#     "Day": [1, 2, 3, 4, 5, 6],
#     "Sales": [100, 200, 300, 400, 500, 600]
# })

# df["rolling_mean"] = df["Sales"].rolling(3).mean()
# print(df)

# df["Rolling_sum"] = df["Sales"].rolling(3).sum()
# print(df)

# df["Rolling_Max"] = df["Sales"].rolling(3).max()
# print(df)

# df["Rolling_Min"] = df["Sales"].rolling(3).min()
# print(df)

# # expanding
# df["Expanding_Sum"] = df["Sales"].expanding().sum()
# print(df)

# df["Expanding_mean"] = df["Sales"].expanding().mean()
# print(df)

# df = pd.DataFrame({
#     "Day": [1, 2, 3, 4, 5, 6, 7],
#     "Sales": [100, 150, 200, 180, 250, 300, 280]
# })

# # Q1
# # 3-day rolling mean બનાવો.
# df["rolling"] = df["Sales"].rolling(3).mean()
# print(df)


# # Q8 ⭐⭐
# # Sales માટે cumprod() બનાવો.
# df["Sales_Prod"] = df["Sales"].cumprod()
# print(df)

# # Q9 🔥
# # Rolling અને Expanding વચ્ચેનો difference codeથી demonstrate કરો.
# df["rolling"] = df["Sales"].rolling(3).mean()
# print(df)

# df["Expanding"] = df["Sales"].expanding().mean()
# print(df)

# df = pd.read_excel("E:\\Pandas\\pandas_window_functions_practice.xlsx")
# print(df)

# # Q1. Sales માટે 3-day rolling mean બનાવો.
# df["Rolling_mean"] = df["Sales"].rolling(3).mean()

# # Q2. Sales માટે 3-day rolling sum બનાવો.
# df["Rolling_sum"] = df["Sales"].rolling(3).sum()

# # Q3. Sales માટે 3-day rolling maximum શોધો.
# df["Rolling_max"] = df["Sales"].rolling(3).max()

# # Q4. Sales માટે 3-day rolling minimum શોધો.
# df["Rolling_min"] = df["Sales"].rolling(3).min()

# # Q5. Profit માટે 3-day rolling mean બનાવો.
# df["Rolling_mean"] = df["Profit"].rolling(3).mean()
# print(df)

# Expanding

# # Q6. Sales માટે expanding sum બનાવો.
# df["Expanding_sum"] = df["Sales"].expanding().sum()

# # Q7. Sales માટે expanding mean બનાવો.
# df["Expanding_mean"] = df["Sales"].expanding().mean()

# # Q8. Profit માટે expanding maximum શોધો.
# df["Expanding_max"] = df["Profit"].expanding().max()
# print(df)

# # Cumulative

# # Q9. Sales માટે cumsum() નો ઉપયોગ કરીને cumulative sales બનાવો.
# df["Cumulative_sum"] = df["Sales"].cumsum()

# # Q10. Orders માટે cumulative total બનાવો.
# df["Cumulative_sum"] = df["Orders"].cumsum()

# # Q11. Profit માટે cummax() નો ઉપયોગ કરીને અત્યાર સુધીનો highest profit શોધો.
# df["cumulative_max"] = df["Profit"].cummax()
# print(df)

# ⭐ Challenge

# Q12. એક સાથે આ columns બનાવો:

# Rolling_Mean
# Rolling_Sum
# Rolling_Max
# Rolling_Min
# Expanding_Sum
# Expanding_Mean
# Cumulative_Sales

# df["Rolling_mean"] = df["Sales"].rolling(3).mean()

# df["Rolling_sum"] = df["Sales"].rolling(3).sum()

# df["Rolling_max"] = df["Sales"].rolling(3).max()

# df["Rolling_min"] = df["Sales"].rolling(3).min()

# df["Expanding_sum"] = df["Sales"].expanding().sum()

# df["Expanding_mean"] = df["Sales"].expanding().mean()

# df["Cumulative_sum"] = df["Sales"].cumsum()
# print(df)

# # Q13. Sales માટે 5-day rolling mean બનાવો.
# df["Rolling_mean"] = df["Sales"].rolling(5).mean()

# # Q14. Profit માટે 5-day rolling sum બનાવો.
# df["Rolling_sum"] = df["Sales"].rolling(5).sum()
# print(df)

# # Multiindex
# df = pd.DataFrame({
#     "Department": ["IT", "IT", "IT", "HR", "HR", "Finance"],
#     "City": ["Surat", "Rajkot", "Ahmedabad", "Surat", "Rajkot", "Surat"],
#     "Employee": ["Rahul", "Amit", "Neha", "Priya", "Karan", "Meena"],
#     "Salary": [40000, 45000, 50000, 35000, 42000, 60000]
# })

# df = df.set_index(["Department", "City"])
# print(df)

# # Selecting data from multiindex
# print(df.loc["IT"])
# print(df.loc[("IT", "Surat"), "Salary"])

# # Indexslice
# # syntax :
# # df.loc[
# #     idx[Department, City],
# #     Columns
# # ]

# idx = pd.IndexSlice 
# print(df.loc[idx["IT",:],:])
# print(df.loc[idx[["IT","HR"],:],:])

# print(df.loc[idx["IT",["Surat","Rajkot"]],:])

# # swaplevel
# print(df.swaplevel("Department","City"))

# # droplevel
# print(df.droplevel("City"))

# # sorting
# print(df.sort_index(level="Department"))

# # sorting by multiple levels
# df.sort_index(
#     level=["Department", "City"]
# )
# print(df)

# data = {
#     ("Salary", "Mean"): [40000, 45000],
#     ("Salary", "Max"): [50000, 60000],
#     ("Age", "Mean"): [25, 28],
#     ("Age", "Max"): [30, 35]
# }

# df = pd.DataFrame(
#     data,
#     index=["IT", "HR"]
# )
# print(df)

# # Multilevel Columns
# df = pd.DataFrame({
#     "Department": ["IT", "IT", "HR", "HR"],
#     "Salary": [40000, 50000, 35000, 45000],
#     "Age": [22, 25, 24, 28]
# })

# result = df.groupby("Department").agg({
#     "Salary": ["mean", "max", "min"],
#     "Age": ["mean", "max"]
# })
# print(result)

# df = pd.read_excel("E:\\Pandas\\Pandas_MultiIndex_Practice.xlsx")
# print(df)

# # Create a MultiIndex using Department and City.
# df = df.set_index(["Department","City"])
# print(df)

# # Display all employees who belong to the IT department.
# idx = pd.IndexSlice
# df = (df.loc[idx["IT",:],:])
# print(df)

# # Select the employee data for IT and Surat.
# df = (df.loc[idx["IT",["Surat"],:],:])
# print(df)

# # Select only the Salary of the HR employee(s) in Rajkot.
# df = df.set_index(["Department", "City"])
# print(df.loc[("HR", "Rajkot"), "Salary"])

# # Create an IndexSlice object and use it to select all IT and HR departments.
# idx = pd.IndexSlice
# print(df.loc[idx[["IT","HR"],:],:])

# # Using IndexSlice, select only IT employees from Surat and Rajkot.
# idx = pd.IndexSlice
# print(df.loc[idx["IT",["Surat","Rajkot"],:],:])

# # Swap the Department and City index levels using swaplevel().
# print(df.swaplevel("Department","City"))

# # After swaplevel(), sort the DataFrame according to the new index order.
# print(df.sort_index())

# # Remove the City index level using droplevel().
# print(df.droplevel("City"))

# # Sort the MultiIndex DataFrame by Department.
# print(df.sort_index(level="Department"))

# # Sort the MultiIndex DataFrame by City.
# print(df.sort_index(level="City"))

# # Sort the MultiIndex DataFrame by Department and then City.
# print(df.sort_index(level=["Department","City"]))

# # Create a MultiIndex result using groupby(['Department', 'City']) and calculate average Salary.
# result = df.groupby(["Department","City"]).agg({
#     "Salary" : ["mean"]
# })
# print(result)

# # Reset the index of the result from Question 13.
# result = result.reset_index()
# print(result)

# # Group by Department and City and calculate total Salary and average Performance.
# result = df.groupby(["Department","City"]).agg({
#     "Salary" : ["sum"],
#     "Performance" : ["mean"]
# })
# print(result)

# # Create multilevel columns using groupby('Department').agg() for Salary: mean, max, min.
# result = df.groupby("Department").agg({
#     "Salary" : ["mean","max","min"]
# })
# print(result)

# # Create multilevel columns using groupby('Department').agg() for Salary and Performance.
# result = df.groupby("Department").agg({
#     "Salary" : ["mean","max","min"],
#     "Performance" : ["mean","max","min"]
# })
# print(result)

# # Select the Salary → mean column from the multilevel-column result.
# df = pd.DataFrame({
#     "Department": ["IT", "IT", "IT", "HR", "HR", "HR", "Finance", "Finance"],
#     "Employee": ["Rahul", "Amit", "Neha", "Priya", "Karan", "Pooja", "Meena", "Jignesh"],
#     "Salary": [40000, 45000, 52000, 35000, 42000, 48000, 60000, 65000],
#     "Performance": [85, 78, 92, 88, 75, 90, 95, 82]
# })

# result = df.groupby("Department").agg({
#     "Salary": ["mean", "max", "min"],
#     "Performance": ["mean", "max"]
# })
# print(result[("Salary","mean")])

# # Select all Salary-related columns from the multilevel-column result.
# print(result["Salary"])

# # Flatten the multilevel columns into names such as Salary_mean, Salary_max, Salary_min.
# result.columns = [
#     "_".join(col)
#     for col in result.columns
# ]

# print(result)

# # Create a final report with Department and City as MultiIndex and calculate total Salary, average Age, and average Performance.
# df = df.groupby(["Department","City"]).agg({
#     "Salary" : "sum",
#     "Age" : "mean",
#     "Performance" : "mean"
# })
# print(df)

# # Reset the MultiIndex from Question 21 and create a normal DataFrame suitable for further analysis.
# df = df.reset_index()
# print(df)


# # ranking
# df = pd.DataFrame({
#     "Date": pd.date_range("2026-09-01", periods=12, freq="D"),
#     "Product": ["Laptop","Phone","Tablet","Laptop","Phone","Tablet","Laptop","Phone","Tablet","Laptop","Phone","Tablet"],
#     "Department": ["IT","Sales","Sales","IT","Sales","Sales","IT","Sales","Sales","IT","Sales","Sales"],
#     "Sales": [50000, 30000, 20000, 55000, 33000, 22000, 60000, 36000, 25000, 58000, 40000, 28000],
#     "Profit": [8000, 5000, 3000, 9000, 5500, 3500, 10000, 6000, 4000, 9500, 6500, 4500],
#     "Orders": [5, 8, 6, 6, 9, 7, 7, 10, 8, 6, 11, 9]
# })
# print(df)

# # rank
# df["Rank"] = df["Sales"].rank(ascending=True)
# print(df)

# # rank with groupby
# # groupwise ranking Alag Alag thashe
# df["Department_rank"] = (
#     df.groupby("Department")["Sales"].rank(ascending=False)
# )
# print(df)

# # shift
# df["Previous_sales"] = df["Sales"].shift(1)
# print(df)

# # next
# df["Next_Sales"] = df["Sales"].shift(-1)
# print(df)

# # diff :: current - previous no difference ape
# df["Sales_Difference"] = df["Sales"].diff()
# print(df)

# # current with specific period
# df["Sales_Difference"] = df["Sales"].diff(2)
# print(df)

# # pct_change :: percentage change
# # formula :: current - previous/100
# df["Sales_Pct_Change"] = df["Sales"].pct_change()
# print(df)

# # Percentage Change Analysis
# df["Sales_Growth_%"] = (
#     df["Sales"].pct_change() * 100
# )
# print(df)

# # correlation
# print(df["Sales"].corr(df["Profit"]))

# # covariance
# # print(df["Sales"].cov(df["Profit"]))

# import pandas as pd

# df = pd.DataFrame({
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#               "Jul", "Aug", "Sep", "Oct"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR",
#                    "IT", "Finance", "HR", "IT", "Finance"],
#     "Sales": [12000, 15000, 18000, 14000, 22000,
#               25000, 20000, 28000, 30000, 26000],
#     "Profit": [2000, 2500, 3200, 1800, 4000,
#                4500, 3000, 5200, 6000, 4800],
#     "Orders": [12, 15, 18, 14, 22, 25, 20, 28, 30, 26]
# })

# # Q1. Create a new column Sales_Rank and rank Sales in descending order, assigning Rank 1 to the highest sales.
# df["Sales_rank"] = df["Sales"].rank(ascending=False)
# print(df)

# # Q2. Create a new column Previous_Sales using shift() to display the previous month's sales.
# df["Previous_Sales"] = df["Sales"].shift(1)
# print(df)

# # Q3. Create a new column Next_Sales using shift() to display the next month's sales.
# df["Next_Sales"] = df["Sales"].shift(-1)
# print(df)

# # Q4. Calculate the difference between the current month's sales and the previous month's sales using diff().
# df["Different_sales"] = df["Sales"].diff()
# print(df)

# # Q5. Calculate the percentage change in Sales from the previous month using pct_change(). Display the result as a percentage.
# df["Sales_change"] = df["Sales"].pct_change()
# print(df)

# # Q6. Create a column Profit_Difference that calculates the difference in Profit between consecutive months.
# df["Profit_difference"] = df["Profit"].diff()
# print(df)

# # Q7. Create a column Profit_Change_Percentage that calculates the month-to-month percentage change in Profit.
# df["Profit_change_percentage"] = df["Profit"].pct_change()*100
# print(df[["Month", "Profit", "Profit_change_percentage"]])

# # Q8. Calculate the correlation between Sales and Profit.
# print(df["Sales"].corr(df["Profit"]))

# # Q9. Calculate the covariance between Sales and Profit.
# print(df["Sales"].cov(df["Profit"]))

# # Q10. Rank Profit in ascending order, assigning Rank 1 to the lowest profit.
# df["profit_rank"] = df["Profit"].rank(ascending=True)
# print(df)

# # Q11. Calculate the percentage change in Orders from the previous month and store it in a new column called Orders_Change_%.
# df["Orders_change_%"] = df["Orders"].shift(1)
# print(df)

# # Q12. Rank Sales separately within each Department, assigning Rank 1 to the highest sales in each department.
# df["Department_rank"] = df.groupby("Department")["Sales"].rank(ascending=False)
# print(df)

# Q13. Create a column Sales_Growth_Status using Sales_Difference:
# Positive difference → "Increased"
# Negative difference → "Decreased"
# Zero difference → "No Change"

# df["Sales_difference"] = df["Sales"].diff()
# df["Sales_growth_status"] = df["Sales_difference"].apply(
#     lambda x : "Increased" if x>0
#     else "Decreased" if x < 0
#     else "No change"
# )
# print(df)

# # Q14. Create a new column Sales_vs_Next_Month that calculates the difference between the next month's sales and the current month's sales.
# df["Sales_vs_next_month"] = df["Sales"].diff()
# print(df)

# # Q15. ⭐ Final Challenge: Create a final report containing these columns:
# # Month
# # Sales
# # Previous_Sales
# # Sales_Difference
# # Sales_Change_%
# # Sales_Rank
# # Profit_Change_Percentage
# # Sort the final report by Sales_Rank in ascending order.

# df["Previous_sales"] = df["Sales"].shift(1)

# df["Sales_difference"] = df["Sales"].diff()

# df["Sales_changes_%"] = df["Sales"].pct_change()*100

# df["Sales_rank"] = df["Sales"].rank(ascending=False).astype(int)

# df["Profit_change_percentage"] = df["Profit"].pct_change()*100

# final_report = df[
#     [
#         "Month",
#         "Sales",
#         "Previous_sales",
#         "Sales_difference",
#         "Sales_changes_%",
#         "Sales_rank",
#         "Profit_change_percentage"
#     ]
# ]

# final_report = final_report.sort_values(
#     "Sales_rank"
# )
# print(final_report)

# Resampling 
# df = pd.DataFrame({
#     "Date": [
#         "2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05",
#         "2026-01-06", "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10",
#         "2026-01-11", "2026-01-12", "2026-01-13", "2026-01-14", "2026-01-15",
#         "2026-01-16", "2026-01-17", "2026-01-18", "2026-01-19", "2026-01-20",
#         "2026-01-21", "2026-01-22", "2026-01-23", "2026-01-24", "2026-01-25",
#         "2026-01-26", "2026-01-27", "2026-01-28", "2026-01-29", "2026-01-30",
#         "2026-01-31"
#     ],
#     "Sales": [
#         1200, 1500, 1800, 1100, 2200, 2500, 2100, 2800, 3000, 2600,
#         1900, 2300, 2700, 3100, 2900, 2000, 2400, 2600, 3200, 3500,
#         2800, 3000, 3300, 3600, 3100, 2900, 3400, 3700, 3900, 3500, 4000
#     ],
#     "Orders": [
#         12, 15, 18, 11, 22, 25, 21, 28, 30, 26,
#         19, 23, 27, 31, 29, 20, 24, 26, 32, 35,
#         28, 30, 33, 36, 31, 29, 34, 37, 39, 35, 40
#     ],
#     "Profit": [
#         200, 250, 300, 180, 400, 450, 380, 500, 550, 480,
#         320, 410, 490, 580, 520, 350, 420, 460, 600, 650,
#         500, 540, 620, 680, 570, 520, 640, 700, 750, 660, 780
#     ],
#     "Customers": [
#         10, 13, 16, 9, 19, 22, 18, 25, 27, 23,
#         17, 20, 24, 28, 26, 18, 21, 23, 29, 32,
#         25, 27, 30, 33, 28, 26, 31, 34, 36, 32, 38
#     ]
# })
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# print(df)

# # monthly sales
# print(df.resample("ME")["Sales"].sum())

# # monthly average
# print(df.resample("ME")["Sales"].mean())

# # weekly total
# print(df.resample("W")["Sales"].sum())

# # yearly total
# print(df.resample("YE")["Sales"].sum())

# # multiple 
# monthly_report = df.resample("ME")["Sales"].agg(
#     ["sum", "mean", "max", "min"]
# )

# print(monthly_report)

# # multiple columns
# monthly_report = df.resample("ME").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Orders": "sum"
# })
# print(monthly_report)

# # resampling + diff aggeragation
# monthly_report = df.resample("ME").agg({
#     "Sales": ["sum", "mean", "max"],
#     "Profit": ["sum", "mean"],
#     "Orders": "sum"
# })
# print(monthly_report)

# df = pd.read_excel("E:\\Pandas\\resampling.xlsx")
# print(df)

# # Q1. Convert the Date column to datetime and set it as the index.
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# print(df) 

# # Q2. Calculate total monthly Sales.
# print(df.resample("ME")["Sales"].sum())

# # Q3. Calculate average monthly Sales.
# print(df.resample("ME")["Sales"].mean())

# # Q4. Calculate total weekly Sales.
# print(df.resample("W")["Sales"].sum())

# # Q5. Calculate total monthly Profit.
# print(df.resample("ME")["Profit"].sum())

# # Q6. Calculate average monthly Profit.
# print(df.resample("ME")["Profit"].mean())

# # Q7. Calculate total monthly Orders.
# print(df.resample("ME")["Orders"].sum())

# # Q8. Calculate the maximum Sales for each week.
# print(df.resample("W")["Sales"].max())


# # Q9. Calculate the minimum Profit for each week.
# print(df.resample("W")["Profit"].min())

# # Q10. Create a monthly report containing:

# # Total Sales
# # Total Orders
# # Total Profit
# # Average Customers

# Monthly_report = df.resample("ME").agg({
#     "Sales" : "sum",
#     "Orders" : "sum",
#     "Profit" : "sum",
#     "Customers" : "mean"
# })
# print(Monthly_report)

# # Q11. 
# # Create a monthly report using .agg() with:

# # Sales → sum, mean, max, min
# # Profit → sum, mean
# Monthly_report = df.resample("ME").agg({
#     "Sales" : ["sum","mean","max","min"],
#     "Profit" : ["sum","mean"]
# })
# print(Monthly_report)

# # Q12. 
# # Create a yearly report containing total Sales, Profit, Orders, and Customers.
# Yearly_report = df.resample("YE").agg({
#     "Sales" : "sum",
#     "Profit" : "sum",
#     "Orders" : "sum",
#     "Customers" : "sum"
# })
# print(Yearly_report)

# # Q13. 
# # Create a weekly report with:

# # Total Sales
# # Average Sales
# # Total Orders
# # Total Profit
# weekly_report = df.resample("W").agg({
#     "Sales" : "sum",
#     "Sales" : "mean",
#     "Orders" : "sum",
#     "Profit" : "sum"
# })
# print(weekly_report)

# # Q14. 
# # Find the month with the highest total Sales.
# monthly_sales = df.resample("ME")["Sales"].sum()

# highest_sales_month = monthly_sales.idxmax()
# highest_sales_value = monthly_sales.max()

# print("Month:", highest_sales_month)
# print("Highest Sales:", highest_sales_value)

# # Q15. 
# # Create a final Monthly Business Report using resample() and .agg().
# monthly_report = df.resample("ME").agg({
#     "Sales": ["sum", "mean", "max", "min"],
#     "Orders": "sum",
#     "Profit": ["sum", "mean"],
#     "Customers": "mean"
# })

# print(monthly_report)

# categorical data

# df = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Riya", "Jay", "Pooja"],
#     "Age": [18, 22, 27, 35, 42, 29, 55, 31],
#     "Salary": [20000, 28000, 35000, 45000, 60000, 38000, 75000, 50000],
#     "Department": [
#         "IT", "HR", "IT", "Finance",
#         "HR", "IT", "Finance", "HR"
#     ],
#     "Performance": [
#         "Low", "Medium", "High", "Medium",
#         "High", "High", "Low", "Medium"
#     ]
# })

# print(df["Department"].dtype)
# df["Department"] = df["Department"].astype("category")
# print(df.dtypes)

# print(df["Department"].cat.categories)

# # cut :: Numerical Data → Categories 
# df["Age_Group"] = pd.cut(
#     df["Age"],
#     bins=[0, 20, 30, 40, 100],
#     labels=["Teen", "Young", "Adult", "Senior"]
# )

# print(df[["Name","Age","Age_Group"]])

# # qcut  :: equal number of data
# df["Salary_group"] = pd.qcut(
#             df["Salary"],
#             q=4,
#             labels=["Low","Medium","High","Very high"]
# )
# print(df[["Name","Salary","Salary_group"]])

# # category ordering
# df["Performance"] = pd.Categorical(
#     df["Performance"],
#     categories=["Low","Medium","High"],
#     ordered=True
# )
# df = df.sort_values("Performance")
# print(df[["Name","Performance"]])

# # Category Memory Optimization
# print(df["Department"].memory_usage(deep=True))

# df["Department"] = df["Department"].astype("category")
# print(df["Department"].memory_usage(deep=True))


# import pandas as pd

# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
#                     111, 112, 113, 114, 115],
    
#     "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan",
#              "Riya", "Jay", "Pooja", "Vivek", "Anjali",
#              "Rohit", "Meera", "Arjun", "Kavya", "Nikhil"],
    
#     "Age": [19, 24, 29, 35, 42, 27, 51, 31, 22, 46,
#             38, 26, 55, 33, 41],
    
#     "Salary": [22000, 28000, 35000, 45000, 62000,
#                38000, 75000, 50000, 25000, 68000,
#                48000, 32000, 85000, 55000, 65000],
    
#     "Department": [
#         "IT", "HR", "IT", "Finance", "HR",
#         "IT", "Finance", "HR", "IT", "Finance",
#         "IT", "HR", "Finance", "IT", "HR"
#     ],
    
#     "Performance": [
#         "Low", "Medium", "High", "Medium", "High",
#         "High", "Low", "Medium", "Low", "High",
#         "Medium", "High", "High", "Medium", "Low"
#     ],
    
#     "Education": [
#         "Graduate", "Postgraduate", "Graduate", "Graduate", "Postgraduate",
#         "Graduate", "Postgraduate", "Graduate", "Graduate", "Postgraduate",
#         "Graduate", "Postgraduate", "Postgraduate", "Graduate", "Graduate"
#     ]
# })

# print(df)

# # Basic Category

# # Q1. Check the data type of the Department column.
# print(df["Department"].dtype)

# # Q2. Convert the Department column from its current dtype to category.
# df["Department"] = df["Department"].astype("category")
# print(df["Department"].dtype)

# # Q3. Display all unique categories of the Department column using .cat.categories.
# print(df["Department"].cat.categories)

# # Q4. Convert the Education column into categorical dtype.
# df["Education"] = df["Education"].astype("category")
# print(df["Education"].dtype)

# # Q5. Create a new column Age_Group using pd.cut() with:

# # 0–20   → Teen
# # 21–30  → Young
# # 31–40  → Adult
# # 41–60  → Senior
# df["Age_Group"] = pd.cut(
#     df["Age"],
#     bins = [0,20,30,40,100],
#     labels = ["Teen","Young","Adult","Senior"]
# )
# print(df[["Name","Age","Age_Group"]])

# # Q6. Count how many employees belong to each Age_Group.
# result = df.groupby("Age_Group")["Employee_ID"].count()
# print(result)

# # Q7. Create a Salary_Level column using pd.cut():

# # 0–30000      → Low
# # 30000–50000  → Medium
# # 50000–70000  → High
# # 70000+       → Very High
# df["Salary_Group"] = pd.cut(
#     df["Salary"],
#     bins = [0,30000,50000,70000,100000],
#     labels = ["Low","Medium","High","Very High"]
# )
# print(df[["Name","Age","Salary_Group"]])

# # Q8. Create Salary_Quartile using pd.qcut() with 4 equal-sized groups:

# # Low
# # Medium
# # High
# # Very High

# df["Salary_Group"] = pd.qcut(
#     df["Salary"],
#     q=4,
#     labels=["Low","Medium","High","Very High"]
# )
# print(df[["Name","Salary","Salary_Group"]])

# # Q9. Count the number of employees in each Salary_Quartile.
# result = df.groupby("Salary_Group")["Employee_ID"].count()
# print(result)

# # Q10. Compare Salary_Level created with cut() and Salary_Quartile created with qcut().
# df["Salary_level"] = pd.cut(
#     df["Salary"],
#     bins=[0,30000,50000,70000,100000],
#     labels=["Low","Medium","High","Very High"]
# )


# df["Salary_Quartile"] = pd.qcut(
#     df["Salary"],
#     q=4,
#     labels=["Low","Medium","High","Very High"]

# )
# print(df[
#     ["Name", "Salary", "Salary_level", "Salary_Quartile"]
# ])

# # Q11. Convert Performance into an ordered categorical column with:

# # Low < Medium < High
# df["Performance"] = pd.Categorical(
#     df["Performance"],
#     categories = ["Low","Medium","High"],
#     ordered = True
# )


# # Q12. Sort the DataFrame according to the ordered Performance category.
# df = df.sort_values("Performance")
# print(df[["Name","Performance"]])

# # Q13. After ordering Performance, display only:

# # Name
# # Performance
# # Salary
# print(df[["Name","Performance","Salary"]])

# # 14. Check the memory usage of the Department column before and after converting it to category.
# print("Before")

# print(df["Department"].memory_usage(deep=True))

# print("After")
# df["Department"] = df["Department"].astype("category")

# print(df["Department"].memory_usage(deep=True))

# # Q15. ⭐ Final Challenge

# # Create a final DataFrame containing:

# # Employee_ID
# # Name
# # Age
# # Age_Group
# # Salary
# # Salary_Quartile
# # Department
# # Performance

# df["Department"] = df["Department"].astype("category")

# df["Age_Group"] = pd.cut(
#     df["Age"],
#     bins = [0,20,30,40,100],
#     labels = ["Teen","Young","Adult","Senior"]
# )

# df["Salary_Quartile"] = pd.qcut(
#     df["Salary"],
#     q=4,
#     labels=["Low","Medium","High","Very High"]

# )
# df["Performance"] = pd.Categorical(
#     df["Performance"],
#     categories = ["Low","Medium","High"],
#     ordered = True
# )

# df = df.sort_values("Performance")
# print(df[["Name","Performance"]])

# final_df = df[["Employee_ID",
#           "Name",
#           "Age",
#           "Age_Group",
#           "Salary",
#           "Salary_Quartile",
#           "Department",
#           "Performance"]]
# print(final_df)

# Missing value stratigies

# find missing value
# import numpy as np

# df = pd.DataFrame({
#     "Date": pd.date_range("2026-01-01", periods=10),
#     "Sales": [1000, 1200, np.nan, 1800, np.nan, 2200, 2500, np.nan, 3000, 3200],
#     "Profit": [100, np.nan, 180, np.nan, 220, 250, np.nan, 300, 320, np.nan],
#     "Customers": [10, 12, np.nan, 18, 20, np.nan, 25, 27, np.nan, 32]
# })
# print(df.isna())
# print(df.isna().sum())

# missing_percentage = df.isna().mean()*100
# print(missing_percentage)

# # missing rows
# print(df[df.isna().any(axis=1)])

# # remove missing columns
# print(df.dropna())

# # specific column ne delete karvi
# # specific columns na missing rows delete
# df = df.dropna(subset=["Sales"])
# print(df)

# fill with specific value
# df["Sales"] = df["Sales"].fillna(25)
# print(df)

# df["Profit"] = df["Profit"].fillna(df["Profit"].mean())
# print(df)

# df["Customers"] = df["Customers"].fillna(
#     df["Customers"].median()
# )
# print(df)

# df["Profit"] = df["Profit"].fillna(df["Profit"].mode()[0])
# print(df)

# fill with previous value
# df["Sales"] = df["Sales"].ffill()
# print(df)

# # fill with next value
# df["Profit"] = df["Profit"].bfill()
# print(df)

# # groupwise missing value filling
# df["Sales"] = df["Sales"].fillna(
#     df.groupby("Date")["Sales"].transform("mean")
# )
# print(df)

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115],

    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan",
             "Riya", "Jay", "Pooja", "Vivek", "Anjali",
             "Rohit", "Meera", "Arjun", "Kavya", "Nikhil"],

    "Age": [22, np.nan, 25, 31, np.nan,
            28, 45, 36, np.nan, 29,
            41, 24, 52, np.nan, 34],

    "Salary": [30000, 35000, np.nan, 48000, 52000,
               np.nan, 75000, 45000, 28000, np.nan,
               60000, 32000, np.nan, 55000, 47000],

    "Department": ["IT", "HR", "IT", np.nan, "Finance",
                   "IT", "Finance", "HR", np.nan, "Finance",
                   "IT", "HR", "Finance", np.nan, "HR"],

    "Performance": ["High", "Medium", np.nan, "High", "Medium",
                    np.nan, "Low", "High", "Medium", np.nan,
                    "High", "Low", "High", "Medium", np.nan],

    "Experience": [1, 3, np.nan, 7, 8,
                   np.nan, 15, 9, 2, 5,
                   np.nan, 3, 18, 6, np.nan]
})

print(df)

# Basic Missing Value Detection

# # Q1. Display the number of missing values in each column.
# print(df.isna())
# print(df.isna().sum())

# # Q2. Calculate the percentage of missing values in each column.
# print(df.isna().mean()*100)

# # Q3. Display only the rows that contain at least one missing value.
# print(df[df.isna().any(axis=1)])

# # Q4. Display only the rows where Salary is missing.
# print(df[df["Salary"].isna()])

# # dropna()

# # Q5. Remove all rows containing at least one missing value and store the result in a new DataFrame called clean_df.
# clean_df = df.dropna()
# print(clean_df)

# # Q6. Remove rows only when the Age value is missing. Keep rows with missing values in other columns.
# clean_df = df.dropna(subset=["Age"])
# print(clean_df)

# # fillna()

# # Q7. Fill missing Age values using the median Age.
# df["Age"] = df["Age"].fillna(df["Age"].median())
# print(df)

# # Q8. Fill missing Salary values using the median Salary.
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df)

# # Q9. Fill missing Department values using the mode of the Department column.
# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
# print(df)

# # Q10. Fill missing Performance values using the mode of the Performance column.
# df["Performance"] = df["Performance"].fillna(df["Performance"].mode()[0])
# print(df)

# ffill() and bfill()

# # Q11. Create a new column called Salary_FFill and fill missing Salary values using forward fill.
# df["Salary_FFill"] = df["Salary"].ffill()
# print(df[["Name","Salary","Salary_FFill"]])

# # Q12. Create a new column called Salary_BFill and fill missing Salary values using backward fill.
# df["Salary_BFill"] = df["Salary"].bfill()
# print(df[["Name","Salary","Salary_BFill"]])

# Group-wise Missing Value Strategy

# Q13. Fill missing Salary values using the mean Salary of the employee's Department.
df["Salary"] = df["Salary"].fillna(
    df.groupby("Department")["Salary"].transform("mean"))
print(df)

# Q14. After filling the missing values, verify that there are no missing values left in:

# Age
# Salary
# Department
# Performance

# df["Age"] = df["Age"].fillna(df["Age"].median())
# print(df)


# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df)

# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
# print(df)

# df["Performance"] = df["Performance"].fillna(df["Performance"].mode()[0])
# print(df)

# print(df.isna().sum())

# Q15 — Final Data Cleaning Challenge

# Create a completely cleaned DataFrame using these rules:

# Age → fill missing values with median Age
# Salary → fill missing values with Department-wise mean Salary
# Department → fill missing values with mode
# Performance → fill missing values with mode
# Experience → fill missing values with median Experience
# Verify the final DataFrame has no missing values.

# df["Age"] = df["Age"].fillna(df["Age"].median())
# df["Salary"] = df["Salary"].fillna(
#     df.groupby("Department")["Salary"].transform("mean")
# )
# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
# df["Performance"] = df["Performance"].fillna(df["Performance"].mode()[0])
# df["Experience"] = df["Experience"].fillna(df["Experience"].median())

# final_df = df[[
#     "Age",
#     "Salary",
#     "Department",
#     "Performance",
#     "Experience"
# ]]
# print(final_df)
# print(df.isna().sum())

# # interpolate
# df = pd.DataFrame({
#     "Day": [1, 2, 3, 4, 5],
#     "Sales": [100, np.nan, np.nan, 400, 500]
# })
# df["Sales"] = df["Sales"].interpolate()
# print(df)

# # Data validation
# # duplicated
# df = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Amit", "Rahul"],
#     "Salary": [30000, 40000, 30000, 50000]
# })

# print(df.duplicated())

# # duplicate row display
# print(df[df.duplicated()])

# # duplicate rows remove
# df = df.drop_duplicates()
# print(df)

# # Specific column પ્રમાણે duplicate
# df["Name"].duplicated()

# # equals
# # equals() માત્ર values જ નહીં, પરંતુ shape, labels અને corresponding values પણ compare કરે છે.
# df1 = pd.DataFrame({
#     "Name": ["Amit", "Neha"],
#     "Salary": [30000, 40000]
# })

# df2 = pd.DataFrame({
#     "Name": ["Amit", "Neha"],
#     "Salary": [30000, 40000]
# })
# print(df1.equals(df2))

# # compare
# df1 = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Rahul"],
#     "Salary": [30000, 40000, 50000]
# })

# df2 = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Rahul"],
#     "Salary": [30000, 45000, 50000]
# })
# print(df1.compare(df2))

# # check missing value
# print(df.isna().any())

# # check data type
# print(df.dtypes)

# # validate column name
# required_columns = [
#     "Employee_ID",
#     "Name",
#     "Age",
#     "Salary"
# ]
# missing_columns = set(required_columns) - set(df.columns)

# print(missing_columns)

# # validate unique values
# print(df["Name"].unique())

# # numique :: count the unique number
# print(df["Name"].nunique())

# # validate allowed values
# allowed_Name = {"Amit","Neha","Rahul"}

# invalid_values = set(df["Name"]) - allowed_Name

# print(invalid_values)

# # validate unique id
# print(df["Name"].is_unique)

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 110, 112],
#     "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Riya", "Jay", "Pooja", "Vivek", "Anjali", "Anjali", "Nikhil"],
#     "Age": [22, 25, np.nan, 31, 28, np.nan, 35, 29, 41, 26, 26, 33],
#     "Salary": [30000, 35000, 42000, np.nan, 50000, 55000, 60000, np.nan, 70000, 45000, 45000, 65000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR", "IT", "Marketing", "Marketing", "HR"],
#     "Performance": ["High", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Medium", "Medium", "High"]
# })

# # Q1 — Duplicate Rows
# # Check whether the DataFrame contains any completely duplicated rows.
# print(df.duplicated())

# # Q2 — Count Duplicates
# # Find the total number of duplicated rows.
# print(df.duplicated().sum())

# # Q3 — Display Duplicates
# # Display only the rows that are completely duplicated.
# print(df[df.isna().any(axis=1)])

# # Q4 — Duplicate Employee IDs
# # Check whether any Employee_ID values are duplicated.
# print(df.duplicated("Employee_ID"))

# # Q5 — Find Duplicate Employee IDs
# # Display the rows where Employee_ID is duplicated.
# print(df[df["Employee_ID"].duplicated(keep=False)])

# # Q6 — Unique Employee IDs
# # Check whether Employee_ID contains only unique values using is_unique.
# print(df["Employee_ID"].is_unique)

# # Q7 — Missing Values
# # Find the number of missing values in every column.
# print(df.isna().sum())

# # Q8 — Missing Value Percentage
# # Calculate the percentage of missing values for every column.
# print(df.isna().mean()*100)

# # Q9 — Data Types
# # Display the data type of every column.
# print(df.dtypes)

# # Q10 — Validate Required Columns
# # Check whether these required columns exist in the DataFrame:

# # Employee_ID
# # Name
# # Age
# # Salary
# # Department
# # Performance

# required_columns = [
#     "Employee_ID",
#     "Name",
#     "Age",
#     "Salary",
#     "Department",
#     "Performance"
# ]
# missing_columns = set(required_columns) - set(df.columns)
# print(missing_columns)

# # Q11 — Validate Department Values
# # Display all unique values present in the Department column.
# print(df["Department"].unique())

# # Q12 — Validate Allowed Departments
# # Allowed departments are:

# # IT
# # HR
# # Finance
# # Find any invalid department values.

# allowed_department = {"IT","HR","Finance"}
# invalid_values = set(df["Department"].dropna()) - allowed_department
# print(invalid_values)

# # Q13 — Compare Two DataFrames
# # Create a copy of df called df2, change Rahul's Salary from 42000 to 45000, and check whether df and df2 are exactly equal.

# df2 = pd.DataFrame({
#     "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 110, 112],
#     "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Riya", "Jay", "Pooja", "Vivek", "Anjali", "Anjali", "Nikhil"],
#     "Age": [22, 25, np.nan, 31, 28, np.nan, 35, 29, 41, 26, 26, 33],
#     "Salary": [30000, 35000, 45000, np.nan, 50000, 55000, 60000, np.nan, 70000, 45000, 45000, 65000],
#     "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR", "IT", "Marketing", "Marketing", "HR"],
#     "Performance": ["High", "Medium", "High", "Low", "Medium", "High", "Low", "Medium", "High", "Medium", "Medium", "High"]
# })

# print(df.equals(df2))

# # Q14 — Find Differences
# # Using compare(), find the difference between df and df2.
# print(df.compare(df2))

# # Q15 — Final Data Validation Report ⭐
# # Create a validation report containing:

# # Total rows
# # Total columns
# # Total duplicate rows
# # Total missing values
# # Missing values by column
# # Data types
# # Number of unique departments
# # Unique department values
# # Whether Employee_ID is unique

# Total rows and columns
total_rows = df.shape[0]
total_columns = df.shape[1]

# Total duplicate rows
total_duplicates = df.duplicated().sum()

# Total missing values
total_missing = df.isna().sum().sum()

# # Missing values by column
# missing_by_column = df.isna().sum()

# # Data types
# data_types = df.dtypes

# # Unique departments
# unique_departments = df["Department"].unique()

# # Number of unique departments
# number_of_departments = df["Department"].nunique()

# # Employee ID uniqueness
# employee_id_unique = df["Employee_ID"].is_unique

# print("===== DATA VALIDATION REPORT =====")

# print("Total Rows:", total_rows)
# print("Total Columns:", total_columns)
# print("Total Duplicate Rows:", total_duplicates)

# print("\nTotal Missing Values:", total_missing)

# print("\nMissing Values by Column:")
# print(missing_by_column)

# print("\nData Types:")
# print(data_types)

# print("\nNumber of Unique Departments:", number_of_departments)

# print("\nUnique Departments:")
# print(unique_departments)

# print("\nAre Employee IDs Unique?:", employee_id_unique)