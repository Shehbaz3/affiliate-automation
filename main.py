def generate_product_list():
    # Example static list of products
    return [
        {"name": "Product 1", "price": 19.99, "url": "https://example.com/product1"},
        {"name": "Product 2", "price": 29.99, "url": "https://example.com/product2"},
        {"name": "Product 3", "price": 39.99, "url": "https://example.com/product3"},
    ]

def main():
    products = generate_product_list()
    for product in products:
        print(f"Name: {product['name']}, Price: ${product['price']}, Link: {product['url']}")

if __name__ == "__main__":
    main()
