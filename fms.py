class Food:
    def __init__(self, food_id, food_name, price, quantity):
        self.food_id = food_id
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.food_id} - {self.food_name} - RM{self.price:.2f} - Stock: {self.quantity}"


def find_food(food_list, food_id):
    for food in food_list:
        if food.food_id == food_id:
            return food
    return None


def add_food(food_list, food):
    if find_food(food_list, food.food_id):
        return False
    food_list.append(food)
    return True


def search_food(food_list, keyword):
    result = []

    for food in food_list:
        if keyword.lower() in food.food_name.lower():
            result.append(food)

    return result


def calculate_total_price(food, quantity):
    return food.price * quantity


def place_order(food, quantity):
    if quantity <= 0:
        return False

    if quantity > food.quantity:
        return False

    food.quantity -= quantity
    return True


def calculate_total_available(food_list):
    total = 0

    for food in food_list:
        total += food.quantity

    return total
