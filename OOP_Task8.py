import csv


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
       
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position
    
    def display_info(self):
       
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")


class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)  
        Employee.__init__(self, employee_id, position)  
        self.department = department
    
    def display_info(self):
       
        Person.display_info(self)
        Employee.display_info(self)
        print(f"Department: {self.department}")
    
    def additional_info(self):
       
        print(f"Department: {self.department}")


def read_employee_data(filename):
    """Reads employee data from a CSV file."""
    employees = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                name, age, employee_id, position, department = row
                staff = Staff(name, int(age), employee_id, position, department)
                employees.append(staff)
    except FileNotFoundError:
        print(f"{filename} not found. A new file will be created.")
    return employees

def add_employee_data(filename, staff):
    """Adds new employee data to the CSV file."""
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([staff.name, staff.age, staff.employee_id, staff.position, staff.department])

def save_employee_data(filename, employees):
    """Saves all employee data to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Employee ID', 'Position', 'Department'])  
        for staff in employees:
            writer.writerow([staff.name, staff.age, staff.employee_id, staff.position, staff.department])


if __name__ == "__main__":
    
    filename = 'employee_data.csv'

    
    employees = read_employee_data(filename)

    
    print("\nCurrent Employee Data:")
    for emp in employees:
        emp.display_info()
        print()

    
    new_staff = Staff("John Doe", 30, "E12345", "Software Developer", "IT")
    add_employee_data(filename, new_staff)

    
    save_employee_data(filename, employees + [new_staff])

    
    print("\nUpdated Employee Data:")
    employees = read_employee_data(filename)
    for emp in employees:
        emp.display_info()
        print()
