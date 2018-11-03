from simple_calculator import add,substract,divide,multiply

def test_add():
    assert add(1,1) == 2

def test_substract():
    assert 0 == substract(1,1)

def test_divide():
    assert 2 == divide(10,5)

def test_multiply():
    assert 4 == multiply(2,2)