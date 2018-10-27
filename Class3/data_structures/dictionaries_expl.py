# Dictonaries, key value pairs

my_dict = {'Denis': 116150555, 'Person1':12345}

# Show Value of key:

print(my_dict['Denis'])

# Change vlaue of key: 

my_dict['Person1'] = 54321


print(my_dict)

# Assign list to value

my_dict['Person1'] = [1,2,3,4]

print(my_dict)

# Delete key value pair

del(my_dict['Person1'])

# Dict from scratch

slang_dict = {}

# If key is not found, its created.

slang_dict['Mae'] = 'Dude'

print(slang_dict)

# Other way with function

slang_dict.update({'La Choza': 'The House'})

print(slang_dict)

# Print values:

print(slang_dict.values())

# Print Keys

print(slang_dict.keys())

print(slang_dict.items())

# Create dictionaries 

dir_dict = dict(denis='heredia',marvin='perez zeledon')

# How to merge two dict, ** gets contents in format key=value

merged_dict = dict(**my_dict,**slang_dict)


print(merged_dict)

# Show lenght of dict or list

print(len(merged_dict))



