import pandas as pd

df = pd.read_csv("employee.csv")

print("Employee Data:")
print(df)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nSalary by Department:")
print(df.groupby("Department")["Salary"].mean())
import matplotlib.pyplot as plt

dept_salary = df.groupby("Department")["Salary"].mean()

dept_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.savefig("employee_salary_chart.png")

plt.show()