pizza_types = {"Margherita": "Classic", "Pepporoni": "Spicy", "Veggie": "Fresh"}
print(pizza_types["Veggie"])
pizza_types["Veggie"]="Tasty"
print(pizza_types["Veggie"])
for pizza in pizza_types:
    print(pizza,pizza_types[pizza])
print("Via key value syntax : ")
for key , value in pizza_types.items():
    print(key,value)
if "Veggie" in pizza_types:
    print("Pizza is Veggie")
pizza_types["Peppy"]="Panner"
print(pizza_types)
print(pizza_types.pop("Peppy"))#if passes simple pop then pass a key
#print(pizza_types.popitem())  #removed last value 
del pizza_types["Pepporoni"] # removed from memory
print(pizza_types)
pizza_shop = {
    "Veg": {"Margherita": "Classic", "Farmhouse": "Loaded"},
    "Non-Veg": {"Pepperoni": "Spicy", "Chicken": "Savory"}
}
print(pizza_shop["Veg"]["Margherita"])
sqaured_num={x:x**2 for x in range(6)}
print(sqaured_num)
keys = ["Margherita", "Pepporoni", "Veggie"]
default_value = "Delicious"
pizza_dict = dict.fromkeys(keys, default_value)
print(pizza_dict)