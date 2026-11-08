# Strings operations and methods

# Slicing
names="Shubham"
print(names[0:5])
print(names[:5])
# Python will automatically add len(names) and perform further action like len(names)-3=2 
print(names[-3:-1])
# len
print(len(names))
#strip for space used in web dev 
space ="  Shubham Bither  "
print(space.strip())
fruits="apple,mango,papaya,banana"
print(fruits.split(","))
quantity=2
type="pizza"
order="I order {} boxes of {}"
print(order.format(quantity,type))
pizza_variety=('Farmhouse','Peppy Paneer','Veggie Paradise')
print(pizza_variety)
print("/".join(pizza_variety))
# use r or / 
pizza=r"c:\user\pwd" # cannot use single \ as it works it escape characters, use \\ or r
print(pizza)
