def test_division_entera():
    num1 = 10
    num2 = 3

    my_div = num1 // num2
    print(my_div)
    assert 3 == my_div

def test_division_exacta():
    num1 = 10
    num2 = 3

    my_div = num1 / num2
    print(my_div)
# Rises Exception if not true, assert <expression>, <error message>
    assert 3 == my_div, "Not an int"