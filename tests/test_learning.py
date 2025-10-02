from learning import greet, add, multiply


def test_greet():
    assert greet("Enock") == "Hello, Enock!"


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20
