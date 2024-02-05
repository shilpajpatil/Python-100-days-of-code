



import pytest

@pytest.fixture()
def setup():
    print("Setup method will get exicute first")
    yield
    print("I will be exicuting last")

def test_fixturedemo(setup):
    print("I will be get exicuted after the  setup method")



@pytest.fixture
def input_value():
   input = 39
   return input


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0