from product import Product
from product import Book
from product import Electronics
from product import Toy

from store import Store

from cart import Cart


online_store = Store()
cart = Cart()


war_and_peace = Book(1234, "War and Peace", "Leo Tolstoy", 2015, 50, 3)
air_purifier = Electronics(2635, "Air Purifier", "Xiaomi", 150, 5)
toy_bear = Toy(5436, "Toy Bear", "3-13", 80, 5)


online_store.add_product(war_and_peace)
online_store.add_product(air_purifier)
online_store.add_product(toy_bear)


while True:
    print("1. Show all products")
    print("2. Find product by name")
    print("3. Add product to cart")
    print("4. Show cart")
    print("5. Show total amount in cart")
    print("6. Delete product from cart")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print(online_store.all_products())

    elif choice == "2":
        product_name = input("Search: ")
        search_result = online_store.product_search_by_name(product_name)
        print("\n".join(f"{i+1}. {product}" for i,
              product in enumerate(search_result)))
    elif choice == "3":
        product_name = input("Add product to cart: ")
        search_result = online_store.product_search_by_name(product_name)
        if len(search_result) == 1:
            cart.add_to_cart(search_result[0])
            print(f"{search_result[0]} added to cart")
        elif len(search_result) > 1:
            search_list = "\n".join(
                f"{i+1}. {product}" for i, product in enumerate(search_result))
            print(f"Products found: {search_list}")
            print("Found more than one product. Please enter full name")
        elif len(search_result) == 0:
            print("Product not found")

    elif choice == "4":
        print(cart.show_cart())

    elif choice == "5":
        print(f"Total amount: {cart.cart_sum()} USD")

    elif choice == "6":
        product_name = input("Product to delete: ")
        search_result = cart.cart_search_by_name(product_name)
        if len(search_result) == 1:
            cart.remove_from_cart(search_result[0])
            print(f"{search_result[0]} removed from cart")
        elif len(search_result) > 1:
            search_list = "\n".join(
                f"{i+1}. {product}" for i, product in enumerate(search_result))
            print(f"Products found: {search_list}")
            print("Found more than one product. Please enter full name")
        elif len(search_result) == 0:
            print("Product not found")

    elif choice == "7":
        break
