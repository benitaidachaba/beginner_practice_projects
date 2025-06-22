length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

area = calculate_area(length, width)
print("The area of the rectangle is:", area)