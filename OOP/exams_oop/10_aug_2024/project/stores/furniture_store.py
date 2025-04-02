from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)


    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        from collections import defaultdict
        models_data = defaultdict(list)

        for product in self.products:
            models_data[product.model].append(product.price)

        sorted_models = sorted(models_data.items())
        models_info = []
        for model, prices in sorted_models:
            count = len(prices)
            avg_prices = sum(prices) / count
            models_info.append(f"{model}: {count}pcs, average price: {avg_prices:.2f}")
        furniture_all = "\n".join(models_info)
        profit = self.get_estimated_profit()
        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{profit}\n"
                  f"**Furniture for sale:\n"
                  f"{furniture_all}"
                ).strip()

