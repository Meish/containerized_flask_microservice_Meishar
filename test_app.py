from app import home, addition, multiply

def test_home():
    assert('Hello World! I can make addition at route /add' == home())

def test_add():
    assert(addition(1,2) == '3')
    assert(addition(3,2) == '5')
    assert(addition(1,5) == '6')
    assert(addition(150,-32) == '118')

def test_multiply():
    assert(multiply(1,2) == '2')
    assert(multiply(3,2) == '6')
    assert(multiply(1,5) == '5')
    assert(multiply(150,0) == '0')
