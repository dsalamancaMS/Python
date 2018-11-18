def add(a,b):
    return a + b

# Tuple with values
a = (1,2)

# * unpacks values of tuple
print(add(*a))

# makes values into key=value pairs
kargs = {'a':1, 'b':2}
result = add(**kargs)
print(a)