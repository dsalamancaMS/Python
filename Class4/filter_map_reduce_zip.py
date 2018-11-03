# Filter example

a = [0,1,2,3,4,5,6]

my_labda = lambda x: x % 2 == 0

stuff = filter(my_labda,a)

#need to transform to list, filter creates a filter type object:
print(stuff) 

filtered = list(stuff)

print(filtered)

# list comprehension

result = [i for i in a if my_labda(i)] 

print(result)

# --------------------------- MAP ----------------------------------------------------

# map performs X on each item in array Y
# map returns object of type map 

power_of = map(lambda x: x**2, a)

print(power_of)

power_of = list(power_of)

print(power_of)

# ---------------------------- Reduce --------------------------
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

print(product)

reduce_str = reduce((lambda x,y: x + y), ['hello','you', 'person'])

print(reduce_str)

# --------------------- Zip --------------------------------
# Unpack a,b = ('a','b')
# Zip as in Zipper, unifies lists

list_1 = ['a','b','c']

list_2 = ['1','2','3']

my_zip = zip(list_1,list_2)

# un_zip = zip(*my_zip)


my_dict = dict(my_zip)

print(my_dict)