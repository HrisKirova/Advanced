def shopping_list(budget: int, **product_list):
    if budget < 100:
        return "You do not have enough budget."

    basket = {}
    result = []  # Store messages to return them later

    for product, (price, quantity) in product_list.items():
        total_price = price * quantity

        if len(basket) >= 5:  # Stop if basket is full
            break

        if total_price <= budget:  # Buy only if within budget
            basket[product] = total_price
            budget -= total_price
            result.append(f"You bought {product} for {total_price:.2f} leva.")

    return "\n".join(result)  # Return all messages as a single string


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
