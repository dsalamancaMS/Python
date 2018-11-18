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

email_address= 'Please contact us at: support_disk-denis@email.com'
# it can be search of findall functions.
# to replace you can use re.sub
match= re.search(r'([\w\.\-\_]+)@([\w\.]+)', email_address)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))

pattern_2 = "C"
sequence1 = "IceCream"

boolean_result = all([re.match(pattern, sequence1)])
print(boolean_result)

