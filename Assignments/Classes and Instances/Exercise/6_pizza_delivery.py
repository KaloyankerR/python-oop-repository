class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity
            self.price += (quantity * ingredient_price)
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients.keys():
                return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
            elif self.ingredients[ingredient] < quantity:
                return f'Please check again the desired quantity of {ingredient}!'
            self.ingredients[ingredient] -= quantity
            self.price -= (quantity * ingredient_price)
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def pizza_ordered(self):
        if not PizzaDelivery.ordered:
            PizzaDelivery.ordered = True
            all_ingredients = [f'{k}: {v}' for (k, v) in self.ingredients.items()]
            return f"You've ordered pizza {self.name} prepared with {', '.join(all_ingredients)} and the price will be {self.price}lv."
        return f"Pizza {self.name} already prepared and we can't make any changes!"
