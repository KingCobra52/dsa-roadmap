products = [
    {"name": "Laptop", "price": 1000, "rating": 4.5},
    {"name": "Phone",  "price": 500,  "rating": 4.8},
    {"name": "Tablet", "price": 500,  "rating": 4.2}
]

print(sorted(products, key = lambda product: (product["price"], -product["rating"])))
#ascending by default -> cheapest first
