# Function definitions

def my_print():
    print("hello")


my_print()
my_print()


# List Comprehension, will do X for i in 10 times.
[my_print() for i in range(10)]

[print(i) for i in range(5)]

# _ can just be used to not declare var

for _ in range(2):
    my_print()


# Get Parameters
def my_print2(message):
    print(message)

my_print2('\n'"sup")


# pointers to functions
new_print = my_print2

new_print("stuff")


def plus(a,b):
    return a + b

def substract(a,b):
    return a - b

print('\n')

# Dictionary of functions works like a switch.
taco_calculator = {
    'sumar': plus,
    'restar': substract
}

print(taco_calculator['sumar'](2,3))

