number = int(input("Enter a number: "))
remainder = number % 2
def is_odd(number):
    """Check if a number is odd."""
    if remainder == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")
is_odd(number)
# This code takes an integer input from the user and checks if it is odd or even.
