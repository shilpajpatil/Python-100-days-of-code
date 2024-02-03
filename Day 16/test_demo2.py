
import math
import pytest

#@pytest.mark.smoke
#@pytest.mark.skip



def test_demo2():

    msg = "Hello";
    assert msg == "Hi", "Strings does not match"


def test_sqrt():
    num = 144;
    assert math.sqrt(num)==12 ," it does not match"