import re

# https://pythex.org/


# look for regex and return in group() string 
print(type(re.search(r'^Co.k.e', 'Cookie').group()))

pattern = r"Cookie"
sequence= "Cookie"

if re.match(pattern,sequence):
    print("Match!")
else:
    print("No match")

