pizza_types = ("Margherita", "Pepporoni", "Veggie")

print(len(pizza_types))

more_pizza = ("Cheese", "Paneer")
all_pizza = more_pizza + pizza_types
print(all_pizza)

if "Veggie" in all_pizza:
    print("I have veggie pizza")

more_pizza = ("Cheese", "Paneer", "Cheese")
print(more_pizza)
print(more_pizza.count("Cheese"))
