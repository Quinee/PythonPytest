import pytest


def test_pract():
    print("hi")


def test_pract2():
    assert 2 == 3,"Numbers dont match"

@pytest.mark.xfail
def test_greet():
    print("Greet")



def test_greet2():
    print("Greet2")
