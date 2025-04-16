import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo1(setup):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixture_demo2(setup):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixture_demo3(setup):
        print("I will execute steps in fixtureDemo3 method")
