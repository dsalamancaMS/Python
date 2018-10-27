# For loops
# Basic for structure

for i in [1,2,3,4,5]:
    print(i)


names = ['denis','eli','jose','pedro','david']


# Prints cycle number and value
for i in enumerate(names):
    print(i)

# Enumerate returns 2 values, we can store the values like this
# format on string will replace first value witn first {} and so on

for enumarate_value, i in enumerate(names):
    print('The index is {} for value {}'.format(enumarate_value,i))

# Other forms of formatting:

for enumarate_value, i in enumerate(names):
    print(f'The index is {enumarate_value} for value {i}')