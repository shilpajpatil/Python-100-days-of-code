
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

@pytest.fixture()
def newdata():
    print("inside fixture newdata")
    return ["Shilpa","Patil","Pshilpa056@gmail.com"]

@pytest.fixture(params= [("chrome","Shilpa"), ("Firefox","patil"), ("IE","lock")])
def crossBrowser(request):
    return request.param
