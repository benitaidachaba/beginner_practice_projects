# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

# Example usage
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
product_quantity = int(input("Enter the product quantity: "))

product = Product(product_name, product_price, product_quantity)
print(f"The total value of {product.name} in stock is: ${product.total_value():.2f}")