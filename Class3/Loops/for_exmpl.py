# For loops
# Basic for structure

for i in [1,2,3,4,5]:
    print(i)


names = ['denis','eli','jose','pedro','david']

print('\n')


# Else is to execute a command right after loop finishes. It will be executed only if for is executed
for i in names:
    print(names)
else:
    print('\n')

# Prints cycle number and value

for i in enumerate(names):
    print(i)
else:
    print('\n')

# Printing value in index

for index,i in enumerate(names):
    print(names[index])
else:
    print('\n')

# Enumerate returns 2 values, we can store the values like this
# format on string will replace first value witn first {} and so on

for enumarate_value, i in enumerate(names):
    print('The index is {} for value {}'.format(enumarate_value,i))
else:
    print('\n')
# Other forms of formatting:

for enumarate_value, i in enumerate(names):
    print(f'The index is {enumarate_value} for value {i}')
else:
    print('\n')
# Sorting in reverse

for enumarate_value, i in enumerate(sorted(names, reverse=True)):
    print(f'The index is {enumarate_value} for value {i}')
else:
    print('\n')