# While loops

# structure is while (boolean):

while True:
    print("looop")
    break


boolean = True
i=0

while boolean:
    i+=1
    print(f'Current value {i}')
    if i == 4:
        boolean= False
        print(f'Value is now {i}, we exit loop')
else:
    print("im an else")