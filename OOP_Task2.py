# Class: 
# A class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the created objects (instances) will have. 
# Think of a class as a template for a specific type of object.

# Object:
# An object is an instance of a class. 
# When a class is instantiated, an object is created that 
# contains its own unique data while sharing the structure defined by the class.

# Example

# class Dog:  # This is a class
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

# # Creating objects (instances) of the Dog class
# dog1 = Dog("Buddy", "Golden Retriever")  # dog1 is an object
# dog2 = Dog("Max", "Bulldog")              # dog2 is another object

# print(dog1.name)  # Output: Buddy
# print(dog2.breed) # Output: Bulldog

# Constructor Method (__init__) vs. __str__() Function

# Constructor Method (__init__): 

# This special method is called when an object is instantiated. 
# It initializes the attributes of the object. 
# The __init__ method allows you to set up initial values for an object's attributes when the object is created.


# __str__() Function:

# This method returns a string representation of the object when it is printed or converted to a string. 
# It’s used to provide a human-readable format of the object’s data, making it easier to understand what the object represents.

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# book1 = Book("1984", "George Orwell", 1949)

# print(book1)  
