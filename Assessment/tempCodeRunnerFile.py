# Prog.10
# Product Stock Shortage Report
# A product is low in stock if quantity < 10

class Solution:
    def low_stock_products(self, products):
        low_stock = []

        for product, quantity in products.items():
            if quantity < 10:
                low_stock.append(product)

        return low_stock


# -------- Main Program --------

# Example inventory dictionary
products = {
    "Laptop": 5,
    "Mouse": 50,
    "Keyboard": 8,
    "Monitor": 15,
    "PenDrive": 3
}

# Create object
obj = Solution()

# Call function
result = obj.low_stock_products(products)

# Print result
print("Products low in stock:", result)