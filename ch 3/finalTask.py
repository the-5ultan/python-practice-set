names = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "David"}
salaries = {101: 50000, 102: 60000, 103: 55000, 104: 70000}

while(True):
    id = int(input("Enter employee ID: "))
    if id in names and id in salaries:
        print(f"Employee Name: {names[id]}")
        print(f"Employee Salary: ${salaries[id]}")
    else:
        print("Employee not found.")