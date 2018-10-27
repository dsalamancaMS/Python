# Try, if fails it will execute an except based on its <ERROR TYPE> and do X or Y, if no error else is executed, finally will always be exectued

c = 10
d = 0

try:
    e = c / d
except ZeroDivisionError:
    print("ERROR Can't divde by zero")
    e = c
else: 
    print("No by zero division")
finally:
    print("Im always excecuted")