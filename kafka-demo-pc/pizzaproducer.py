import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames = [
            'Magherita',
            'Divaloa',
            'Mari & Monti',
            'salami',
            'pepperoni'
        ]
        return validPizzaNames[random.randint(0,len(validPizzaNames)-1)]