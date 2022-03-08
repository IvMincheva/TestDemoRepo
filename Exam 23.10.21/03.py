def shopping_list(budget, **kwargs):
    products = {x: kwargs[x] for x in kwargs}
    bought_products = []
    if budget < 100:
        return "You do not have enough budget."
    # while
        # for product in products:
    if len(bought_products) <= 5 or len(products) > 0:
        for k, v in products.items():
            # print(k, v)
            total = v[0]*v[1]
            if total <= budget:
                bought_products.append(k)
                budget -= total

        if not bought_products:
            return "You do not have enough budget."
        else:
            for el in bought_products:
                return f"You bought {el} for {total:.2f} leva."


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))

