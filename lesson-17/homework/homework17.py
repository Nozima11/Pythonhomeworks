# 1
import pandas as pd
import numpy as np
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
df.rename(columns={"First Name": "first_name", "Age": "age"}, inplace=True)
print(df.head(3))
mean_age = df['age'].mean()
print(f"Mean age: {mean_age}")
print(df[['first_name', 'City']])
df['Salary'] = np.random.randint(40000, 100000, size=len(df))
print(df.describe())

# 2
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print(f"Maximum Sales: {max_sales}, Maximum Expenses: {max_expenses}")

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print(f"Minimum Sales: {min_sales}, Minimum Expenses: {min_expenses}")

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print(f"Average Sales: {avg_sales}, Average Expenses: {avg_expenses}")

# 3
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

expenses.set_index('Category', inplace=True)

max_expense = expenses.max(axis=1)
print("Maximum expense per category:")
print(max_expense)

min_expense = expenses.min(axis=1)
print("Minimum expense per category:")
print(min_expense)

avg_expense = expenses.mean(axis=1)
print("Average expense per category:")
print(avg_expense)
