from app import home

def test_home():
    assert('Hello World! I can make change at route: /change' == home())