class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget
        self._expenses = 0

    # Getter and setter for category name
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, new_name):
        self._category_name = new_name

    # Getter and setter for allocated budget
    def get_allocated_budget(self):
        return self._allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self._allocated_budget = new_budget
        else:
            print("Invalid budget amount. Budget should be a positive number.")

    # Getter for expenses
    def get_expenses(self):
        return self._expenses

    # Setter for expenses (optional, since expenses are managed internally)
    def set_expenses(self, amount):
        self._expenses = amount

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount >= 0:
            self._expenses += amount
        else:
            print("Invalid expense amount. Expense should be a positive number.")

    # Method to calculate remaining budget
    def remaining_budget(self):
        return self._allocated_budget - self._expenses

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget}")
        print(f"Expenses: ${self._expenses}")
        print(f"Remaining Budget: ${self.remaining_budget()}")


# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()

    # Test setters
    food_category.set_category_name("Groceries")
    food_category.set_allocated_budget(600)
    food_category.add_expense(50)

    food_category.display_category_summary()
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


# Test the functionality
if __name__ == "__main__":
    # Create instances of each subclass
    my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
    my_electronic = Electronic("456", "Smartphone", 399.99, "6.7-inch display, 128GB storage")
    my_clothing = Clothing("789", "T-shirt", 19.99, "Large")

    # Display information for each product
    print("Book Information:")
    my_book.display_info()
    print("\nElectronic Information:")
    my_electronic.display_info()
    print("\nClothing Information:")
    my_clothing.display_info()
