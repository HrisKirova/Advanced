from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    VALID_TYPES = ["Chair", "HobbyHorse"]

    def produce_item(self, product_type: str, model: str, price: float):

        if product_type not in self.VALID_TYPES:
            raise Exception("Invalid product type!")
        if product_type == "Chair":
            self.products.append(Chair(model, price))
        elif product_type == "HobbyHorse":
            self.products.append(HobbyHorse(model, price))
        return f"A product of sub-type {self.products[-1].sub_type} was produced."

    VALID_STORES = ['FurnitureStore', 'ToyStore']
    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(F"{store_type} is an invalid type of store!")

        if store_type == "FurnitureStore":
            self.stores.append(FurnitureStore(name, location))
        elif store_type == "ToyStore":
            self.stores.append(ToyStore(name, location))
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity <= len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [p for p in products if p.sub_type.lower() in store.store_type.lower()]

        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = self.__find_store_by_name(store_name)
        if not store:
            raise Exception("No such store!")
        if store.products:
            return f"The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    # helper method
    def __find_store_by_name(self, store_name):
        return next((s for s in self.stores if s.name == store_name), None)

    def discount_products(self, product_model: str):
        discounted_products = [p for p in self.products if p.model == product_model]
        for product in discounted_products:
            product.discount()
        # can be also like that:
        # [p.discount() for p in discounted_products]
        return f"Discount applied to {len(discounted_products)} products with model: {product_model}"


    def request_store_stats(self, store_name: str):
        store = self.__find_store_by_name(store_name)
        if not store:
            raise Exception("There is no store registered under this name!")
        return store.store_stats()

    def statistics(self):
        model_counts = {}
        total_price = 0
        for product in self.products:
            total_price += product.price
            model = product.model
            if model not in model_counts:
                model_counts[model] = 0
            model_counts[model] += 1

        product_lines = [f"{model}: {count}" for model, count in sorted(model_counts.items())]
        store_names = [f'{store.name}' for store in sorted(self.stores, key=lambda s: s.name)]

        return (
            f"Factory: {self.name}\n"
            f"Income: {self.income:.2f}\n"
            f"***Products Statistics***\n"
            f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}\n"
            f"{chr(10).join(product_lines)}\n"
            f"***Partner Stores: {len(self.stores)}***\n"
            f"{chr(10).join(store_names)}"
        )