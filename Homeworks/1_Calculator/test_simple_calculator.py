def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

def ask_number():
    a = input('Type a number ')
    return a

def validate_num(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def error_loop():
    a = ask_number()
    while validate_num(a) != True:
        print('\nERROR! That is not a number....','Try again!\n')
        a = ask_number()
    return float(a)

def get_numbers():
    a = error_loop()
    b = error_loop()
    return a,b

def option_1_add():
    numbers = get_numbers()
    return add(numbers[0],numbers[1])

def option_2_substract():
    numbers = get_numbers()
    return substract(numbers[0],numbers[1])

def option_3_divide():
    numbers = get_numbers()
    return divide(numbers[0],numbers[1])

def option_4_multiply():
    numbers = get_numbers()
    return multiply(numbers[0],numbers[1])

menu_functions = {
       '1': option_1_add,
       '2': option_2_substract,
       '3': option_3_divide,
       '4': option_4_multiply,
       '5': exit
     }

menu_operations = {
    '1': '****Add Numbers****',
    '2': '****Substract Numbers****',
    '3': '****Divide Numbers****',
    '4': '****Multiply Numbers****',
    '5': '****Ciao!!!****'
}

def validate_opt(option_test):
    try:
        menu_functions[option_test]
        return True
    except KeyError:
        return False


def print_menu():
    print(
   " >Press '1' for adding two numbers.",'\n',
   ">Press '2' for substracting two numbers.",'\n',
   ">Press '3' for dividing two numbers.",'\n',
   ">Press '4  for multiplying two numbers.",'\n'
   " >Press '5' to exit."
 )


def main():
    print('Welcome to the PyCalculator', '\n')
    option = 0
    while option != '5':
        print_menu()
        option = input('Selection: ')
        while validate_opt(option) != True:
            print('\nERROR!! Wrong Option Selected... Try Again...')
            print_menu()
            option = input('Selection: ') 
        print('\n',menu_operations[option])
        print('Result: ',menu_functions[option](),'\n')


def test_add():
    assert add(1,1) == 2

def test_substract():
    assert 0 == substract(1,1)

def test_divide():
    assert 2 == divide(10,5)

def test_multiply():
    assert 4 == multiply(2,2)

main()


