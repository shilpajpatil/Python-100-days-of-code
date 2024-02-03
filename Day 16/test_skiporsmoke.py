

# Any pytest file should start with test_
#pytest method starts with test method
# Any code  shoud be wrapped in  function

import math
import pytest


#def test_firstProgram():
@pytest.mark.smoke
def test_sqrt():
    num = 25;
    assert math.sqrt(num)==5


def test_square():
    num = 7
    assert 7 *7 ==49

def test_quality():
    assert 10==10



