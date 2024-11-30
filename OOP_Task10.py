import csv


class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    
   
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

   
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
    
   
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}"


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department
    
   
    def get_department(self):
        return self.__department
    
    def set_department(self, department):
        self.__department = department
    
    def display_info(self):
        return super().display_info() + f", Department: {self.__department}"


class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked
    
    
    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked
    
    def display_info(self):
        return super().display_info() + f", Hours Worked: {self.__hours_worked}"


def read_employee_data(filename):
    """Reads employee data from a CSV file and returns a list of Employee objects."""
    employees = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[3] == "Manager":
                    employee = Manager(row[0], int(row[1]), float(row[2]), row[4])
                elif row[3] == "Worker":
                    employee = Worker(row[0], int(row[1]), float(row[2]), int(row[4]))
                employees.append(employee)
    except FileNotFoundError:
        print(f"{filename} not found. A new file will be created.")
    return employees

def add_employee_data(filename, employee):
    """Adds new employee data to the CSV file."""
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(employee, Manager):
            writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "Manager", employee.get_department()])
        elif isinstance(employee, Worker):
            writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "Worker", employee.get_hours_worked()])

def update_employee_data(filename, employees):
    """Updates employee information and saves it back to the CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Salary', 'Type', 'Department/Hours Worked'])
        for employee in employees:
            if isinstance(employee, Manager):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "Manager", employee.get_department()])
            elif isinstance(employee, Worker):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "Worker", employee.get_hours_worked()])

def delete_employee_data(filename, name):
    """Deletes employee data from the CSV file by name."""
    employees = read_employee_data(filename)
    employees = [employee for employee in employees if employee.get_name() != name]
    update_employee_data(filename, employees)


def display_all_employees(employees):
    """Displays all employee information."""
    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee.display_info())
            print()

def get_employee_choice():
    """Returns the user's choice from the menu."""
    print("\nEmployee Management System")
    print("1. Add New Employee")
    print("2. Display All Employees")
    print("3. Update Employee Information")
    print("4. Delete Employee")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def add_new_employee():
    """Adds a new employee based on user input."""
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    type_of_employee = input("Enter type (Manager/Worker): ").lower()

    if type_of_employee == "manager":
        department = input("Enter department: ")
        new_employee = Manager(name, age, salary, department)
    elif type_of_employee == "worker":
        hours_worked = int(input("Enter hours worked: "))
        new_employee = Worker(name, age, salary, hours_worked)
    else:
        print("Invalid employee type!")
        return None
    return new_employee

def update_employee():
    """Updates an employee's information."""
    name = input("Enter the name of the employee to update: ")
    employees = read_employee_data('employee_data.csv')
    employee = None
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            employee = emp
            break
    if employee:
        print("Employee found. Update details:")
        new_name = input(f"Current Name: {employee.get_name()}. Enter new name (leave blank to keep the same): ")
        if new_name:
            employee.set_name(new_name)
        
        new_age = input(f"Current Age: {employee.get_age()}. Enter new age (leave blank to keep the same): ")
        if new_age:
            employee.set_age(int(new_age))
        
        new_salary = input(f"Current Salary: {employee.get_salary()}. Enter new salary (leave blank to keep the same): ")
        if new_salary:
            employee.set_salary(float(new_salary))
        
        if isinstance(employee, Manager):
            new_department = input(f"Current Department: {employee.get_department()}. Enter new department (leave blank to keep the same): ")
            if new_department:
                employee.set_department(new_department)
        elif isinstance(employee, Worker):
            new_hours = input(f"Current Hours Worked: {employee.get_hours_worked()}. Enter new hours (leave blank to keep the same): ")
            if new_hours:
                employee.set_hours_worked(int(new_hours))

        update_employee_data('employee_data.csv', employees)
    else:
        print(f"No employee found with the name {name}")

def delete_employee():
    """Deletes an employee from the records."""
    name = input("Enter the name of the employee to delete: ")
    delete_employee_data('employee_data.csv', name)
    print(f"Employee {name} deleted.")


if __name__ == "__main__":
    filename = 'employee_data.csv'
    employees = read_employee_data(filename)

    while True:
        choice = get_employee_choice()

        if choice == '1':
            new_employee = add_new_employee()
            if new_employee:
                add_employee_data(filename, new_employee)
                employees.append(new_employee)
        elif choice == '2':
            display_all_employees(employees)
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
