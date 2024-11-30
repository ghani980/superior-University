#PART_1

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  
        self.num_doors = num_doors
    
    def additional_info(self):
        
        print(f"Number of Doors: {self.num_doors}")


class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)  
        self.features = features
    
    def additional_info(self):
        
        print(f"Luxury Features: {', '.join(self.features)}")


if __name__ == "__main__":
    
    car = Car("Toyota", "Corolla", 4)
    print("Car Info:")
    car.display_info()
    car.additional_info()
    print()

    
    luxury_car = LuxuryCar("Mercedes", "S-Class", 4, ["Heated Seats", "Sunroof", "Leather Interior", "Bose Sound System"])
    print("Luxury Car Info:")
    luxury_car.display_info()
    luxury_car.additional_info()


    #PART_2

   
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
       
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)  
        self.department = department
    
    def additional_info(self):
   
        print(f"Department: {self.department}")


class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position) 
        self.hours_worked = hours_worked
    
    def additional_info(self):
        
        print(f"Hours Worked: {self.hours_worked}")


if __name__ == "__main__":
    
    manager = Manager("Alice Johnson", "Project Manager", "IT Department")
    print("Manager Info:")
    manager.display_info()
    manager.additional_info()
    print()

    
    worker = Worker("Bob Smith", "Software Engineer", 40)
    print("Worker Info:")
    worker.display_info()
    worker.additional_info()

