import sqlite3

# Connect to database
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 department TEXT NOT NULL,
 salary REAL NOT NULL
)
''')

# Add Employee
def add_employee():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))
    cursor.execute("INSERT INTO employee (name, department, salary) VALUES (?, ?, ?)", (name, dept, salary))
    conn.commit()
    print("Employee added successfully.\n")

# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    print("ID\tName\t\tDepartment\tSalary")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    print()

# Search Employee
def search_employee():
    emp_id = input("Enter Employee ID: ")
    cursor.execute("SELECT * FROM employee WHERE id=?", (emp_id,))
    emp = cursor.fetchone()
    if emp:
        print("ID\tName\tDepartment\tSalary")
        print(f"{emp[0]}\t{emp[1]}\t{emp[2]}\t{emp[3]}\n")
    else:
        print("Employee not found.\n")

# Update Employee
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    name = input("Enter new name: ")
    dept = input("Enter new department: ")
    salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE employee SET name=?, department=?, salary=? WHERE id=?", (name, dept, salary, emp_id))
    conn.commit()
    print("Employee updated successfully.\n")

# Delete Employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    cursor.execute("DELETE FROM employee WHERE id=?", (emp_id,))
    conn.commit()
    print("Employee deleted successfully.\n")

# Menu
def menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
conn.close()
