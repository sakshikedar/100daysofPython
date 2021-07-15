import random

fruits = ["Blueberry",
        "Orange",
        "Strawberry",
        "Banana",
        "Apple"]

food = ["Maggie",
          "Dahi-vada",
          "Pani-puri",
          "Sushi",
          "Pan-cake",
          "Choclate truffle"]

random_fruits = random.choice(fruits)
random_food = random.choice(food)


print(f"You should eat {random_food} with {random_fruits}")