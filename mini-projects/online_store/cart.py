from product import Product


class Cart:
    def __init__(self):
        self.products_in_cart = []

    def add_to_cart(self, product):
        if not isinstance(product, Product):
            raise TypeError("Can only add Product instances")
        if product.product_is_available():
            self.products_in_cart.append(product)
            product.amount -= 1
        else:
            raise ValueError("Product is out of stock")

    def show_cart(self):
        if not self.products_in_cart:
            return "Cart is empty"
        return "\n".join(f"{i+1}. {product}" for i, product in enumerate(self.products_in_cart))

    def remove_from_cart(self, product):
        if not isinstance(product, Product):
            raise TypeError("Can only remove Product instances")
        try:
            self.products_in_cart.remove(product)
            product.amount += 1
        except ValueError:
            raise ValueError("Product is not in the cart")

    def cart_sum(self):
        return sum(product.price for product in self.products_in_cart)

    def cart_search_by_name(self, name: str):
        result = []
        for product in self.products_in_cart:
            if name.lower() in product.name.lower():
                result.append(product)
        return result
