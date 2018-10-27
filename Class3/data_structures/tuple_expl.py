# Create a Tuple

# tuples are inmutable and declared with ()
my_tuple=('1','2','hello')

print(type(my_tuple))

# Slices also work in tuples

print(my_tuple[:])

print(my_tuple[1:2])

my_list= ['one','two','three']


# Returns a copy, does not transform into tuple
tuple(my_list)

print(type(my_list))

# To transform into tuple:

my_list = tuple(my_list)

print(type(my_list))


