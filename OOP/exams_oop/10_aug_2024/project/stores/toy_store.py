from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    INITIAL_CAPACITY = 100
    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)


    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        from collections import defaultdict
        models_stats = defaultdict(list)

        for product in self.products:
            models_stats[product.model].append(product.price)
        sorted_models = sorted(models_stats)
        models_info = []
        for model, prices in sorted_models:
            count = len(prices)
            avg_price = sum(prices) / count
            models_info.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")
        furniture_all = "\n".join(models_info)
        profit = self.get_estimated_profit()
        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{profit}\n"
                f"**Toys for sale:\n"
                f"{furniture_all}").strip()


