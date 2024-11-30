class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def main():
    try:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        
        rect = Rectangle(width, height)
        
        # Display rectangle details
        print(rect)
        
        # Calculate and display the area
        print(f"Area: {rect.area()}")
        
        # Calculate and display the perimeter
        print(f"Perimeter: {rect.perimeter()}")
        
    except ValueError:
        print("Please enter valid numbers for width and height.")

if __name__ == "__main__":
    main()
