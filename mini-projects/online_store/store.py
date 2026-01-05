from product import Product


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def all_products(self):
        all_products = []
        for product in self.products:
            all_products.append(str(product))
        return f"\n".join(all_products)

    def product_search_by_name(self, name: str):
        result = []
        for product in self.products:
            if name.lower() in product.name.lower():
                result.append(product)
        return result
