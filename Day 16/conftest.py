
import pytest

@pytest.fixture(scope = "class")
def setup():
    print("Setup method will get exicute first")
    yield
    print("I will be exicuting last")




@pytest.fixture
def input_value():
   input = 39
   return input