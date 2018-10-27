# Assert rises exception if boolean is false

a = 20
b = 20


if a < b:
    print(a," is less than ",b)
elif a==b:
    assert a!=b, "ERROR! Cant be the same number"
else:
    print(f"{b} is less than {a}")

# Try, if fails it will execute except based on its <ERROR TYPE> and do X or Y

c = 10
d = 0

try:
    e = c / d
except:
    print("ERROR Can't divde by zero")
    e = c
